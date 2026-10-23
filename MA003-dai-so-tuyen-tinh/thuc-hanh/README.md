# MA003 — Gauss với phân số chính xác

```console
python MA003-dai-so-tuyen-tinh/thuc-hanh/gauss.py
```

Chạy từ gốc bộ học liệu. Python 3.8+, thư viện chuẩn `fractions`. Ba ví dụ gồm duy nhất (1,2), vô số nghiệm và vô nghiệm. Script trả RREF, rank của ma trận hệ số, cột pivot/biến tự do, nghiệm riêng và cơ sở kernel nếu hệ có nghiệm.

Để thử hệ khác, import `solve` hoặc sửa danh sách ví dụ bằng bản sao của bạn. Input là ma trận mở rộng, cột cuối là b. Dùng số nguyên hoặc chuỗi `'1/3'` cho phân số; không dùng float khi muốn biểu diễn thập phân/phân số chính xác theo ý định.

## Việc phải tự làm

1. Giải tay bài1,2,3 trong tập bài tập, ghi từng phép biến đổi hàng.
2. Kiểm tra RREF bằng script; với hệ có nghiệm, thế nghiệm riêng vào Ax=b.
3. Với từng vector cơ sở kernel, kiểm tra Av=0 và số vector bằng số ẩn−rank.
4. Thử hệ cần đổi hàng đầu, hệ nhiều phương trình hơn ẩn, hệ tất cả hệ số0 và vế phải0/khác0.
5. Giải thích vì sao tập nghiệm dạng x0+ker(A) và vì sao vô nghiệm thì không có x0.

Script chỉ tính cho hệ số hữu tỉ, không biện luận tham số ký hiệu, không xử lý số vô tỉ và không tối ưu cho ma trận lớn. Khi biện luận a, phải xét riêng giá trị làm pivot bằng0 trên giấy. Phần mềm không thay chứng minh điều kiện của tham số.
