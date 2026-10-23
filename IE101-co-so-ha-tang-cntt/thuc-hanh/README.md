# IE101 — Lab hạ tầng

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
