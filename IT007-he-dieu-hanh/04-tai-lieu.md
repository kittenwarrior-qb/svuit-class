# IT007 — Nguồn học

- [Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/): sách tại website tác giả, có các chương đọc miễn phí. Học process/scheduling, concurrency, memory, persistence. Đã mở 23/10/2026; đọc tại nguồn, không re-upload toàn bộ sách.
- [Linux man-pages — fork(2)](https://man7.org/linux/man-pages/man2/fork.2.html): API, giá trị trả về và lỗi; nguồn sơ cấp của dự án man-pages, đã mở cùng ngày. Tra thêm exec/wait/pthread theo lab.
- [Python threading](https://docs.python.org/3/library/threading.html): API lock/thread của Python; lưu ý khác biệt CPython/GIL và bản free-threaded, không dùng đặc điểm một bản Python để kết luận về OS nói chung.
- [Ubuntu Server documentation](https://documentation.ubuntu.com/server/): thao tác shell, quản lý tài khoản và OS thực tế.
- [SVUIT IT007 — mã nguồn tham khảo](https://github.com/SVUIT/mmtt/blob/main/docs/MonHocCoSoNganh/IT007.md): đã đối chiếu mô tả chương/lab; không áp dụng tỉ lệ điểm/thi của các khóa trước cho G12.
- [Folder Drive IT007 do trang SVUIT liên kết](https://drive.google.com/drive/folders/1Fv5QgPX6cuuvXp40pAEqgwweRLpMlHOM?usp=sharing): đã kiểm kê/tải đủ 70 mục vào `tai-lieu-lop/Drive-IT007/` (slide, lab, đề cương, bài tập và sách). Folder có tài liệu khóa cũ và một số bài làm sinh viên; giữ local, không commit lại lên GitHub công khai.
- [Thư viện UIT — hồ sơ tài liệu IT007](https://ir.vnulib.edu.vn/entities/publication/17283db5-7e69-4cb7-ba6b-70e528183357): đầu mục được liên kết từ danh mục đề cương UIT. Trang hồ sơ yêu cầu đăng nhập; đăng nhập để xem tên/phiên bản và quyền truy cập.
- [UIT Knowledge — ôn lý thuyết Hệ điều hành giữa kỳ](https://www.youtube.com/watch?v=BsmsDm5rS34): video ôn giữa kỳ do UIT Knowledge phát hành, được lập chỉ mục với đúng tên môn. Dùng bổ sung để nhớ khái niệm; video có thể thuộc lớp/đề cương và năm khác, nên đối chiếu phạm vi G12. Kênh cũng có [review giảng viên IT007](https://www.youtube.com/watch?v=Fddq4jPCvcg), hữu ích tham khảo chọn lớp, không phải bài giảng.
- [Kênh UIT Knowledge](https://www.youtube.com/@UIT_Knowledge/videos) và [website UIT Knowledge](https://uitknowledge.org/): website hiện liệt kê Hệ điều hành trong nhóm video đăng ký xem và yêu cầu email Teams/MSSV. Xác minh điều kiện truy cập/chi phí trước khi đăng ký.

Trình tự đọc đề xuất: process → CPU scheduling → threads/locks → deadlock → address translation → paging → file system. Sau mỗi chương tự làm một bài trước khi xem mô phỏng.
