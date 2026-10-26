# 06 — Acronym Glossary / Bảng viết tắt

Ôn chủ động: che cột bên phải, tự nói đầy đủ acronym, rồi giải thích nó ảnh hưởng gì đến thiết kế/vận hành.

| Acronym | Full form | One-line meaning |
|---|---|---|
| ACL | Access Control List | Rules granting/denying actions to identities on resources. |
| API | Application Programming Interface | Contract through which software components communicate. |
| ARP | Address Resolution Protocol | Maps a local IPv4 next hop to a link-layer address. |
| A / AAAA | Address record / IPv6 address record | DNS name to IPv4 / IPv6 address. |
| BYOD | Bring Your Own Device | Personally owned device used for work/study access. |
| CIDR | Classless Inter-Domain Routing | Prefix-based IP network notation, e.g. `/24`. |
| CPU | Central Processing Unit | General-purpose instruction execution resource. |
| DHCP | Dynamic Host Configuration Protocol | Automatically leases host network configuration. |
| DNS | Domain Name System | Distributed naming and record lookup system. |
| DAS | Direct-Attached Storage | Storage directly attached to a host. |
| FaaS | Function as a Service | Managed event-driven function execution model. |
| HTTP / HTTPS | Hypertext Transfer Protocol / HTTP Secure | Web request-response protocol / HTTP protected with TLS. |
| ICMP | Internet Control Message Protocol | IP diagnostics and error reporting. |
| IOPS | Input/Output Operations Per Second | Storage operation rate. |
| IP / IPv4 / IPv6 | Internet Protocol / version 4 / version 6 | Network-layer addressing and packet delivery. |
| IaaS | Infrastructure as a Service | Cloud model exposing virtual infrastructure primitives. |
| LAN | Local Area Network | Network covering a limited local area. |
| MAC | Media Access Control | Link-layer address used on a local network segment. |
| MFA | Multi-Factor Authentication | Authentication using independent factor categories. |
| MTU | Maximum Transmission Unit | Maximum payload size for a link layer without fragmentation at that layer. |
| MX / NS / TXT | Mail eXchanger / Name Server / Text | Common DNS record types. |
| NAS / SAN | Network-Attached Storage / Storage Area Network | Network file access / network block-storage architecture. |
| NAT | Network Address Translation | Rewrites IP address and often transport port information. |
| NIC | Network Interface Card | Host hardware/software endpoint for network connectivity. |
| OS | Operating System | Software managing hardware and system resources. |
| PaaS / SaaS | Platform as a Service / Software as a Service | Cloud-managed runtime platform / complete hosted application. |
| p95 | 95th percentile | Value at or below which 95% of measurements fall. |
| PSU / UPS | Power Supply Unit / Uninterruptible Power Supply | Converts/distributes power / provides temporary backup power. |
| RAM | Random Access Memory | Fast volatile working memory. |
| RAID | Redundant Array of Independent Disks | Combines drives for performance/capacity/fault tolerance; not backup. |
| RPO / RTO | Recovery Point Objective / Recovery Time Objective | Acceptable data-loss window / target recovery duration. |
| RBAC | Role-Based Access Control | Permissions assigned through roles. |
| SLI / SLO / SLA | Service Level Indicator / Objective / Agreement | Measurement / target / external commitment. |
| SSH | Secure Shell | Encrypted protocol for remote shell and related access. |
| TCP / UDP | Transmission Control Protocol / User Datagram Protocol | Ordered reliable byte stream / connectionless datagram transport. |
| TLS | Transport Layer Security | Cryptographic protocol for peer authentication and channel protection. |
| TTL | Time to Live | Cache lifetime for DNS data; also a hop limit concept in IP. |
| VM | Virtual Machine | Isolated virtual computer with a guest OS. |
| VLAN | Virtual Local Area Network | Logical Layer-2 network segmentation. |
| ZT / ZTA | Zero Trust / Zero Trust Architecture | Resource-focused access model without implicit trust from location alone. |

## Cách học acronym

Với mỗi thuật ngữ, ghi: **full form → layer/category → nhiệm vụ → một kiểu lỗi → một cách kiểm tra/control**. Ví dụ: `DNS → application support service → phân giải tên → answer cũ/sai → kiểm tra resolver answer và TTL`.
