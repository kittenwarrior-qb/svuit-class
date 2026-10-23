# IT004 — Kiến thức cơ sở dữ liệu

Ghi chú được biên soạn lại theo đề cương IT004 và các bài giảng/bài tập trong folder Drive. Đây là tài liệu ôn tập, không thay thế giáo trình hay nội dung lớp hiện hành.

## 1. Cơ sở dữ liệu và DBMS

Cơ sở dữ liệu (CSDL) là tập dữ liệu có tổ chức, được lưu bền vững và chia sẻ. Hệ quản trị CSDL (DBMS) cung cấp định nghĩa, truy vấn, cập nhật, kiểm soát truy cập, ràng buộc toàn vẹn, giao dịch và phục hồi. Phân biệt lược đồ (schema: cấu trúc tương đối ổn định) với trạng thái/instance (dữ liệu tại một thời điểm). Tính độc lập dữ liệu giúp thay đổi biểu diễn lưu trữ mà giảm ảnh hưởng chương trình.

## 2. Mô hình ER và thiết kế khái niệm

Thực thể biểu diễn một loại đối tượng; thuộc tính mô tả thực thể; khóa định danh từng thể hiện. Liên kết biểu diễn quan hệ giữa các thực thể. Khi thiết kế ER, xác định lực lượng (1–1, 1–N, N–N), tham gia bắt buộc/tùy chọn, thuộc tính đa trị/dẫn xuất và thực thể yếu. Ví dụ `SINHVIEN` đăng ký `MONHOC`: nếu cần lưu học kỳ, năm học, điểm thì các thuộc tính này thuộc liên kết `DANGKY`, không thuộc riêng sinh viên hay môn.

### Chuyển ER sang quan hệ

- Thực thể mạnh → bảng; khóa định danh → khóa chính.
- Liên kết 1–N → khóa ngoại đặt phía N; thuộc tính liên kết có thể đặt cùng bảng phía N.
- Liên kết N–N → bảng kết hợp, thường có khóa ghép từ hai khóa ngoại; thêm thuộc tính của liên kết.
- Thuộc tính đa trị → bảng riêng gồm khóa chủ thể và giá trị.
- Thực thể yếu → bảng có khóa gồm khóa chủ sở hữu và khóa bộ phận.

## 3. Mô hình quan hệ và toàn vẹn

Quan hệ là bảng khái niệm gồm bộ (tuple) và thuộc tính (attribute). Khóa siêu khóa định danh duy nhất; khóa ứng viên là siêu khóa tối thiểu; chọn một khóa làm khóa chính. Khóa ngoại tham chiếu khóa của quan hệ khác. Ràng buộc miền giới hạn kiểu/giá trị; ràng buộc thực thể yêu cầu khóa chính duy nhất và không NULL; toàn vẹn tham chiếu yêu cầu khóa ngoại khớp bản ghi đích hoặc NULL nếu được phép.

## 4. Đại số quan hệ và phép tính quan hệ

Các phép cốt lõi: chọn `σ` lọc hàng; chiếu `π` chọn cột (và loại trùng theo ngữ nghĩa quan hệ); tích Descartes ghép mọi cặp bộ; nối kết hợp hàng theo điều kiện; hợp, giao, hiệu yêu cầu hai quan hệ tương thích; đổi tên hỗ trợ truy vấn. Phép chia hữu ích cho câu hỏi “mọi”: sinh viên đã học tất cả môn bắt buộc.

Phép tính quan hệ mô tả điều kiện để một bộ được chọn thay vì nêu chuỗi thao tác. Phân biệt biến bộ và biến miền; biểu thức cần an toàn (miền kết quả bị giới hạn bởi dữ liệu đầu vào), tránh định nghĩa kết quả vô hạn.

## 5. SQL

Nhóm lệnh thường gặp: DDL (`CREATE`, `ALTER`, `DROP`), DML (`INSERT`, `UPDATE`, `DELETE`), truy vấn (`SELECT`), điều khiển giao dịch (`BEGIN TRANSACTION`, `COMMIT`, `ROLLBACK`) và quyền (`GRANT`, `REVOKE`). Cấu trúc truy vấn: `SELECT ... FROM ... WHERE ... GROUP BY ... HAVING ... ORDER BY ...`. `WHERE` lọc hàng trước nhóm; `HAVING` lọc nhóm sau tổng hợp. `NULL` biểu thị thiếu/không biết, phải kiểm tra bằng `IS NULL`; so sánh với NULL cho kết quả unknown. Cẩn trọng với `NOT IN` khi tập con chứa NULL; cân nhắc `NOT EXISTS`.

Nối trong: chỉ lấy hàng khớp; nối trái giữ tất cả hàng trái và điền NULL phía phải khi không khớp. Điều kiện nối thiếu có thể tạo tích Descartes. Truy vấn con có thể vô hướng, nhiều hàng hoặc tương quan. Hàm tổng hợp thường dùng: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`; `COUNT(*)` đếm hàng còn `COUNT(cột)` bỏ qua NULL.

## 6. Phụ thuộc hàm và chuẩn hóa

Phụ thuộc hàm `X → Y` nghĩa là hai hàng trùng X phải trùng Y. Bao đóng `X+` tìm các thuộc tính suy ra được theo tập phụ thuộc; dùng để kiểm tra siêu khóa và khóa ứng viên. Bao phủ tối thiểu thường tách vế phải về đơn thuộc tính, bỏ thuộc tính thừa ở vế trái và bỏ phụ thuộc dư thừa.

- 1NF: mỗi ô chứa giá trị nguyên tố theo miền đã chọn, không lặp nhóm.
- 2NF: đạt 1NF và mọi thuộc tính không khóa phụ thuộc đầy đủ vào mọi khóa ứng viên (không phụ thuộc bộ phận vào khóa ghép).
- 3NF: với mọi phụ thuộc không tầm thường `X → A`, X là siêu khóa hoặc A là thuộc tính khóa (prime).
- BCNF: với mọi phụ thuộc không tầm thường `X → Y`, X phải là siêu khóa.

Phân rã nhằm giảm dư thừa và bất thường thêm/sửa/xóa. Ưu tiên phân rã không mất mát; bảo toàn phụ thuộc giúp kiểm tra ràng buộc cục bộ. 3NF có thể bảo toàn phụ thuộc; phân rã BCNF đôi khi không.

## 7. Giao dịch và vận hành

ACID: nguyên tử, nhất quán, cô lập, bền vững. Mức cô lập điều tiết đọc bẩn, đọc không lặp và phantom; khóa và lịch tuần tự hóa góp phần giữ đúng dữ liệu nhưng ảnh hưởng đồng thời. Chỉ dùng giao dịch và cập nhật có điều kiện khi thử lệnh thay đổi dữ liệu. Trigger tự chạy khi sự kiện xảy ra, phù hợp một số ràng buộc/audit nhưng có thể gây tác dụng phụ khó thấy; ưu tiên constraint cho quy tắc đơn giản.

## 8. Tự kiểm tra trước khi nộp thiết kế

Mỗi bảng có khóa? Mỗi thuộc tính phụ thuộc đúng khóa? Liên kết N–N đã tách? FK và NULL có đúng ý nghĩa nghiệp vụ? Truy vấn có điều kiện nối đầy đủ? Trường hợp không có dữ liệu và NULL đã được kiểm tra? Phân rã có mất mát? Chạy lại script có thể tái tạo dữ liệu mẫu?

Nguồn phạm vi: đề cương và slide/bài tập IT004 trong folder Drive; sách tham khảo *Beginning SQL* của Wilton & Colby (2005). Xem [04-tai-lieu.md](04-tai-lieu.md) để biết giới hạn niên đại và quyền sử dụng.
