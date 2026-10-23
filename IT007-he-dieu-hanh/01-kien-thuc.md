# IT007 — Kiến thức hệ điều hành

## 1. Vai trò và cấu trúc OS

OS cung cấp abstraction (process, virtual memory, file) và phân phối tài nguyên (CPU, RAM, disk, thiết bị). Kernel chạy quyền đặc biệt; ứng dụng thường chạy user mode và dùng system call để yêu cầu dịch vụ. Chuyển user↔kernel mode không luôn là context switch sang tiến trình khác.

Interrupt thường từ thiết bị/timer; exception phát sinh đồng bộ từ lệnh đang thực thi như chia 0 hoặc page fault; system call là lối vào có kiểm soát. Tên gọi trap/exception có thể khác giữa giáo trình/kiến trúc; nêu ngữ cảnh khi trả lời.

Monolithic kernel tích hợp nhiều dịch vụ trong kernel; microkernel giữ lõi nhỏ và chuyển một số dịch vụ ra user space; kiến trúc thực tế có biến thể. Boot nạp OS và khởi động dịch vụ; shell là giao diện lệnh, không đồng nghĩa kernel.

## 2. Process và thread

Program là mã/dữ liệu tĩnh; process là thể hiện đang chạy với không gian địa chỉ, tài nguyên và trạng thái. PCB thường giữ PID, thanh ghi, PC, trạng thái, thông tin lập lịch và bộ nhớ. Trạng thái cơ bản: new → ready → running → waiting/blocked → ready → terminated. Tiến trình đang chờ I/O không tranh CPU như ready.

Context switch lưu trạng thái thực thi và nạp trạng thái khác, có overhead trực tiếp và ảnh hưởng cache/TLB. Thread có luồng điều khiển, thanh ghi và stack riêng; các thread cùng process thường chung code, heap và file descriptor. Stack riêng không có nghĩa mọi dữ liệu luôn riêng nếu truyền con trỏ đến nó.

Concurrency là nhiều công việc có tiến triển đan xen; parallelism là thực thi đồng thời trên nhiều tài nguyên. Một CPU có concurrency mà không chạy hai lệnh thread cùng thời điểm. Nhiều core không tự làm chương trình nhanh nếu bị phần tuần tự/lock/I/O.

IPC: pipe, message queue, socket, shared memory. Shared memory cần đồng bộ; message passing cần xử lý giao thức và lỗi. Linux `fork()` tạo process con với không gian địa chỉ riêng, thường tận dụng copy-on-write; `exec` thay ảnh chương trình; `wait` thu trạng thái con. Sau fork, thứ tự chạy cha/con không đảm bảo. Zombie đã kết thúc nhưng chưa được thu trạng thái; orphan mất cha và được tiến trình khác nhận quản lý theo cơ chế hệ thống.

## 3. Lập lịch CPU

Preemptive cho phép ngắt tiến trình đang chạy để chọn tiến trình khác; non-preemptive thường giữ CPU đến khi block/kết thúc. Tiêu chí: CPU utilization, throughput, turnaround, waiting, response và công bằng.

Với một CPU burst, bỏ I/O và overhead: `TAT = completion − arrival`, `WT = TAT − burst`, `RT = first_start − arrival`. Có I/O thì WT phải trừ cả thời gian blocked tương ứng, không dùng công thức đơn giản một cách mù quáng.

| Thuật toán | Quy tắc | Bẫy |
|---|---|---|
| FCFS | Đến trước chạy trước, không ngắt | Convoy effect |
| SJF | Burst ngắn nhất trong ready, không ngắt | Cần dự đoán burst; có starvation |
| SRTF | Remaining ngắn nhất, có ngắt | Phải xét sự kiện arrival |
| Priority | Theo độ ưu tiên | Quy ước số nhỏ/lớn phải ghi; aging giảm starvation |
| Round Robin | Hàng đợi vòng, quantum q | q nhỏ tăng overhead; q lớn tiến tới FCFS |
| Multilevel feedback | Di chuyển giữa hàng đợi theo hành vi | Phụ thuộc quy tắc cụ thể |

Ví dụ FCFS cùng đến lúc 0, burst P1=5,P2=3,P3=1: Gantt P1[0,5],P2[5,8],P3[8,9]. WT=0,5,8 trung bình 13/3; TAT=5,8,9 trung bình 22/3. Nếu SJF với cùng giả định: P3,P2,P1, WT=0,1,4 theo thứ tự chạy, trung bình 5/3. Cần ghi quy tắc hòa khi cùng arrival/burst.

## 4. Race condition và critical section

`counter += 1` có thể gồm đọc, tính, ghi. Hai thread cùng đọc 0 rồi cùng ghi 1 làm mất một lần tăng. Race condition là kết quả phụ thuộc thứ tự đan xen không được kiểm soát. Critical section truy cập tài nguyên dùng chung cần loại trừ lẫn nhau nếu có xung đột.

Ba yêu cầu thường học: mutual exclusion (không cùng vào), progress (tiến triển khi có người muốn vào), bounded waiting (không đợi vô hạn sau yêu cầu theo giả định). Việc thỏa các yêu cầu phụ thuộc mô hình bộ nhớ và atomic operation; thuật toán trên giấy không luôn chuyển nguyên xi sang CPU/compiler hiện đại.

Mutex giữ quyền sở hữu và lock/unlock vùng tới hạn. Spinlock chờ bận, hợp trong một số vùng ngắn và môi trường kernel; blocking lock nhường CPU khi phải đợi. Không giữ khóa qua thao tác I/O dài khi có thể tách logic an toàn.

## 5. Semaphore và condition variable

Semaphore có bộ đếm và thao tác nguyên tử wait/P (xin), signal/V (trả). Counting semaphore quản lý nhiều slot; binary semaphore có thể dùng cho phối hợp nhưng không hoàn toàn đồng nghĩa mutex về ownership. Condition variable cho thread ngủ chờ điều kiện dưới mutex; chờ bằng vòng `while`, vì thức dậy không đảm bảo điều kiện còn đúng.

Producer–consumer, buffer N: `empty=N, full=0, mutex=1`. Producer: wait(empty), wait(mutex), thêm item, signal(mutex), signal(full). Consumer: wait(full), wait(mutex), lấy item, signal(mutex), signal(empty). Nếu giữ mutex rồi chờ empty/full có thể chặn phía cần mutex để làm điều kiện đổi.

Readers–writers cân bằng quyền đọc và ghi theo policy; dining philosophers minh họa deadlock/starvation. Không chỉ nêu “dùng semaphore” mà phải chỉ tài nguyên, invariant, thứ tự thao tác và khả năng tiến triển.

## 6. Deadlock

Bốn điều kiện Coffman: mutual exclusion, hold-and-wait, no preemption, circular wait. Chúng là các điều kiện cần cho deadlock trong mô hình thông thường; sự tồn tại của cả bốn khả năng không chứng minh hệ đang deadlock tại thời điểm đó.

Prevention phá một điều kiện như lấy khóa theo thứ tự toàn cục. Avoidance chỉ cấp nếu còn trạng thái an toàn theo nhu cầu cực đại đã biết, ví dụ Banker. Detection tìm tình trạng deadlock rồi recovery bằng thu hồi/rollback/kết thúc tùy tài nguyên. Ignoring là quyết định có chủ đích khi chi phí khác cao, không là giải pháp mọi bài.

Banker: `Need = Max − Allocation`. Bắt đầu `Work=Available`; chọn tiến trình chưa Finish có Need≤Work theo từng loại tài nguyên; giả sử nó xong, Work+=Allocation; lặp. Hoàn thành hết thì safe. Unsafe không đồng nghĩa đã deadlock; nó nghĩa không đảm bảo chuỗi hoàn tất theo mức yêu cầu cực đại.

Với một instance mỗi loại tài nguyên, cycle trong resource-allocation graph cho deadlock theo mô hình cơ bản; nhiều instance thì cycle chỉ là dấu hiệu cần kiểm tra thêm.

## 7. Bộ nhớ và dịch địa chỉ

Địa chỉ logic/ảo do process dùng; địa chỉ vật lý trỏ RAM; MMU thực hiện dịch và kiểm tra quyền. Contiguous allocation dùng vùng liên tiếp; external fragmentation là lỗ trống tổng đủ nhưng không liền; internal fragmentation là phần thừa bên trong khối đã cấp. First fit chọn lỗ đầu đủ; best fit chọn lỗ nhỏ nhất đủ; worst fit chọn lỗ lớn nhất, không thuật toán nào luôn tốt nhất.

Paging chia không gian ảo thành page và RAM thành frame cùng cỡ. Với page size 2^d, offset có d bit. `page = VA // page_size`, `offset = VA % page_size`, `PA = frame[page] * page_size + offset` nếu entry hợp lệ. Page table còn chứa quyền/present/dirty/reference tùy kiến trúc.

Ví dụ page size 1024, VA=2500 → page 2, offset 452. Nếu page 2 ở frame 7 thì PA=7620. Không tra page table khi chưa tách đúng page/offset.

TLB cache ánh xạ địa chỉ, không phải cache nội dung page. Với mô hình TLB tra tuần tự trước RAM, page table một cấp, không page fault: EAT = h(t_TLB+t_RAM) + (1−h)(t_TLB+2t_RAM). Kiến trúc tra song song/nhiều cấp có mô hình khác; ghi giả định trước khi tính.

Segmentation chia theo đoạn logic có base/limit; có thể kết hợp paging. Paging tránh phân mảnh ngoài ở mức cấp frame nhưng vẫn có phân mảnh trong và chi phí page table. Đừng nói paging loại bỏ mọi loại lãng phí.

## 8. Bộ nhớ ảo và thay trang

Demand paging nạp page khi cần. Page fault là truy cập page cần xử lý vì ánh xạ/trạng thái chưa đáp ứng; với bài cơ bản thường là page chưa ở RAM. OS kiểm tra hợp lệ, tìm frame hoặc chọn nạn nhân, ghi dirty page nếu cần, nạp dữ liệu, cập nhật bảng/TLB và chạy lại lệnh. Truy cập không hợp lệ có thể kết thúc process thay vì nạp trang.

FIFO bỏ page vào sớm nhất; LRU bỏ page lâu nhất không dùng; OPT bỏ page có lần dùng tiếp xa nhất trong tương lai, dùng làm chuẩn so sánh chứ không biết tương lai thực. Clock xấp xỉ bằng reference bit. FIFO có thể có Belady anomaly: tăng frame vẫn tăng lỗi; LRU/OPT có tính chất stack trong mô hình chuẩn.

Chuỗi `1,2,3,1,4,2,5` với 3 frame rỗng: FIFO 5 lỗi; LRU 6 lỗi. Phải phân biệt hit có thay đổi thứ tự chính sách hay không: FIFO không đổi lúc hit; LRU có cập nhật độ mới. Script lab in kết quả để đối chiếu.

Thrashing xảy ra khi hệ dành nhiều thời gian paging thay vì làm việc do working set không đủ chỗ và tải quá mức. Có thể giảm multiprogramming, thêm RAM, điều chỉnh workload; chỉ tăng swap không đảm bảo hiệu năng.

## 9. File system và I/O

File là abstraction cho dữ liệu; directory ánh xạ tên đến đối tượng file; metadata giữ kích thước, quyền, thời gian và thông tin block tùy FS. File descriptor là handle trong process. Hard link tham chiếu cùng đối tượng file trong giới hạn FS; symbolic link lưu đường dẫn, có thể bị gãy.

Cấp phát file có contiguous, linked, indexed/extents; đánh đổi truy cập ngẫu nhiên, phân mảnh và metadata. Buffer/cache giảm I/O; write-back cần cơ chế đảm bảo bền theo yêu cầu. Journaling hỗ trợ phục hồi tính nhất quán cấu trúc sau sự cố, không tự bảo vệ mọi dữ liệu ứng dụng hay thay backup.

Polling liên tục kiểm tra thiết bị; interrupt báo sự kiện; DMA chuyển khối dữ liệu với ít can thiệp CPU hơn, CPU vẫn thiết lập và xử lý hoàn tất. Disk scheduling như FCFS/SSTF/SCAN/C-SCAN minh họa tối ưu di chuyển đầu đọc HDD; mô hình seek của HDD không áp nguyên xi cho SSD.

## 10. Bảo vệ và thực hành OS

Least privilege giới hạn tác động. Quyền Linux rwx cho owner/group/others; thư mục cần x để đi qua, r để liệt kê tên, w để thay mục theo các quy tắc bổ sung. `chmod 640 file` là owner rw, group r, others không quyền. Chỉ chmod file lab của mình; tránh cấp 777 như cách chữa mọi lỗi.

Phân biệt mechanism (cơ chế kiểm soát) và policy (ai được quyền). Windows/Linux đều có process/thread, virtual memory, security và file system; khác API/công cụ/chi tiết. Không học bằng đối lập “hệ này luôn nhanh/an toàn hơn” mà thiếu workload và cấu hình.

Khi debug: quan sát process/CPU/RAM/I/O, đọc thông báo lỗi, dựng ví dụ nhỏ, thay một yếu tố rồi kiểm tra lại. Mã mô phỏng Python trong kho là mô hình học thuật, không là bộ lập lịch kernel thật.
