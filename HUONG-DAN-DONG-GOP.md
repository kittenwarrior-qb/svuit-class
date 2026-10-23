# Thêm và cập nhật học liệu

## Quy ước

Tên file không dấu, nội dung UTF-8 có dấu. Mỗi ghi chú có tên chủ đề, định nghĩa, ví dụ, lỗi thường gặp và nguồn. Tài liệu gốc phải có tác giả, URL, ngày truy cập và ghi rõ được phép chia sẻ hay chỉ lưu cá nhân.

Tạo folder `bai-lam/` trong môn cho lời giải của bạn; dùng `ket-qua-ca-nhan/` nếu có thông tin riêng. Tách đề và lời giải để luyện nhớ chủ động. Không ghi thông tin đăng nhập trong notebook, mã nguồn hoặc ảnh chụp màn hình.

## Đối chiếu sau mỗi buổi

1. Ghi chủ đề giảng viên dạy và việc phải làm trước buổi sau.
2. Sửa ghi chú theo định nghĩa/ký hiệu dùng trên lớp; giữ nguồn và lý do sửa.
3. Thêm bài tập còn sai vào sổ lỗi: lỗi → cách sửa → bài tương tự → ngày làm lại.
4. Chạy `python scripts/kiem_tra.py` tại gốc bộ tài liệu.

## Git thường dùng

```console
git status
git diff
git add duong-dan-tep-da-kiem-tra
git commit -m "docs: bo sung bai tap he dieu hanh"
git push
```

Xem `git status` trước khi stage. Chỉ stage tài liệu cần chia sẻ; `git add .` có thể vô tình thêm dữ liệu cá nhân khi quy tắc ignore thay đổi. Nếu muốn cộng tác, tạo branch, push branch và mở pull request.
