# IE101 — Kiến thức nền

## 1. Hạ tầng là gì?

Hạ tầng CNTT là tài nguyên và dịch vụ làm nền cho ứng dụng: phần cứng, OS, mạng, lưu trữ, trung tâm dữ liệu, nền tảng triển khai và con người/quy trình vận hành. Khi thiết kế phải trả lời: ai dùng, tải bao nhiêu, dữ liệu quan trọng mức nào, mất dịch vụ tối đa bao lâu và ngân sách bao nhiêu?

Ví dụ hệ thống đăng ký môn: trình duyệt → DNS → mạng Internet → cổng TLS/load balancer → ứng dụng → CSDL. Mỗi đoạn có điểm hỏng, độ trễ, giới hạn tải và người chịu trách nhiệm. Một máy chủ mạnh không bù được truy vấn thiếu index hoặc đường truyền nghẽn.

Phân biệt hiệu năng (thời gian/tốc độ hoàn thành việc), khả năng mở rộng (đáp ứng khi tăng tải), tính sẵn sàng (dùng được khi cần), độ bền dữ liệu (khả năng giữ dữ liệu lâu dài) và khả năng bảo trì (sửa/đổi có kiểm soát).

## 2. Phần cứng và đơn vị

| Thành phần | Vai trò | Câu hỏi đo đạc |
|---|---|---|
| CPU | Thực thi lệnh, lõi/luồng | CPU bận bao nhiêu? Có nghẽn một lõi? |
| RAM | Dữ liệu đang dùng, mất khi tắt nguồn | Working set có vừa RAM? Có swap? |
| SSD/HDD | Lưu dữ liệu bền | IOPS, throughput, latency thế nào? |
| NIC | Gửi/nhận dữ liệu mạng | Tốc độ link và lưu lượng thực? |
| PSU/UPS | Nguồn và thời gian duy trì | Mất điện có tắt an toàn được? |

1 byte = 8 bit. 1 GB = 10^9 byte; 1 GiB = 2^30 byte. Link 100 Mbps có trần lý thuyết 12,5 MB/s trước overhead. Truyền file 1 GB qua 100 Mbps mất tối thiểu 80 giây nếu dùng hệ thập phân và không mất mát/overhead.

Latency là thời gian cho một thao tác; throughput là lượng việc mỗi đơn vị thời gian. IOPS cao hữu ích cho nhiều truy cập nhỏ, throughput cao hữu ích cho luồng tuần tự lớn. Cache giảm truy cập tầng chậm nhưng phải cân nhắc tính nhất quán và độ bền khi ghi.

Scale up: tăng tài nguyên một máy. Scale out: tăng số máy. Scale out yêu cầu ứng dụng chia tải và xử lý trạng thái; không tự động giúp một CSDL ghi đơn nút.

## 3. OS và dịch vụ

OS quản lý CPU, bộ nhớ, file, thiết bị và bảo vệ. Ứng dụng gọi system call để xin tài nguyên. Tiến trình là chương trình đang chạy, dịch vụ thường chạy nền. Người dùng, nhóm và quyền giúp giới hạn truy cập.

Quy trình triển khai cơ bản: kiểm kê yêu cầu → chuẩn bị máy/OS → cập nhật → tạo tài khoản/quyền → cấu hình dịch vụ → kiểm tra → giám sát → sao lưu → tài liệu hóa. Mỗi thay đổi nên có cách kiểm tra và rollback. Xem IT007 để học cơ chế bên trong.

## 4. Mạng máy tính

Mô hình TCP/IP thực dụng: application (HTTP, DNS), transport (TCP, UDP), internet (IP), link (Ethernet/Wi-Fi). TCP cung cấp luồng byte tin cậy, có thứ tự; UDP gửi datagram, không tự đảm bảo giao nhận/thứ tự. Ứng dụng có thể xây thêm cơ chế tin cậy trên UDP.

Switch lớp 2 chuyển frame trong LAN dựa trên MAC; router chuyển packet giữa mạng IP. ARP tìm MAC cho IPv4 trên cùng link. Nếu đích ngoài subnet, máy gửi frame tới MAC của gateway. NAT chuyển địa chỉ/cổng, không thay thế chính sách firewall. VLAN chia miền broadcast; cần định tuyến và ACL/firewall để kiểm soát liên lạc giữa VLAN.

Port xác định điểm cuối dịch vụ trong TCP/UDP. Cổng thường gặp: SSH 22, DNS 53, HTTP 80, HTTPS 443. Cổng mặc định có thể cấu hình khác. DNS thường dùng UDP nhưng cũng dùng TCP; không khẳng định DNS chỉ dùng UDP.

### IPv4 và CIDR

IPv4 có 32 bit. Prefix `/p` giữ p bit mạng. Với mạng thông thường từ /0 đến /30: số địa chỉ = 2^(32-p), host thường dùng = số địa chỉ − 2 (network và broadcast). /31 dùng đặc biệt cho point-to-point, /32 biểu diễn một địa chỉ; không áp công thức trừ 2 máy móc.

Ví dụ `192.168.10.70/26`: mask `255.255.255.192`, block 64 địa chỉ. .70 thuộc block .64–.127; network .64, broadcast .127, host .65–.126, 62 host. Gateway là một địa chỉ host được cấu hình, **không bắt buộc** là host đầu.

Mạng private IPv4 theo RFC 1918: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`. Không định tuyến trực tiếp toàn cầu. Private IP không có nghĩa là mọi thiết bị trong mạng đều đáng tin. IPv6 có 128 bit, không dùng broadcast như IPv4; `/64` phổ biến cho subnet LAN, không dùng phép trừ 2 host của IPv4.

## 5. Dịch vụ nền

DHCP cấp cấu hình IP, mask, gateway, DNS và thời gian lease. Với DHCPv4 thường mô tả Discover → Offer → Request → ACK. DNS phân giải tên: A (IPv4), AAAA (IPv6), CNAME (bí danh), MX (mail), NS (name server). TTL điều khiển thời gian cache, thay DNS có thể cần chờ cache cũ hết hạn.

Khi mở `https://example.org`: máy tìm IP qua DNS/cache; kết nối đến máy chủ; thương lượng TLS và kiểm tra chứng chỉ/tên máy; gửi HTTP; nhận phản hồi; trình duyệt tải tài nguyên. HTTP/1.1 và HTTP/2 thường trên TCP; HTTP/3 dùng QUIC trên UDP. HTTPS bảo vệ dữ liệu truyền, không chứng minh ứng dụng không có lỗ hổng.

Máy chủ file cung cấp truy cập file; CSDL cung cấp mô hình dữ liệu, truy vấn và giao dịch; web server phục vụ HTTP; reverse proxy đứng trước ứng dụng. Tách vai trò giúp quản lý, nhưng với lab nhỏ nhiều vai trò có thể chung máy nếu ghi rõ hạn chế.

## 6. Lưu trữ và phục hồi

DAS gắn trực tiếp; NAS cung cấp file qua mạng; SAN cung cấp block qua mạng chuyên dụng hoặc IP. Object storage lưu đối tượng với metadata và khóa, phù hợp ảnh/backup nhưng không đồng nghĩa ổ đĩa POSIX thông thường.

| RAID | Ý tưởng | Dung lượng với n ổ cùng cỡ S | Lưu ý |
|---|---|---|---|
| 0 | Chia dải | nS | Hỏng một ổ có thể mất mảng |
| 1 | Mirror | S với cặp 2 ổ | Không bảo vệ xóa nhầm |
| 5 | Một parity phân tán | (n−1)S, n ≥ 3 | Chịu hỏng 1 ổ; rebuild có rủi ro |
| 6 | Hai parity | (n−2)S, n ≥ 4 | Chịu hỏng 2 ổ |
| 10 | Stripe qua các cặp mirror | nS/2, n chẵn ≥ 4 | Khả năng chịu lỗi tùy ổ hỏng thuộc cặp nào |

RAID duy trì dịch vụ khi ổ hỏng; **backup** giữ bản sao để phục hồi khi xóa nhầm, mã độc hoặc mất cả hệ thống. Snapshot có thể phụ thuộc cùng storage; cần bản tách biệt. Chiến lược 3-2-1: 3 bản, 2 loại phương tiện, 1 bản ngoài nơi chính; nên có bản bất biến/offline tùy nhu cầu.

RPO: lượng thời gian dữ liệu có thể mất. RTO: thời gian mục tiêu để phục hồi dịch vụ. Backup mỗi 24 giờ có thể mất gần 24 giờ dữ liệu nếu không có cơ chế bổ sung. Phải thử restore: file tồn tại chưa chứng minh backup dùng được. Full sao toàn bộ; incremental sao thay đổi từ lần sao trước; differential sao thay đổi từ full gần nhất. Chuỗi incremental thiếu một mắt có thể không phục hồi được đến mốc mong muốn.

## 7. Ảo hóa, container, cloud

Hypervisor chạy VM, mỗi VM có OS khách riêng. Container cô lập tiến trình, thường dùng chung kernel của host. VM hợp khi cần OS/kernel khác hoặc ranh giới cô lập mạnh hơn; container thuận tiện đóng gói ứng dụng và triển khai nhất quán. Cả hai cần giới hạn tài nguyên, cập nhật và quản lý image.

IaaS cung cấp VM/mạng/đĩa; PaaS quản lý thêm nền tảng chạy; SaaS cung cấp ứng dụng hoàn chỉnh. Trách nhiệm bảo mật chia giữa nhà cung cấp và khách hàng tùy dịch vụ. Cloud có chi phí máy, đĩa, lưu lượng, backup và vận hành; không mặc định rẻ hơn on-premise. Tính tổng chi phí theo cùng thời hạn và mức sẵn sàng.

## 8. Bảo mật và vận hành

CIA: bí mật, toàn vẹn, sẵn sàng. Dùng quyền tối thiểu, tài khoản riêng, MFA khi phù hợp, cập nhật, phân đoạn mạng, mã hóa, quản lý secret và log. Không ghi mật khẩu vào repo. Firewall cho phép đúng luồng cần; thử kết nối sau khi đổi rule để tránh tự khóa truy cập.

Theo dõi metrics (số đo), logs (sự kiện), traces (đường đi yêu cầu). Đặt cảnh báo dựa trên ảnh hưởng và khả năng xử lý, ví dụ latency p95 và tỷ lệ lỗi; không chỉ CPU trung bình. p95 = 95% quan sát không vượt ngưỡng ấy, không phải trung bình.

Availability = uptime/(uptime+downtime), cần chỉ rõ cửa sổ đo và loại trừ. 99,9% trong 30 ngày cho phép xấp xỉ 43,2 phút downtime. Hai thành phần nối tiếp độc lập có availability 0,999 mỗi phần cho tổng khoảng 0,998001; giả định độc lập có thể sai vì chung điện/mạng.

Runbook sự cố: mô tả triệu chứng → kiểm tra phạm vi → thu bằng chứng → giảm ảnh hưởng → xử lý nguyên nhân → xác minh phục hồi → ghi bài học. Ví dụ web lỗi: DNS? route? port? TLS? HTTP status? app log? CSDL? Không khởi động lại mọi thứ trước khi thu bằng chứng.

## 9. Thiết kế và sizing

Bắt đầu từ workload và SLA, không bắt đầu từ hãng thiết bị. Dung lượng dự kiến = dữ liệu hiện tại + tăng trưởng + index/log/backup + khoảng trống vận hành. Ước lượng băng thông = người dùng đồng thời × tốc độ mỗi người × hệ số dự phòng; phân biệt đồng thời và tổng tài khoản.

Sơ đồ phải có client, mạng, gateway/firewall, máy chủ, storage, backup và luồng dữ liệu. Ghi giả định, giới hạn, điểm lỗi đơn, phương án phục hồi và cách đo nghiệm thu. Không cam kết RTO/RPO nếu chưa diễn tập.
