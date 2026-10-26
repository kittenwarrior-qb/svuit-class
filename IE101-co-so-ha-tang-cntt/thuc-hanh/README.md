# IE101 — Lab hạ tầng

Đọc song song với [Field Notes](../notes/README.md): computer systems → networking → services → VM/container/cloud → security/operations/design. Labs dưới đây ưu tiên quan sát an toàn, không thay đổi cấu hình production.

## Lab 1: quan sát máy đang dùng

Trên Windows PowerShell: `Get-ComputerInfo`, `Get-Process`, `Get-NetIPConfiguration`, `Resolve-DnsName example.org`. Trên Ubuntu: `uname -a`, `free -h`, `df -h`, `ip addr`, `ip route`, `getent hosts example.org`. Kết quả IP/process có thể chứa thông tin cá nhân; chỉ ghi phần cần thiết.

Nộp bảng CPU/RAM/disk/OS, IP-prefix-gateway-DNS và giải thích từng trường. Phân biệt dung lượng đĩa còn trống và RAM khả dụng. Lệnh cần module/công cụ hệ điều hành tương ứng; đây là bài thao tác thủ công.

## Lab 2: kiểm tra subnet

```console
python IE101-co-so-ha-tang-cntt/thuc-hanh/subnet.py 192.168.10.70/26
```

Chạy từ gốc bộ học liệu. Tự tính trước; kỳ vọng network .64, broadcast .127, 62 host. Thử /27, /31, /32. Script IPv4 dùng thư viện `ipaddress`; không gửi packet, không sửa cấu hình mạng.

## Lab 3: phương án sao lưu

Tạo bộ file thử trong `ket-qua-ca-nhan/`, chép bản sao sang nơi riêng, sửa một file rồi phục hồi vào folder khác để so sánh. Ghi thời điểm backup, số file/byte, thời gian restore và kết quả đối chiếu nội dung. Không dùng dữ liệu quan trọng cho thử nghiệm xóa/sửa. Kết luận RPO/RTO từ phép thử có giới hạn, không suy rộng sang hệ thống sản xuất.

## Lab 4: thiết kế phòng học

Hoàn thành bài 10 trong tập bài tập. Báo cáo 2–4 trang có sơ đồ, bảng IP/VLAN, ma trận quyền, cấu hình tối thiểu theo giả định và phép thử nghiệm thu. Không cần mua máy hay tạo dịch vụ cloud trả phí để làm bài này.

## Lab 5: truy vết một HTTPS request

Với một website công khai bạn được phép truy cập, ghi lại DNS answer, thời gian kết nối, TLS/certificate result và HTTP status bằng browser DevTools hoặc các lệnh đọc-only trong [Networking notes](../notes/02-networking.md). Không quét cổng, brute-force, hoặc gửi tải lớn. Vẽ sequence: client → resolver → edge → app → dependency; đánh dấu phần nào không thể quan sát từ máy client.

## Lab 6: container lifecycle (tùy chọn)

Chỉ chạy nếu máy đã có Docker và không yêu cầu cài thêm phần mềm. Trước khi chạy, kiểm tra image name, publisher, tag và cấu hình. Dùng image mẫu được tài liệu Docker chính thức khuyến nghị; không mount thư mục cá nhân, không nhập credential. Quan sát image/container/log/port/volume; sau đó stop/remove đúng tài nguyên của lab. Tham khảo [Docker architecture](https://docs.docker.com/get-started/docker-overview/) và [notes về containers](../notes/04-virtualization-containers-cloud.md).

**Deliverable:** một bảng `action → expected result → observed result → explanation`; che username, hostname, public IP, token, và dữ liệu cá nhân trước khi chia sẻ.
