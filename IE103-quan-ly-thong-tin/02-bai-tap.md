# IE103 — Bài tập và lời giải

Dùng schema/dữ liệu trong [lab](thuc-hanh/README.md). Mỗi câu SQL phải nêu kết quả kỳ vọng trước khi chạy. Các tên người trong lab là dữ liệu giả.

## Đề bài

1. Thiết kế ERD thư viện với nhiều bản sao cho mỗi đầu sách. Khóa lượt mượn là gì? Thông tin nào thuộc đầu sách, thông tin nào thuộc bản sao?
2. Cho R(A,B,C,D), F={A→B, B→C, A→D}. Tính A+, tìm candidate key; chuẩn hóa thành 3NF và giải thích lossless.
3. Liệt kê độc giả có ít nhất 2 lượt mượn.
4. Liệt kê mọi độc giả và số lượt mượn, kể cả bằng 0.
5. Tìm sách chưa từng được mượn bằng NOT EXISTS.
6. Tìm các lượt chưa trả, kèm tên độc giả và tựa sách, sắp theo loan_id.
7. Vì sao `WHERE returned_on = NULL` sai? Sửa lại.
8. Cho bảng phải của NOT IN có NULL; giải thích kết quả bất ngờ và viết phương án thay.
9. Dữ liệu đăng ký R(MaSV,MaMH,TenSV,TenMH,Diem) có các FD trong ghi chú. Chỉ ra 2NF bị vi phạm chỗ nào và tách bảng.
10. Viết XPath tìm title của book có id B01; viết XQuery lấy title những sách năm >2021.
11. Mô tả transaction chuyển 100 từ A sang B, kiểm tra số dư và xử lý khi bước cộng thất bại.
12. Hai request cùng mượn một cuốn chưa có ai mượn. Vì sao “SELECT trước rồi INSERT” ở ứng dụng có thể sai? Đưa cách ngăn ở CSDL.
13. Chọn quan hệ/document/graph cho sổ giao dịch ngân hàng, catalog sản phẩm linh hoạt, mạng bạn bè; giải thích theo workload.
14. Đặc tả report “độc giả đang mượn” và “lượt mượn tháng này”: kỳ đo, điều kiện, nhóm, mẫu số và quyền xem.

## Lời giải

1. `DauSach(book_id, title, ...)`, `BanSao(copy_id, book_id, status, ...)`, `DocGia(reader_id, ...)`, `LuotMuon(loan_id, reader_id, copy_id, borrowed_on, returned_on)`. loan_id định danh mỗi sự kiện. Tựa/tác giả thuộc đầu sách; mã vạch/tình trạng vật lý thuộc bản sao. Tác giả M:N cần bảng liên kết nếu yêu cầu nhiều tác giả.
2. A+ = ABCD, A là khóa duy nhất vì A không nằm vế phải nên mọi khóa cần A, và A tự đủ. B→C vi phạm 3NF vì B không superkey, C không prime. Tách R1(B,C), R2(A,B,D). Giao B xác định R1 nên nối không mất mát; phụ thuộc được giữ trong hai bảng.
3. Kết quả lab: `(1, 'An', 2)`, `(2, 'Binh', 2)`.

```sql
SELECT r.reader_id, r.name, COUNT(*) AS total
FROM readers r JOIN loans l ON l.reader_id = r.reader_id
GROUP BY r.reader_id, r.name
HAVING COUNT(*) >= 2
ORDER BY r.reader_id;
```

4. An 2, Binh 2, Chi 1, Dung 0. Phải COUNT khóa bên phải:

```sql
SELECT r.reader_id, r.name, COUNT(l.loan_id) AS total
FROM readers r LEFT JOIN loans l ON l.reader_id = r.reader_id
GROUP BY r.reader_id, r.name ORDER BY r.reader_id;
```

5. Sách B04:

```sql
SELECT b.book_id, b.title FROM books b
WHERE NOT EXISTS (SELECT 1 FROM loans l WHERE l.book_id = b.book_id)
ORDER BY b.book_id;
```

6. Các loan_id 2, 3, 5:

```sql
SELECT l.loan_id, r.name, b.title
FROM loans l JOIN readers r ON r.reader_id = l.reader_id
JOIN books b ON b.book_id = l.book_id
WHERE l.returned_on IS NULL ORDER BY l.loan_id;
```

7. So sánh với NULL cho UNKNOWN; dùng `IS NULL`. Muốn khác NULL dùng `IS NOT NULL`.
8. `x NOT IN (1,NULL)` tương đương x<>1 AND x<>NULL; với x khác 1 phần sau UNKNOWN nên WHERE không giữ. Dùng NOT EXISTS với điều kiện tương quan rõ ràng; nếu x cũng NULL phải xác định quy tắc nghiệp vụ mong muốn.
9. TenSV phụ thuộc MaSV, TenMH phụ thuộc MaMH, mỗi phần của khóa ghép. Tách `SinhVien(MaSV,TenSV)`, `MonHoc(MaMH,TenMH)`, `DangKy(MaSV,MaMH,Diem)`; thêm PK/FK tương ứng.
10. XPath `/library/book[@id='B01']/title`; XQuery xem ghi chú phần XML. Với mẫu 2 sách kết quả là `He dieu hanh`.
11. BEGIN, kiểm tra/quản lý đồng thời số dư, trừ có điều kiện số dư≥100, kiểm tra đúng một hàng đã cập nhật, cộng vào tài khoản đích hợp lệ, COMMIT. Bất kỳ lỗi nào ROLLBACK cả hai. Số dư nên dùng số nguyên đơn vị nhỏ hoặc decimal phù hợp, không float cho tiền. Isolation/lock cụ thể theo DBMS.
12. Cả hai cùng đọc trạng thái cũ trước khi một bên ghi. Đặt unique theo sách với điều kiện returned_on IS NULL nếu DBMS hỗ trợ, hoặc cơ chế lock/ràng buộc tương đương trong transaction. Trigger lab minh họa SQLite; kiểm tra thao tác từ nhiều phiên trong hệ thực.
13. Sổ ngân hàng thường hợp quan hệ và ràng buộc/giao dịch rõ; catalog có thể hợp document nếu truy vấn theo tài liệu; graph hợp duyệt đường quan hệ. Đây không là quy tắc cứng; khả năng hệ quản trị, truy vấn chéo và kỹ năng vận hành có thể làm lựa chọn thay đổi.
14. Report đang mượn dùng snapshot tại thời điểm T với loan chưa trả tại T; lịch sử cần cả borrowed_on≤T và returned_on>T hoặc NULL. Lượt tháng dùng khoảng `[đầu tháng, đầu tháng sau)` trên borrowed_on, có thể tính cả đã trả. Nêu quyền xem dữ liệu từng người, cách xử lý múi giờ và duplicate.
