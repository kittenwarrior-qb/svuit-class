# Thực hành SQL Server

Các ví dụ dùng cú pháp T-SQL; kiểm tra phiên bản SQL Server đang dùng. Chạy trên CSDL luyện tập, không dùng dữ liệu thật.

## Tạo bảng có khóa và ràng buộc

```sql
CREATE TABLE SinhVien (
  MaSV varchar(12) NOT NULL PRIMARY KEY,
  HoTen nvarchar(100) NOT NULL,
  Email varchar(254) NULL UNIQUE
);
CREATE TABLE MonHoc (
  MaMH varchar(10) NOT NULL PRIMARY KEY,
  TenMH nvarchar(100) NOT NULL,
  SoTinChi tinyint NOT NULL CHECK (SoTinChi BETWEEN 1 AND 10)
);
CREATE TABLE DangKy (
  MaSV varchar(12) NOT NULL REFERENCES SinhVien(MaSV),
  MaMH varchar(10) NOT NULL REFERENCES MonHoc(MaMH),
  HocKy tinyint NOT NULL,
  Diem decimal(4,2) NULL CHECK (Diem BETWEEN 0 AND 10),
  CONSTRAINT PK_DangKy PRIMARY KEY (MaSV, MaMH, HocKy)
);
```

Chọn `nvarchar` cho văn bản Unicode; xác định NULL/NOT NULL từ nghiệp vụ. Khóa chính ghép ngăn đăng ký trùng trong cùng học kỳ.

## Truy vấn, nối, nhóm

```sql
SELECT sv.MaSV, sv.HoTen, mh.TenMH, dk.Diem
FROM SinhVien AS sv
JOIN DangKy AS dk ON dk.MaSV = sv.MaSV
JOIN MonHoc AS mh ON mh.MaMH = dk.MaMH
WHERE dk.HocKy = 1
ORDER BY sv.HoTen, mh.TenMH;

SELECT MaMH, COUNT(*) AS SoLuotDangKy, AVG(Diem) AS DiemTB
FROM DangKy
GROUP BY MaMH
HAVING COUNT(*) >= 2;
```

Làm thêm LEFT JOIN để tìm sinh viên chưa đăng ký: nối trái với `DangKy`, lọc `dk.MaSV IS NULL`. Tìm sinh viên học tất cả môn bằng cách đếm số môn phân biệt đã học và so với tổng số môn (xử lý riêng trường hợp danh sách môn rỗng); đối chiếu với phép chia quan hệ.

## Cập nhật an toàn và giao dịch

Trước `UPDATE`/`DELETE`, chạy cùng `WHERE` dưới dạng `SELECT` để xem chính xác các hàng bị ảnh hưởng. Dùng giao dịch thử nghiệm và rollback khi chưa muốn lưu:

```sql
BEGIN TRANSACTION;
UPDATE DangKy SET Diem = 8.50
WHERE MaSV = 'SV001' AND MaMH = 'DB01' AND HocKy = 1;
SELECT * FROM DangKy
WHERE MaSV = 'SV001' AND MaMH = 'DB01' AND HocKy = 1;
ROLLBACK; -- đổi thành COMMIT chỉ khi đã xác nhận kết quả
```

Thực hành tiếp: tạo dữ liệu mẫu; thử vi phạm PK/FK/CHECK; thêm index cho cột thường dùng trong điều kiện nối/lọc; viết view; so sánh EXISTS với IN; tạo trigger ghi lịch sử và thử cả cập nhật nhiều hàng. Xem source scripts trong `tai-lieu-lop/` ở máy cá nhân; không đẩy các tệp gốc lên GitHub.
