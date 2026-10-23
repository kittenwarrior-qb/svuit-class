# IE005 — Câu hỏi và tình huống

## Đề bài

1. Phân biệt dữ liệu và thông tin bằng ví dụ từ điểm danh lớp; cần metadata nào để hiểu đúng?
2. Vẽ hệ thống bán vé: người dùng, quy trình, phần mềm, hạ tầng, dữ liệu và hai tình huống lỗi.
3. So sánh developer, data analyst, system engineer: đầu ra, nền tảng và một bài nhỏ chứng minh năng lực.
4. Biến “website phải dễ dùng và nhanh” thành 2 tiêu chí có thể đánh giá.
5. Bạn thấy CSV có thông tin sinh viên trong repo công khai. Nêu hành động xử lý phù hợp và cách tránh tái diễn.
6. AI trả lời rằng một câu SQL đúng nhưng dữ liệu thử cho kết quả sai. Cần xử lý thế nào?
7. Thành viên nhóm trễ việc khiến tích hợp trễ. Viết một phản hồi cụ thể và kế hoạch điều chỉnh.
8. Lập kế hoạch 8 tuần phù hợp một hướng nghề, có sản phẩm, lịch và tiêu chí tự đánh giá.

## Gợi ý đáp án

1. Dữ liệu: các mã sinh viên và giá trị có/vắng. Thông tin: tỉ lệ tham dự của một lớp trong khoảng thời gian xác định. Cần mã lớp, ngày, định nghĩa có mặt, cách xử lý đi muộn và số người làm mẫu số.
2. Bao gồm tìm vé → giữ chỗ → thanh toán → xuất vé; bảng suất diễn/chỗ/đơn; web/app/CSDL/mạng. Lỗi thanh toán thành công nhưng chưa xuất vé cần cơ chế đối soát/idempotency; hai người cùng chọn ghế cần kiểm soát giao dịch và ràng buộc.
3. Developer: tính năng có kiểm thử và hướng dẫn chạy. Analyst: truy vấn, bảng/biểu đồ và kết luận có giới hạn. System engineer: cấu hình, monitoring và runbook phục hồi. Cả ba cần hiểu dữ liệu, giao tiếp và bảo mật; khác nhau ở trọng tâm đầu ra.
4. Ví dụ hiệu năng: p95 tìm kiếm dưới 2 giây với tải/bộ dữ liệu xác định. Usability: ít nhất 8/10 người thuộc nhóm mục tiêu hoàn thành thao tác đặt vé mà không cần trợ giúp trong bài thử đã thiết kế. Cần xác nhận mục tiêu với người dùng.
5. Hạn chế chia sẻ thêm, báo người quản lý repo qua kênh được phép; thay bằng dữ liệu giả, kiểm tra lịch sử và bản sao liên quan theo quy trình. Xóa file ở commit mới không tự xóa lịch sử. Không tự phát tán link để “cảnh báo”.
6. Tạo bộ dữ liệu tối thiểu phản ví dụ; kiểm tra JOIN/NULL/nhóm và kỳ vọng; đối chiếu tài liệu DBMS; sửa truy vấn và giữ ví dụ làm kiểm tra hồi quy. Chịu trách nhiệm với bài nộp của mình.
7. “Phần API chưa có trước ngày tích hợp nên nhóm chưa chạy được luồng chính. Mình cần bản tối thiểu gồm hai endpoint trước mốc đã thống nhất; phần còn lại tách issue và cùng rà lại trở ngại.” Trao đổi nguyên nhân trước khi quy lỗi cá nhân.
8. Ví dụ 1–2 nền Git/Python; 3–4 SQL và mô hình dữ liệu; 5–6 tính năng nhỏ; 7 kiểm thử; 8 hoàn thiện tài liệu/demo. Mỗi tuần có commit và một đầu ra chạy được. Đây là mẫu điều chỉnh theo thời gian thực, không phải yêu cầu môn.

Tự chấm mỗi câu 0–2: 0 = chỉ có khẩu hiệu; 1 = đúng ý nhưng thiếu ví dụ/bằng chứng; 2 = lập luận rõ, có ví dụ và giới hạn. Rubric này phục vụ tự học, không thay thế rubric giảng viên.
