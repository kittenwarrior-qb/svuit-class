# IE103 — Kiến thức quản lý thông tin

> [!TIP]
> **Nhớ nhanh:** **nghiệp vụ → ERD → bảng/khóa → chuẩn hóa → SQL → giao dịch/bảo vệ**. M:N cần bảng liên kết. Truy vấn phải kiểm tra JOIN có nhân hàng không, NULL có làm đổi kết quả không, và nhóm/lọc đang đặt đúng chỗ chưa.

### 5 ý cốt lõi

- Mô hình dữ liệu phản ánh quy tắc nghiệp vụ, không chỉ dữ liệu mẫu.
- M:N chuyển thành bảng liên kết; PK định danh, FK giữ tham chiếu.
- Dùng phụ thuộc hàm/khóa để phân tích chuẩn hóa.
- SQL cần kiểm tra JOIN, NULL, `WHERE/HAVING` và mức hạt kết quả.
- Transaction bảo vệ tính nhất quán; backup dùng cho phục hồi.

<details><summary>Mở phần giải thích và ví dụ</summary>

## 1. Vòng đời và chất lượng thông tin

Vòng đời: thu thập → xác thực/làm sạch → mô hình hóa → lưu trữ → xử lý/truy vấn → trình bày/chia sẻ → lưu trữ dài hạn/hủy theo chính sách. Cần biết chủ sở hữu, nguồn, quyền truy cập và mục đích của dữ liệu.

Chất lượng gồm độ đúng, đầy đủ, nhất quán, kịp thời, hợp lệ và không trùng lặp theo quy tắc. Ví dụ `ngay_tra < ngay_muon` có thể sai quy tắc thời gian; hai người cùng tên không đủ kết luận là trùng. Metadata gồm định nghĩa trường, đơn vị, kiểu, nguồn và thời điểm. Từ điển dữ liệu giảm hiểu khác nhau giữa nhóm.

## 2. Mô hình khái niệm → logic → vật lý

Mức khái niệm mô tả thực thể/quan hệ theo nghiệp vụ. Mức logic mô tả bảng, thuộc tính và ràng buộc độc lập tương đối với thiết bị. Mức vật lý chọn kiểu cụ thể, index, phân vùng và cách lưu.

Ví dụ thư viện: `DocGia`, `Sach`, `LuotMuon`. Một độc giả có nhiều lượt mượn; một sách có nhiều lượt mượn theo thời gian. Nếu mỗi đầu sách có nhiều bản vật lý, cần `BanSao`, lượt mượn tham chiếu bản sao. Mô hình đơn giản của lab coi mỗi `Sach` là một bản vật lý và ghi rõ giả định.

ERD phải có khóa, cardinality (1:1, 1:N, M:N), tính bắt buộc/tùy chọn và ý nghĩa nghiệp vụ. Quan hệ M:N chuyển thành bảng liên kết; thuộc tính của lần liên kết nằm ở đó. Không nhét danh sách mã sách vào một ô chuỗi để thay quan hệ.

## 3. Mô hình quan hệ và ràng buộc

Quan hệ có tập thuộc tính và bộ. Thực thi SQL thường có duplicate nếu không `DISTINCT`, khác mô hình quan hệ thuần túy. Superkey xác định duy nhất một hàng; candidate key là superkey tối thiểu; primary key là khóa được chọn; foreign key tham chiếu khóa được phép của bảng khác.

Ràng buộc thực thể: PK duy nhất và không NULL. Tham chiếu: FK phải có đối tượng đích hoặc NULL nếu cho phép. Miền: kiểu, CHECK, NOT NULL. Quy tắc nghiệp vụ: một bản sách chỉ có tối đa một lượt mượn đang mở; không phải quy tắc nào cũng diễn đạt bằng CHECK đơn giản.

Đại số quan hệ: selection chọn hàng; projection chọn cột; join ghép theo điều kiện; union hợp hai quan hệ tương thích; difference lấy phần khác; division diễn đạt “mọi”. Trong SQL, “độc giả mượn mọi sách trong tập X” thường dùng `NOT EXISTS` lồng để tìm người không có sách bắt buộc nào còn thiếu.

## 4. Phụ thuộc hàm và chuẩn hóa

X → Y nghĩa là hai hàng trùng X thì trùng Y trong mọi trạng thái hợp lệ theo nghiệp vụ. Một mẫu dữ liệu tình cờ duy nhất không đủ chứng minh phụ thuộc hàm. Bao đóng X+ là tập thuộc tính suy ra từ X bằng các phụ thuộc; X là superkey nếu X+ chứa mọi thuộc tính.

Ví dụ `DangKy(MaSV,MaMH,TenSV,TenMH,Diem)` có `(MaSV,MaMH) → Diem`, `MaSV → TenSV`, `MaMH → TenMH`. Khóa ghép `(MaSV,MaMH)`; tên phụ thuộc vào từng phần khóa gây lặp dữ liệu và bất thường thêm/sửa/xóa. Tách thành `SinhVien`, `MonHoc`, `DangKy` giúp biểu diễn đúng ba sự kiện.

1NF: giá trị thuộc miền nguyên tử theo mô hình, không nhóm lặp. 2NF: đạt 1NF và thuộc tính không khóa không phụ thuộc bộ phận của bất kỳ candidate key ghép nào. 3NF: với mỗi FD không tầm thường X → A, X là superkey hoặc A là thuộc tính prime (nằm trong một candidate key). BCNF: X phải là superkey cho mọi FD không tầm thường.

Phân rã cần nối không mất mát: ghép lại không sinh hàng giả/không mất thông tin. Với phân rã nhị phân R thành R1,R2, điều kiện đủ và cần theo FD là giao R1∩R2 xác định R1 hoặc R2 trong F+. Bảo toàn phụ thuộc giúp kiểm tra ràng buộc ở từng bảng. BCNF có thể không bảo toàn mọi FD; 3NF có thể giữ phụ thuộc. Không dùng khẩu hiệu “càng nhiều bảng càng tốt”.

## 5. SQL căn bản và cách suy nghĩ

Nhóm lệnh: DDL tạo cấu trúc; DML thay dữ liệu; SELECT truy vấn; quản lý giao dịch và quyền tùy DBMS. Thứ tự logic để hiểu SELECT đơn giản: FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → DISTINCT → ORDER BY → LIMIT/OFFSET (cú pháp cuối tùy hệ).

```sql
SELECT r.reader_id, r.name, COUNT(l.loan_id) AS total
FROM readers AS r
LEFT JOIN loans AS l ON l.reader_id = r.reader_id
GROUP BY r.reader_id, r.name
HAVING COUNT(l.loan_id) >= 2
ORDER BY total DESC, r.reader_id;
```

INNER JOIN giữ hàng khớp; LEFT JOIN giữ mọi hàng trái và gán NULL nếu không khớp. Đặt `WHERE l.returned_on IS NOT NULL` sau LEFT JOIN loại hàng không khớp; chuyển điều kiện vào ON nếu muốn giữ độc giả không có lượt tương ứng. `COUNT(*)` đếm hàng kết quả, `COUNT(l.loan_id)` chỉ đếm loan_id khác NULL.

NULL biểu diễn thiếu/không biết, không phải 0 hay chuỗi rỗng. Dùng `IS NULL`, không dùng `= NULL`. WHERE chỉ giữ TRUE, loại FALSE và UNKNOWN. `NOT IN` có NULL trong tập có thể cho UNKNOWN; `NOT EXISTS` thường rõ nghĩa hơn để biểu diễn “không có”.

Subquery có thể trả scalar, tập hoặc tồn tại; correlated subquery tham chiếu hàng ngoài. UNION loại trùng, UNION ALL giữ trùng. Không có ORDER BY thì không đảm bảo thứ tự kết quả. Không SELECT cột ngoài GROUP BY/aggregate theo thói quen riêng của một DBMS.

## 6. View, index và kế hoạch thực thi

View thường là truy vấn đặt tên, không nhất thiết lưu sẵn kết quả; materialized view có lưu và cần refresh tùy hệ. View giúp đóng gói logic và giới hạn cột/hàng khi kết hợp phân quyền phù hợp; không tự thay thế toàn bộ cơ chế bảo mật.

Index tăng tốc một số truy vấn đổi lấy dung lượng và chi phí ghi. Index ghép `(reader_id, borrowed_on)` thường hữu ích cho lọc reader rồi khoảng thời gian; hiệu quả cụ thể phụ thuộc bộ tối ưu và workload. Không mặc định tạo index cho mọi cột. Dùng EXPLAIN để quan sát, đo trên dữ liệu và tải đại diện; kết quả trên 5 hàng không đại diện hàng triệu hàng.

## 7. Giao dịch và đồng thời

ACID: Atomicity (tất cả hoặc không), Consistency (giữ các ràng buộc đã định nghĩa), Isolation (cách giao dịch đồng thời quan sát nhau), Durability (commit bền theo cơ chế/cấu hình DBMS). Consistency ở đây không đồng nhất với consistency trong hệ phân tán.

Ví dụ chuyển tiền: trừ A và cộng B cùng một transaction; lỗi phải rollback. Đồng thời có thể tạo lost update, dirty read, non-repeatable read, phantom theo isolation và DBMS. Tránh đọc-sửa-ghi ngoài transaction; dùng cập nhật nguyên tử, lock hoặc kiểm tra version theo thiết kế.

Optimistic concurrency phát hiện xung đột lúc ghi; pessimistic dùng khóa trước khi thay đổi. Deadlock có thể xảy ra khi hai giao dịch giữ/chờ khóa nhau; dùng thứ tự lấy khóa nhất quán, giao dịch ngắn và retry theo chính sách. Giao dịch không thay thế kiểm tra ràng buộc nghiệp vụ.

## 8. An toàn, import/export, backup

Xác thực trả lời “ai”; phân quyền trả lời “được làm gì”. Quyền tối thiểu, role theo nhiệm vụ, tài khoản dịch vụ riêng, audit, mã hóa và quản lý secret giảm rủi ro. SQL injection tránh bằng tham số hóa; escape chuỗi thủ công dễ sai. Với tên bảng/cột động thường cần whitelist, không thể thay mọi identifier bằng placeholder giá trị.

Backup khác export: dump logic tái tạo schema/data; backup vật lý và log có thể hỗ trợ phục hồi đến thời điểm tùy DBMS. Restore phải kiểm tra ràng buộc, số hàng, mẫu dữ liệu và truy vấn nghiệp vụ. Replica không thay backup nếu xóa nhầm cũng được sao chép.

Import CSV cần encoding, dấu phân cách, NULL, định dạng ngày, kiểu số và xử lý lỗi. Thử vào staging rồi kiểm tra trước khi nhập bảng chính; giữ nguồn và log chuyển đổi. Không ghi mật khẩu trong script/export.

## 9. Lập trình CSDL

Function trả giá trị hoặc bảng tùy hệ; procedure đóng gói thao tác và được gọi theo cú pháp hệ quản trị. Trigger tự chạy khi sự kiện dữ liệu xảy ra; có thể kiểm tra/lưu audit nhưng dễ tạo hành vi ẩn, đệ quy và chi phí không rõ. Cursor duyệt từng hàng; ưu tiên xử lý theo tập khi phù hợp, không khẳng định cursor luôn sai.

Ví dụ trigger SQLite của lab chặn lượt mượn đang mở thứ hai cho cùng sách. Đây là bài minh họa ràng buộc trong SQLite; PostgreSQL có thể dùng partial unique index, SQL Server có filtered index. Không chép cú pháp một hệ vào hệ khác mà không kiểm tra.

Khi thiết kế procedure ghi dữ liệu: xác định input/output, ràng buộc, transaction, xử lý lỗi và quyền chạy. Không đặt mọi nghiệp vụ vào trigger chỉ để giảm mã ứng dụng. Bản SQLite không hỗ trợ stored procedure phía server theo mô hình PostgreSQL/SQL Server.

## 10. XML, XPath, XQuery

XML biểu diễn cây với element, attribute và text; phải well-formed, một root, thẻ đóng đúng, thuộc tính có dấu nháy. Schema/DTD dùng để kiểm tra cấu trúc/kiểu khi cần; well-formed khác valid theo schema. Namespace tránh trùng tên nhưng ảnh hưởng truy vấn.

```xml
<library>
  <book id="B01"><title>He dieu hanh</title><year>2022</year></book>
  <book id="B02"><title>Co so du lieu</title><year>2020</year></book>
</library>
```

XPath `/library/book[@id='B01']/title` chọn title của B01; `/library/book[year > 2021]/title` lọc theo năm; `//book` tìm book ở các mức hậu duệ. `@` chọn thuộc tính, predicate trong `[]`, vị trí XPath bắt đầu từ 1. Thư viện ElementTree Python chỉ hỗ trợ một tập con XPath, không chạy mọi biểu thức XPath 3.1.

XQuery có thể biến đổi kết quả thành cấu trúc mới. Ví dụ FLWOR (để đọc hiểu, cần bộ xử lý XQuery):

```xquery
for $b in doc("library.xml")/library/book
where xs:integer($b/year) > 2021
order by string($b/title)
return <result>{ $b/title/text() }</result>
```

XPath chủ yếu là biểu thức chọn/tính trên dữ liệu; XQuery bổ sung ngôn ngữ truy vấn và dựng kết quả rộng hơn. Không xử lý XML từ nguồn không tin cậy bằng cấu hình cho phép external entity tùy tiện; lab chỉ dùng file tự soạn.

## 11. Menu, form, report

Menu tổ chức tác vụ theo vai trò; form thu thập/chỉnh sửa với validation; report tổng hợp dữ liệu cho quyết định. Validation ở giao diện giúp trải nghiệm, ở server/CSDL giữ quy tắc khi bỏ qua giao diện. Form tốt có nhãn, phản hồi lỗi rõ và tránh mất dữ liệu người dùng nhập.

Report phải nêu đơn vị, kỳ đo, bộ lọc, thời điểm cập nhật và định nghĩa chỉ tiêu. “Sách đang mượn” là snapshot theo thời điểm; “số lượt mượn trong tháng” là dòng sự kiện theo khoảng ngày; hai phép đếm khác nhau. Join thêm bảng nhiều dòng có thể nhân đôi doanh số/số lượt nếu không kiểm soát mức hạt dữ liệu.

## 12. Mô hình CSDL tiên tiến

CSDL hướng đối tượng gắn object identity, class, quan hệ đối tượng và persistence; khác ORM (lớp ánh xạ object vào CSDL quan hệ). Quan hệ biểu diễn bằng bảng/khóa, object tham chiếu nhau bằng định danh đối tượng; chuyển đổi cần quyết định cách biểu diễn kế thừa, collection và identity.

CSDL phân tán đặt dữ liệu trên nhiều nút. Phân mảnh ngang chia hàng; dọc chia cột và cần khóa để ghép; replication tạo bản sao. Cần cân nhắc định tuyến truy vấn, transaction, đồng bộ, mất mạng và khôi phục. CAP nói về lựa chọn giữa consistency theo nghĩa linearizability và availability theo định nghĩa mô hình khi có network partition; không đơn giản là “mọi lúc chọn hai trong ba”.

NoSQL: key-value cho tra cứu theo khóa; document cho tài liệu lồng; wide-column cho các mẫu truy cập phù hợp; graph cho quan hệ và duyệt đồ thị. “Schema linh hoạt” vẫn cần quy ước và validation. Một hệ có thể hỗ trợ nhiều mô hình và transaction; không nói mọi NoSQL đều không có ACID/JOIN.

Chọn mô hình từ truy vấn, quy tắc nhất quán, tải, tăng trưởng và chi phí vận hành. Dữ liệu nghiệp vụ cần giao dịch quan hệ có thể kết hợp object storage cho file và search index cho tìm kiếm; phải chỉ rõ nguồn sự thật và cách đồng bộ.

</details>
