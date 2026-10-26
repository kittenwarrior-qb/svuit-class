# Kho học tập 6 môn CNTT — lớp G12.LT.CNTT

Tài liệu tự học tiếng Việt cho **IE005, IE101, IE103, IT004, IT007, MA003**. Mỗi môn có kiến thức, ví dụ giải thích, bài tập kèm đáp án, thực hành và danh mục nguồn. Cập nhật: **24/10/2026**.

Đây là bản tổng hợp nền tảng để học chủ động, **chưa phải toàn bộ học liệu chính thức của lớp**. Chưa có đủ slide, rubric và đề cương riêng của giảng viên; các ảnh đề hiện có là đề cũ/đề luyện tập và không xác nhận là đề của lớp G12. Không suy ra cấu trúc thi hoặc tỉ lệ điểm từ lớp khác. Phạm vi mở rộng được đánh dấu trong từng môn.

**Lưu ý chương trình:** [Chương trình liên thông từ xa K21/2026](CHUONG-TRINH-K21-2026.md) trên portal có kế hoạch mẫu khác với ảnh 5 môn bạn gửi: ảnh có IE101, trong khi kế hoạch K21 liệt kê IE109; MA003 nằm HK2 theo kế hoạch mẫu. Trang TKB cá nhân hiện chưa tải được dữ liệu (HTTP 400), vì vậy cần xác nhận kế hoạch áp dụng cho bạn với đơn vị đào tạo.

## Mở từng môn

| Thứ | Môn / folder | Mã lớp | TC | Số buổi | Từ ngày → đến ngày dự kiến |
|---|---|---|---:|---:|---|
| 2 | [IE101 — Cơ sở hạ tầng CNTT](IE101-co-so-ha-tang-cntt/README.md) | IE101.G12.LT.CNTT | 3 | 8 | 26/10 → 14/12 |
| 3 | [IE005 — Giới thiệu ngành CNTT](IE005-gioi-thieu-nganh-cntt/README.md) | IE005.G12.LT.CNTT | 1 | 4 | 27/10 → 17/11 |
| 4 | [IE103 — Quản lý thông tin](IE103-quan-ly-thong-tin/README.md) | IE103.G12.LT.CNTT | 4 | 10 | 28/10 → 30/12 |
| 5 | [IT007 — Hệ điều hành](IT007-he-dieu-hanh/README.md) | IT007.G12.LT.CNTT | 4 | 10 | 29/10 → 31/12 |
| 6 | [MA003 — Đại số tuyến tính](MA003-dai-so-tuyen-tinh/README.md) | MA003.G12.LT.CNTT | 3 | 8 | 30/10 → 18/12 |

## Môn thứ sáu trong kho

[IT004 — Cơ sở dữ liệu](IT004-co-so-du-lieu/README.md) là môn thứ sáu bạn yêu cầu tổng hợp. Môn này không xuất hiện trong ảnh thời khóa biểu 5 môn đã gửi, nên mình giữ riêng ngoài bảng lịch và không tự đoán ngày học.

## Ảnh đề thi hiện có

Hiện repo không còn lưu ảnh trang đề; các bộ đề đã được phân loại dưới dạng PDF cho MA003, IT004 và IT007. IT007 hiện có [13 PDF đã phân loại theo kỳ/năm học](IT007-he-dieu-hanh/de-thi/README.md), MA003 có [15 PDF](MA003-dai-so-tuyen-tinh/de-thi/README.md). IE005, IE101 và IE103 hiện chưa có ảnh đề trong kho.

Lịch trên được chép từ ảnh người học cung cấp, **ảnh không ghi năm**. Không tự gán năm 2026 cho lịch này; xác nhận lịch hiện hành trên LMS. Tổng cộng 15 tín chỉ, 40 buổi theo ảnh.

## Học theo cách nào?

1. Đọc `README.md` của môn để biết mục tiêu và lộ trình tự học đề xuất.
2. Học `01-kien-thuc.md`, tự làm `02-bai-tap.md` trước khi mở đáp án cuối tệp.
3. Làm lab trong `thuc-hanh/`, lưu kết quả và giải thích bằng lời của mình.
4. Dùng `03-on-tap.md` để nhớ công thức, lỗi thường gặp và tự kiểm tra.
5. Đọc sâu qua `04-tai-lieu.md`; nguồn bên ngoài được liên kết, không sao chép nguyên sách.

## Tài liệu dùng chung

- [Kế hoạch học và theo dõi tiến độ](KE-HOACH-HOC.md)
- [Lộ trình ưu tiên môn dễ vào trước và cách phân bổ thời gian](LO-TRINH-UU-TIEN.md)
- [Chương trình đào tạo liên thông CNTT từ xa K21/2026](CHUONG-TRINH-K21-2026.md)
- [Phạm vi đã đối chiếu, phần còn thiếu](PHAM-VI-VA-NGUON.md)
- [Cách thêm tài liệu và quản lý Git](HUONG-DAN-DONG-GOP.md)
- [Quyền sử dụng và nguồn gốc](NGUON-GOC.md)
- [Kết quả kiểm tra và giới hạn](KIEM-TRA.md)

## Chạy các lab có sẵn

Cần Python 3.8 trở lên; các lab Python dùng thư viện chuẩn, không cần cài gói ngoài. Mở terminal tại folder chứa README này:

```console
python IE101-co-so-ha-tang-cntt/thuc-hanh/subnet.py
python IE103-quan-ly-thong-tin/thuc-hanh/lab_sql.py
python IT007-he-dieu-hanh/thuc-hanh/mo_phong.py
python MA003-dai-so-tuyen-tinh/thuc-hanh/gauss.py
python scripts/kiem_tra.py
```

Các bài Bash/C tùy chọn cần Linux hoặc WSL và công cụ tương ứng; xem hướng dẫn trong môn. Không dùng số liệu sinh viên thật trong bài thực hành công khai.
