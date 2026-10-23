# Kết quả kiểm tra bộ học liệu

Kiểm tra trên Windows với **Python 3.8.10**, ngày 23/10/2026:

- Liên kết Markdown tới file nội bộ tồn tại; cặp code fence cân bằng.
- IPv4: network/broadcast/host, các trường hợp /0, /26, /31, /32 và đầu vào sai.
- SQLite: kết quả 4 truy vấn; FK; trigger chặn trùng lượt mượn khi INSERT và UPDATE; thứ tự ngày; trả rồi mượn lại; rollback; parameter binding. XML: đọc title B01 từ file mẫu.
- OS: Gantt FCFS/RR, thời gian đợi, khoảng idle, lỗi trang FIFO/LRU, Banker safe/unsafe và một số đầu vào sai.
- Gauss: nghiệm được thế lại vào hệ gốc; vector kernel thỏa Ax=0; rank-nullity; hệ duy nhất/vô số/vô nghiệm; đổi hàng; hệ toàn0; hệ dư phương trình và phân số.

Chạy lại tại gốc bộ tài liệu:

```console
python scripts/kiem_tra.py
```

Giới hạn kiểm tra: không tự động duyệt mọi URL bên ngoài; không kiểm tra hiển thị Markdown bằng trình duyệt; chưa compile/chạy mẫu C vì môi trường WSL hiện chưa có `cc`; chưa chạy XQuery bằng processor chuyên dụng; chưa có DBMS của lớp để thử stored procedure/cursor/backup server. Các bài thao tác thủ công cần người học thực hiện theo hướng dẫn.

Kiểm tra lab không chứng minh mọi diễn giải lý thuyết hoặc bài tự luận đều không còn sai sót. Đối chiếu định nghĩa, ký hiệu và yêu cầu đánh giá với giảng viên.
