# Bài tập tự luyện IT004

> [!IMPORTANT]
> **Trình tự làm bài:** phác ERD → ghi PK/FK → viết SQL → thử dữ liệu biên/NULL → giải thích kết quả. Đừng xem checklist/đáp án trước khi tự làm.

Hãy tự giải trước, ghi rõ giả định nghiệp vụ và cách kiểm tra kết quả. Bộ bài này được viết lại theo các dạng chủ đề trong học liệu lớp cũ.

1. **ERD:** thiết kế quản lý sinh viên, môn học, lớp mở và đăng ký. Một sinh viên đăng ký nhiều lớp; một lớp có nhiều sinh viên; mỗi đăng ký lưu điểm và ngày đăng ký. Xác định lực lượng, khóa và thực thể kết hợp.
2. **Chuyển mô hình:** chuyển ERD trên thành bảng, PK/FK, ràng buộc NULL và miền điểm. Giải thích vì sao không đặt danh sách môn vào một cột sinh viên.
3. **Đại số quan hệ:** biểu diễn sinh viên đăng ký một môn cụ thể; sinh viên chưa đăng ký môn nào; sinh viên đăng ký mọi môn bắt buộc. Nêu phép chia cho câu hỏi “mọi”.
4. **SQL:** viết truy vấn danh sách lớp có số người đăng ký lớn hơn ngưỡng; điểm trung bình theo môn; sinh viên chưa có đăng ký; sinh viên có điểm cao nhất trong từng môn. Chú ý đồng hạng và NULL.
5. **Phụ thuộc hàm:** với `R(MaSV, MaMH, TenSV, TenMH, HocKy, Diem)` và các phụ thuộc nghiệp vụ tự nêu rõ, tìm khóa ứng viên, chỉ ra dư thừa rồi phân rã đến 3NF; kiểm tra nối không mất mát.
6. **SQL Server:** tạo bảng `SinhVien`, `MonHoc`, `DangKy`; nhập dữ liệu mẫu; kiểm thử PK/FK/CHECK; viết một trigger audit cho nhiều hàng và giải thích vì sao constraint thích hợp hơn cho miền điểm.

## Checklist đáp án

- ERD có bảng kết hợp cho liên kết N–N; thuộc tính điểm nằm trên đăng ký.
- Các phép nối dùng đủ cặp PK/FK; phép tìm chưa có dùng `NOT EXISTS` hoặc LEFT JOIN rồi kiểm tra NULL.
- Truy vấn nhóm phân biệt `WHERE` (lọc hàng) và `HAVING` (lọc nhóm); xử lý trường hợp môn chưa có đăng ký nếu cần hiện cả môn đó.
- Khóa ứng viên được chứng minh bằng bao đóng và tính tối thiểu, không chỉ đoán từ tên cột.
- Phân rã ghi rõ các bảng, phép nối lại và phụ thuộc còn kiểm tra được cục bộ.
- Trigger xử lý tập hợp nhiều hàng trong `inserted`/`deleted`, không giả định mỗi lệnh chỉ cập nhật một hàng.

## Đáp án ngắn cho câu trọng tâm

Với `SinhVien` — `DangKy` — `MonHoc`, truy vấn sinh viên chưa đăng ký có thể dùng:

```sql
SELECT sv.MaSV, sv.HoTen
FROM SinhVien AS sv
WHERE NOT EXISTS (
  SELECT 1 FROM DangKy AS dk WHERE dk.MaSV = sv.MaSV
);
```

`NOT EXISTS` tránh bẫy `NOT IN` khi tập con có NULL. Bài còn lại phụ thuộc chính xác vào giả định nghiệp vụ và tập phụ thuộc hàm mà bạn khai báo.
