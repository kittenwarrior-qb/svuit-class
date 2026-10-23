# IT007 — Lab

## 1. Mô phỏng thuật toán

```console
python IT007-he-dieu-hanh/thuc-hanh/mo_phong.py
```

Chạy tại gốc bộ tài liệu; Python 3.8+, không gói ngoài. FCFS có arrival; RR ở đây **chỉ hỗ trợ mọi AT=0**, q>0, overhead=0. FIFO/LRU giả sử frame ban đầu rỗng. Banker nhận số tài nguyên có sẵn, Allocation, Max; trả một chuỗi chỉ số process hoặc None nếu unsafe.

Kỳ vọng: FCFS CT=5,8,9; RR CT=9,8,5 theo P1,P2,P3; FIFO=5 lỗi, LRU=6; chuỗi an toàn=[0,1,2]. Tự đổi một tham số, dự đoán bằng tay rồi mới chạy. Bài mở rộng: RR có arrival, SRTF có hòa, OPT có nhìn trước chuỗi. Mã hiện tại chưa hiện thực các phần mở rộng.

## 2. Shell và process — thao tác thủ công Linux/WSL

Chạy các lệnh quan sát: `pwd`, `ls -l`, `ps -ef`, `top`, `free -h`, `df -h`. Tạo folder lab của riêng mình, tạo file văn bản rồi thử `chmod 640` và đọc quyền. Viết script Bash nhận tên folder và đếm file thường; kiểm tra tên có khoảng trắng, folder rỗng và đường dẫn không tồn tại. Quote biến, ví dụ `"$1"`, để tránh tách từ ngoài ý muốn.

Nộp: lệnh, kết quả đã lược dữ liệu riêng và giải thích. Không dùng `sudo` chỉ để bỏ qua lỗi mà chưa hiểu quyền cần thiết.

## 3. fork/exec/wait — C tùy chọn

Trong Linux/WSL có compiler C, tại folder này:

```console
cc -Wall -Wextra -std=c11 fork_demo.c -o /tmp/svuit-fork-demo
/tmp/svuit-fork-demo
```

Con in value=20; cha sau wait in value=10 vì bộ nhớ riêng. Mã này đợi con trước dòng in cha nên thứ tự hai dòng được kiểm soát; nếu chuyển printf cha lên trước wait thì thứ tự không đảm bảo. Thêm exec chạy một lệnh vô hại và quan sát mã sau exec chỉ chạy nếu exec lỗi. Không tạo vòng fork vô hạn.

Mẫu C cần Linux/WSL; trình kiểm tra Python không compile nó. Nếu không có môi trường phù hợp, làm bài phân tích mã và ghi rõ chưa chạy.

## 4. Đồng bộ — bài thực hành thiết kế

Viết hai worker tăng counter dùng khóa, join xong kiểm tra tổng. Sau đó mô hình producer–consumer bằng queue có kích thước giới hạn. Giải thích invariant “0≤số item≤N”. Không cố chứng minh race condition chỉ bằng chạy bản không khóa vài lần; scheduler/GIL có thể che lỗi. Cần trình bày interleaving gây sai và lý do khóa ngăn nó.

## 5. Báo cáo

Mỗi lab có giả định, môi trường, cách chạy, kỳ vọng, kết quả, giải thích và giới hạn. Gantt hoặc bảng frame phải kèm bước tính tay. Log chạy không thay phần hiểu cơ chế.
