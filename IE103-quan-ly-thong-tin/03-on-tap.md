# IE103 — Phiếu ôn

> [!IMPORTANT]
> **Trước khi chốt SQL:** xác định một hàng kết quả đại diện cho gì; kiểm tra JOIN nhân hàng, NULL và trường hợp không có liên hệ; chỉ thêm `ORDER BY` khi cần thứ tự.

| Khái niệm | Điều cần giải thích được |
|---|---|
| PK / FK / candidate key | Duy nhất, tham chiếu, tối thiểu |
| ERD | Cardinality, tùy chọn, chuyển M:N |
| FD / bao đóng | Từ nghiệp vụ, không suy chỉ từ mẫu |
| 2NF / 3NF / BCNF | Kiểm tra trên mọi candidate key/FD liên quan |
| LEFT JOIN | Vị trí điều kiện ON/WHERE làm thay đổi hàng giữ lại |
| NULL | Logic ba trị; IS NULL; bẫy NOT IN |
| COUNT | COUNT(*) khác COUNT(cột có NULL) |
| ACID | Giao dịch không tự sửa mọi lỗi nghiệp vụ |
| Index | Tăng tốc truy vấn phù hợp, làm ghi tốn thêm |
| XML / XPath / XQuery | Cây / chọn và tính / truy vấn biến đổi |
| Trigger / procedure | Tự theo sự kiện / gọi tường minh, tùy DBMS |
| Replication / backup | Bản sao phục vụ / bản phục hồi |

Trước khi nộp câu SQL: xác định mức hạt hàng kết quả; kiểm tra một người không có quan hệ; thử nhiều quan hệ và NULL; kiểm tra JOIN có nhân hàng; thêm ORDER BY nếu yêu cầu thứ tự; giải thích bằng dữ liệu nhỏ.

Tự kiểm tra 60 phút đề xuất: 10 phút ERD, 10 phút FD/chuẩn hóa, 20 phút 4 truy vấn, 10 phút transaction/bảo mật, 10 phút XML/NoSQL. Đây là bài tự luyện, không phải cấu trúc đề thi lớp.
