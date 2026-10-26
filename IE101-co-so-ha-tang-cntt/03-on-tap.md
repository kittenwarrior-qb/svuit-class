# IE101 — Phiếu ôn tập

> [!IMPORTANT]
> **Bài tính subnet:** prefix → block → network → broadcast → host. **Bài thiết kế:** yêu cầu → sơ đồ → tính tải → rủi ro → cách kiểm thử/phục hồi.

| Nhớ nhanh | Ý nghĩa / bẫy |
|---|---|
| Mbps / 8 = MB/s | Trần lý thuyết, chưa overhead |
| /p IPv4 → 2^(32−p) | /31, /32 có cách dùng riêng |
| Switch / router | MAC trong LAN / IP giữa mạng |
| DHCP / DNS | Cấp cấu hình / phân giải tên |
| RAM / disk | Dữ liệu đang chạy / lưu bền |
| VM / container | OS khách riêng / thường chung kernel |
| RAID / backup | Chịu lỗi ổ / khôi phục bản dữ liệu |
| RPO / RTO | Mất dữ liệu cho phép / thời gian phục hồi |
| Uptime tỷ lệ | Chỉ có ý nghĩa với cửa sổ đo rõ |

Tự kiểm tra không nhìn tài liệu: vẽ đường đi HTTPS; chia /24 cho 60/30/10 host; giải thích NAT và firewall; kể ba nguy cơ mà RAID không xử lý; viết runbook DNS hỏng; thiết kế một phép thử restore có tiêu chí đạt.

Khi làm bài subnet: viết prefix → block → network → broadcast → host → kiểm tra IP ban đầu. Khi làm bài kiến trúc: yêu cầu → giả định → sơ đồ → tính toán → rủi ro → phương án kiểm thử.
