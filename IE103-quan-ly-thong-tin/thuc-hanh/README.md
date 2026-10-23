# IE103 — Lab SQL, XML và thiết kế

## Chạy ngay

Từ gốc bộ học liệu:

```console
python IE103-quan-ly-thong-tin/thuc-hanh/lab_sql.py
```

Schema và queries nằm trong hai tệp `.sql`, dữ liệu XML trong `library.xml`. Script tạo SQLite trong RAM và kiểm tra các kết quả kỳ vọng; mỗi lần chạy là dữ liệu mới. Ngày 2025 trong dữ liệu là **dữ liệu giả của bài tập**, không là lịch học.

Giả định: mỗi hàng books là một bản sách vật lý; không mô hình nhiều tác giả/bản sao. Chuỗi ngày `YYYY-MM-DD` giúp so sánh từ điển khi input đã hợp lệ; CHECK hiện tại chưa kiểm tra đầy đủ định dạng/ngày tồn tại. Bài mở rộng: thêm validation và mô hình đầu sách/bản sao.

## Bài 1 — Truy vấn

Viết lại 4 query trước khi xem `queries.sql`; so với tập kết quả có ORDER BY. Thêm độc giả không mượn, một sách không mượn và trường hợp đã trả/chưa trả. Giải thích vì sao query vẫn đúng. Không sửa đáp án kỳ vọng để che truy vấn sai.

## Bài 2 — Ràng buộc, giao dịch

Thử insert FK không tồn tại; thêm lượt mượn thứ hai chưa trả cho B01; cập nhật lượt cũ thành chưa trả trong khi có lượt khác đang mở. Kỳ vọng đều bị từ chối. Đánh giá thêm trường hợp sách được trả rồi được mượn lại.

Lab rollback thay tên rồi hủy giao dịch; tên trở lại An. Thiết kế thêm nghiệp vụ chuyển tiền dùng số nguyên đơn vị nhỏ, kiểm tra tổng tiền trước/sau và mô phỏng lỗi giữa hai bước. SQLite không mô phỏng đầy đủ concurrency/isolation của SQL Server/PostgreSQL.

## Bài 3 — XML

Mở `library.xml`, viết XPath chọn B01 và đọc bằng ElementTree như script. Viết XQuery theo phần lý thuyết rồi chạy bằng bộ xử lý XQuery do lớp yêu cầu nếu có. ElementTree **không** là bộ xử lý XQuery hoặc toàn bộ XPath 3.1. Bài XQuery cần công cụ bổ sung và chưa được script kiểm tra tự động.

## Bài 4 — Function/procedure/cursor trên DBMS của lớp

Sau khi biết DBMS bắt buộc: tạo function đếm sách chưa trả của một độc giả; procedure trả sách với validation; trigger ghi audit; cursor duyệt người còn nợ sách rồi so với query theo tập. Ghi rõ dialect, phiên bản, input/output, kết quả khi không có hàng và khi vi phạm ràng buộc. Bài này là hướng dẫn thực hành, chưa cung cấp/kiểm thử mã server cụ thể.

## Bài 5 — Backup và report

Trên CSDL lab riêng của DBMS đã chọn, backup rồi restore vào database mới. So số hàng, FK, view, trigger và kết quả 4 truy vấn. Thiết kế form mượn/trả và report đang mượn có bộ lọc, quyền xem, thời điểm dữ liệu. Nộp schema/ERD, query, kết quả và giải thích, không chỉ ảnh chụp màn hình.
