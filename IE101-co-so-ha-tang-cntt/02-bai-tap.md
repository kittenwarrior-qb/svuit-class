# IE101 — Bài tập tự soạn

## Đề bài

1. Chuyển 200 Mbps thành MB/s lý thuyết. File 5 GB mất ít nhất bao lâu? Giả sử hệ thập phân, bỏ overhead.
2. Tìm network, broadcast, dải host của `192.168.20.145/27`.
3. Chia `192.168.50.0/24` thành 4 subnet bằng nhau; liệt kê network, host và broadcast.
4. Phòng có 45 máy và một gateway, chọn prefix nhỏ nhất đủ dùng; giải thích vì sao /27 không đủ.
5. Dùng VLSM cho 100, 50, 20 host trong `10.10.0.0/24`; bố trí từ subnet lớn trước.
6. Có 4 ổ 2 TB: tính dung lượng RAID 0, 5, 6, 10 trước overhead; so sánh chịu lỗi.
7. Hệ thống cần RPO 1 giờ, RTO 2 giờ. Sao lưu hằng đêm và restore 4 giờ có đạt không? Đề xuất thay đổi.
8. Dịch vụ đạt uptime 718 giờ, downtime 2 giờ trong 30 ngày. Tính availability.
9. IP máy ping được gateway, DNS tên miền thất bại; nêu thứ tự kiểm tra. Vì sao ping thất bại không đủ kết luận máy chủ chết?
10. Thiết kế phòng học 40 máy có Internet, file dùng chung, Wi-Fi khách. Nộp sơ đồ, VLAN, luồng được phép, backup, sizing và cách nghiệm thu.

## Đáp án / hướng dẫn

1. 25 MB/s; 5.000 MB / 25 = 200 giây, khoảng 3 phút 20 giây. Thực tế lâu hơn do giao thức và giới hạn nguồn/đích.
2. /27 block 32: network .128, broadcast .159, host .129–.158; 30 host.
3. /26: .0 (host .1–.62, BC .63); .64 (.65–.126, BC .127); .128 (.129–.190, BC .191); .192 (.193–.254, BC .255).
4. Cần ít nhất 46 địa chỉ host; /26 có 62, /27 có 30. Chừa thêm máy in/AP tùy yêu cầu.
5. `10.10.0.0/25` có 126 host; `10.10.0.128/26` có 62; `10.10.0.192/27` có 30. Còn `10.10.0.224/27`; các subnet không chồng lấn.
6. 8, 6, 4, 4 TB. RAID 0 không chịu lỗi; RAID 5 chịu 1 ổ; RAID 6 chịu 2 ổ; RAID 10 bảo đảm chịu 1 ổ, có thể chịu 2 nếu không cùng cặp mirror. Không tính đây là backup.
7. Không đạt cả hai. Cần bản sao/log theo khoảng ≤1 giờ và pipeline restore đã thử ≤2 giờ; kiểm tra thời gian phát hiện, cấp máy, phục hồi và xác minh. Có thể cần warm standby nhưng vẫn cần backup độc lập.
8. 718/720 × 100 ≈ 99,7222%.
9. Kiểm tra DNS được cấp đúng chưa; hỏi DNS trực tiếp, phân biệt lỗi resolver và authoritative, so cache/TTL, kiểm tra kết nối tới DNS và policy firewall. ICMP có thể bị chặn dù TCP/HTTPS vẫn phục vụ.
10. Một phương án: VLAN máy học, server, khách và quản trị tách nhau; khách chỉ ra Internet; học viên truy cập dịch vụ học cần thiết; quản trị chỉ từ máy được phép. Đưa file server và backup ra hai nơi lưu khác nhau. Nghiệm thu gồm thử phân quyền, đo tải đồng thời, ngắt một thành phần theo kịch bản lab và diễn tập phục hồi. Điểm thiết kế phụ thuộc yêu cầu rõ ràng và bằng chứng, không có một sơ đồ duy nhất đúng.
