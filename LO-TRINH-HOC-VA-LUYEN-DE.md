# Lộ trình học, ôn và luyện đề

Tài liệu này giúp học theo nội dung trong repo rồi chuyển dần sang tự giải đề. Lịch và dạng thi chính thức phải lấy từ LMS, đề cương lớp G12 và thông báo giảng viên; đề cũ chỉ để luyện kỹ năng, không dự đoán đề sẽ thi.

## Bắt đầu ngay

1. Mở [README tổng](README.md), xác nhận môn nào đang học trong LMS. Ảnh thời khóa biểu hiện có 5 môn; IT004 là môn thứ sáu trong kho nhưng không xuất hiện trong ảnh.
2. Với từng môn, đọc `README.md`, sau đó học `01-kien-thuc.md`. Đánh dấu chủ đề đã học trên lớp và bỏ qua phần repo ghi là mở rộng/chưa xác nhận cho tới khi đối chiếu đề cương.
3. Làm `02-bai-tap.md` hoặc `03-bai-tap-on-tap.md` khi đóng phần đáp án. Chỗ sai ghi vào sổ lỗi: sai khái niệm, sai bước tính, hay sai do đọc đề.
4. Làm lab/báo cáo trong `thuc-hanh/` và ghi lại lệnh, kết quả, cách giải thích. Đây là bằng chứng hiểu bài, không chỉ là mã chạy được.
5. Mỗi cuối tuần dùng `03-on-tap.md`, rồi mở `05-de-thi-va-on-tap.md` để chọn đề/nguồn thuộc đúng chủ đề đã học.

## Thứ tự ưu tiên

- **IE005:** hoàn tất sớm vì lịch ảnh ghi 1 TC/4 buổi. Tóm tắt mỗi buổi thành 5–10 ý; ưu tiên bài thu hoạch, hoạt động lớp và yêu cầu LMS. Repo chưa có đề thi cũ xác thực.
- **IE103 và IT007:** duy trì đều mỗi tuần vì mỗi môn 4 TC/10 buổi theo ảnh. IE103 cần luyện mô hình dữ liệu/SQL; IT007 cần vừa làm bài thuật toán vừa chạy lab, tránh học dồn cuối kỳ.
- **MA003:** luyện ngắn hàng ngày sau khi học lý thuyết. Tự trình bày đầy đủ phép biến đổi, không chỉ ghi đáp số.
- **IE101:** theo lịch lớp nếu đúng mã môn; làm sơ đồ, bài tính mạng và báo cáo. Chưa có đề thi cũ xác thực trong repo.
- **IT004:** dùng làm nền cho SQL của IE103 nếu môn này có trong kế hoạch học hiện hành. Không tự đưa vào lịch thi khi chưa xác nhận với LMS.

Thứ tự này là cách chia thời gian để bắt nhịp, không phải đánh giá chính thức môn nào dễ hay khó. Xem [lộ trình ưu tiên và đối chiếu chương trình](LO-TRINH-UU-TIEN.md) vì ảnh thời khóa biểu và kế hoạch mẫu K21/2026 không hoàn toàn trùng nhau.

## Quy trình luyện một đề

### Khi còn đang học bài

1. Chọn một đề có chủ đề trùng phần đã học; ghi rõ môn, năm/học kỳ, kỳ thi, mã đề và nguồn.
2. Làm từng câu không xem đáp án/video. Ghi thời gian và độ tự tin cạnh mỗi câu.
3. So đáp án hoặc lời giải. Nếu không có đáp án đáng tin cậy, đánh dấu câu cần hỏi giảng viên thay vì tự coi đáp án mạng là chuẩn.
4. Viết lại lời giải sạch cho câu sai và ghi vì sao sai; làm lại câu đó sau 1 ngày và 1 tuần.

### Trước kỳ thi

1. Đọc phạm vi, hình thức, thời lượng và cách tính điểm từ giảng viên/LMS. Chỉ chọn đề cũ tương ứng với phạm vi đó.
2. Làm một đề trọn vẹn có bấm giờ, không tra cứu; tự chấm theo đáp án/tiêu chí đã xác minh.
3. Phân nhóm lỗi, ôn đúng phần yếu rồi làm một đề khác. Nếu kho không đủ đề, tạo bộ câu hỏi tự luyện từ `02-bai-tap.md` và bài tập lớp, không khẳng định đó là đề thật.
4. Ngày cuối chỉ ôn công thức, quy trình, lỗi đã ghi và chuẩn bị theo hướng dẫn lớp; không học một dạng chưa xác minh chỉ vì thấy trong đề cũ.

## Trọng tâm luyện theo môn

| Môn | Năng lực cần tự làm được | Nơi bắt đầu trong repo |
|---|---|---|
| IE005 | Trình bày định hướng ngành/nghề bằng ví dụ và lập luận của mình | [Bài tập](IE005-gioi-thieu-nganh-cntt/02-bai-tap.md) · [Ôn tập](IE005-gioi-thieu-nganh-cntt/03-on-tap.md) |
| IE101 | Giải thích kiến trúc; tính subnet/capacity; mô tả phương án vận hành | [Bài tập](IE101-co-so-ha-tang-cntt/02-bai-tap.md) · [Lab](IE101-co-so-ha-tang-cntt/thuc-hanh/README.md) |
| IE103 | Vẽ ERD, xác định khóa/chuẩn hóa, viết và giải thích SQL | [Bài tập](IE103-quan-ly-thong-tin/02-bai-tap.md) · [Lab SQL/XML](IE103-quan-ly-thong-tin/thuc-hanh/README.md) |
| IT004 | Mô hình dữ liệu và SQL trên DBMS được lớp yêu cầu | [Bài tập](IT004-co-so-du-lieu/03-bai-tap-on-tap.md) · [Bộ đề](IT004-co-so-du-lieu/de-thi/README.md) |
| IT007 | Vẽ Gantt, giải lập lịch/đồng bộ/deadlock/phân trang và giải thích cơ chế | [Bài tập](IT007-he-dieu-hanh/02-bai-tap.md) · [Bộ đề](IT007-he-dieu-hanh/de-thi/README.md) |
| MA003 | Giải hệ, biến đổi ma trận, định thức, cơ sở và ánh xạ theo phạm vi lớp | [Bài tập](MA003-dai-so-tuyen-tinh/02-bai-tap.md) · [Bộ đề](MA003-dai-so-tuyen-tinh/de-thi/README.md) |

## Nhịp học tối thiểu mỗi tuần

- Trước buổi học: 20–30 phút xem tiêu đề và ghi tối đa 3 câu hỏi.
- Trong 24 giờ sau buổi học: 45–60 phút tự viết lại ý chính, làm một bài không xem lời giải.
- Cuối tuần: mỗi môn đang học có ít nhất một lần tự kiểm tra; cập nhật sổ lỗi và lịch ôn lại sau 1 ngày/1 tuần/3 tuần.
- Khi có bài nộp hoặc kiểm tra gần: ưu tiên hạn của lớp trước, nhưng vẫn giữ một phiên ngắn cho MA003 và các môn nhiều tín chỉ.

## Giới hạn nguồn trong kho

Repo hiện có PDF đề được phân loại cho MA003, IT004 và IT007; IE005, IE101, IE103 chưa có đề thi cũ đáng tin cậy. Các trang Studocu/ video trong từng `05-de-thi-va-on-tap.md` là nguồn tham khảo cộng đồng, có thể giới hạn truy cập hoặc khác chương trình. Tài liệu lớp do giảng viên phát và thông báo LMS luôn được ưu tiên.
