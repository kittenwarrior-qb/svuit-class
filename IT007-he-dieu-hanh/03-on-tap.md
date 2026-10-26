# IT007 — Công thức và lỗi hay gặp

> [!IMPORTANT]
> **Ba dạng cần luyện tay:** vẽ Gantt và tính WT/TAT/RT; mô phỏng semaphore/Banker; dịch địa chỉ và đếm lỗi trang. Nêu giả định về hòa, quantum, I/O và số frame trước khi tính.

```text
TAT = CT - AT
WT = TAT - BT        (một CPU burst, bỏ I/O)
RT = first_start - AT
Need = Max - Allocation
page = VA // page_size; offset = VA % page_size
PA = frame * page_size + offset
EAT_TLB = h(t + m) + (1-h)(t + 2m)  (mô hình tuần tự, 1 cấp)
```

Khi vẽ Gantt: liệt kê sự kiện đến và ready queue; cập nhật remaining; ghi quy tắc hòa, preemption, quantum và overhead. Tính từng process trước khi lấy trung bình. Nếu CPU nhàn, vẽ khoảng idle.

Khi tính thay trang: ghi số frame ban đầu, đánh dấu H/F và frame nạn nhân. FIFO chỉ đổi thứ tự khi nạp; LRU đổi khi truy cập. OPT cần biết cả chuỗi tương lai.

Khi giải đồng bộ: xác định tài nguyên, invariant, giá trị khởi tạo, thứ tự wait/signal, vùng tới hạn; kiểm tra trường hợp buffer rỗng/đầy và nhiều người chờ. Kiểm tra không deadlock chưa đủ chứng minh không starvation.

Lỗi thường gặp: unsafe=deadlock; fork tạo thread; virtual memory=swap; page fault luôn là lỗi chương trình; paging hết mọi phân mảnh; mutex và semaphore luôn thay thế nhau; kiểm tra một lần chạy đúng là đã chứng minh hết race condition.

Ôn miệng: hành trình system call; vòng đời process; vì sao context switch tốn phí; lost update; 4 điều kiện deadlock; dịch địa chỉ; TLB khác page table; page fault khác TLB miss; journaling khác backup.
