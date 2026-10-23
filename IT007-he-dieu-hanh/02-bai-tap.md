# IT007 — Bài tập tự soạn

## Đề bài

1. Phân biệt mode switch và context switch; process và thread.
2. FCFS: P1(AT=0,BT=5), P2(AT=1,BT=3), P3(AT=2,BT=1). Vẽ Gantt, tính CT/TAT/WT/RT, bỏ overhead/I/O.
3. SRTF với dữ liệu câu 2. Quy tắc hòa: giữ tiến trình đang chạy nếu remaining bằng nhau.
4. RR q=2, cả ba đến lúc 0, thứ tự P1,P2,P3, BT=5,3,1. Tính Gantt/WT trung bình, bỏ overhead.
5. Hai thread mỗi thread tăng x một lần từ x=0. Viết interleaving ra x=1; sửa bằng mutex.
6. Với buffer giới hạn, vì sao producer không nên giữ mutex rồi wait(empty)?
7. Available=(1,1); Allocation P0=(1,0), P1=(0,1), P2=(1,1); Max P0=(2,1), P1=(1,2), P2=(2,2). Tính Need và tìm chuỗi an toàn.
8. Page size 1 KiB, VA=2500, page 2→frame 7. Tính page, offset, PA.
9. Không gian ảo 32 bit, page 4 KiB, PTE 4 byte, page table một cấp phủ đủ không gian. Có bao nhiêu page, bảng trang bao nhiêu byte?
10. TLB hit=90%, lookup=10 ns, RAM=100 ns. Dùng mô hình tuần tự một cấp, không page fault, tính EAT.
11. Chuỗi 1,2,3,1,4,2,5 có 3 frame rỗng, đếm FIFO và LRU, ghi từng bước.
12. Hệ có page fault service time 8 ms và thời gian truy cập thường 100 ns. p=10^-6; xấp xỉ EAT=(1−p)100 + p·8.000.000 ns là bao nhiêu? Nêu giả định.
13. Các lỗ trống 100,500,200,300,600 KiB; cấp lần lượt 212,417,112,426 bằng first fit, phần thừa còn dùng được. Ghi vị trí cấp.
14. Soạn chương trình fork nhỏ: cha in PID con và wait; con in PID/PPID. Vì sao không được khẳng định thứ tự dòng in nếu không đồng bộ?

## Lời giải

1. Mode switch đổi mức quyền, có thể vẫn cùng thread; context switch thay trạng thái thực thi thread/process. Thread cùng process chia sẻ nhiều tài nguyên, process có không gian địa chỉ riêng theo mô hình thông thường.
2. P1[0,5] P2[5,8] P3[8,9]. Theo P1,P2,P3: CT=(5,8,9), TAT=(5,7,7), WT=(0,4,6), RT=(0,4,6). WT trung bình=10/3. P2,P3 chỉ được chọn sau P1 vì FCFS không ngắt.
3. P1[0,1], P2[1,2], P3[2,3], P2[3,5], P1[5,9]. CT=(9,5,3), TAT=(9,4,1), WT=(4,1,0), RT=(0,0,0). WT trung bình=5/3.
4. P1[0,2],P2[2,4],P3[4,5],P1[5,7],P2[7,8],P1[8,9]. CT=(9,8,5); TAT cũng vậy do AT=0; WT=(4,5,4), trung bình=13/3; RT=(0,2,4).
5. T1 đọc 0, T2 đọc 0, T1 ghi 1, T2 ghi 1. Khóa phải bao trọn đọc-sửa-ghi; chỉ khóa bước ghi không đủ. Không phụ thuộc một lần chạy Python có tình cờ lộ lỗi hay không để chứng minh an toàn.
6. Khi empty=0, producer ngủ giữ mutex; consumer không lấy được mutex để rút item, nên không signal empty được. Chờ số slot trước rồi vào vùng tới hạn.
7. Need P0=(1,1), P1=(1,1), P2=(1,1). Work ban đầu (1,1), chọn P0 rồi Work=(2,1); chọn P1 →(2,2); chọn P2 →(3,3). Có chuỗi P0,P1,P2; cũng có chuỗi khác. An toàn không có nghĩa lúc nào cũng cấp được mọi yêu cầu ngay.
8. page=2, offset=452, PA=7×1024+452=7620.
9. 2^20 page, bảng=2^20×4=2^22 byte=4 MiB. Bỏ qua cấu trúc nhiều cấp và overhead bổ sung.
10. 0,9×110 + 0,1×210 =120 ns.
11. FIFO: F,F,F,H,F,H,F =5. LRU: F,F,F,H,F,F,F =6. Sau tham chiếu 1 thứ tư, LRU xem 1 mới dùng; FIFO vẫn coi 1 vào đầu tiên.
12. 107,9999 ns, xấp xỉ108 ns. Giả định service time đã là toàn bộ chi phí nhánh fault, bỏ ảnh hưởng cache/TLB và chờ I/O khác; nếu đề định nghĩa khác phải lập lại công thức.
13. 212 vào lỗ500 còn288; 417 vào600 còn183; 112 vào phần288 còn176; 426 không có lỗ đủ, dù tổng còn trống lớn hơn426. Đây là external fragmentation theo mô hình cho trước.
14. Scheduler có thể chọn cha hoặc con trước; buffering stdout còn ảnh hưởng thứ tự nhìn thấy. wait chỉ bảo đảm cha sau wait biết con đã xong, không sắp thứ tự các dòng trước wait. Xem mã C mẫu trong lab.
