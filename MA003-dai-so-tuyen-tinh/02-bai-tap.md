# MA003 — Bài tập tự soạn và lời giải

## Đề bài

1. Giải x+2y=5, 3x+4y=11 bằng Gauss; kiểm tra nghiệm.
2. Giải hệ x+y+z=2, 2x+2y+2z=4; viết dạng vector nghiệm.
3. Biện luận theo a: x+y=1, 2x+ay=3.
4. Với A=[[1,2],[3,4]], tìm det và nghịch đảo.
5. Tính det của [[1,2,3],[0,4,5],[0,0,6]]. Nếu nhân hàng 1 với 3 và đổi hàng 2/3, det mới là gì?
6. Kiểm tra W={(x,y,z):x+y+z=0} là không gian con và tìm cơ sở.
7. v1=(1,0,1),v2=(0,1,1),v3=(1,1,2) độc lập không? Tìm cơ sở span.
8. Với B={(1,1),(1,−1)}, tìm tọa độ của (4,2).
9. Với A=[[1,2,3],[2,4,6]], tìm rank, cơ sở kernel và image.
10. T(x,y,z)=(x+y,y+z): tìm ma trận, kernel/image và kết luận đơn/toàn ánh.
11. Tìm ma trận T(x,y)=(2x,3y) theo B={(1,1),(1,−1)} ở cả miền/đích.
12. Cho U=span{e1,e2}, W=span{e2,e3} trong R³. Tính chiều tổng và giao.
13. Mở rộng: trị riêng/vector riêng của [[2,1],[0,3]] và chéo hóa.
14. Mở rộng: chiếu (2,0) lên span{(1,1)} và tính khoảng cách.
15. Mở rộng: fit y=a+bt cho (0,1),(1,2),(2,2) bằng bình phương tối thiểu.

## Lời giải

1. R2−3R1 cho −2y=−4; y=2,x=1. Thế vào cho 5 và11 đúng.
2. R2−2R1 là hàng0; y=s,z=t, x=2−s−t. Dạng vector (2,0,0)+s(−1,1,0)+t(−1,0,1). Hai tham số tự do.
3. R2−2R1 cho (a−2)y=1. a≠2: y=1/(a−2), x=(a−3)/(a−2). a=2: 0=1, vô nghiệm. Không có trường hợp vô số nghiệm.
4. det=4−6=−2; A^-1=[[-2,1],[3/2,−1/2]]. Nhân lại A×A^-1=I để kiểm tra.
5. det=1×4×6=24. Nhân một hàng3 và đổi hai hàng làm det mới=−72; không nhầm nhân toàn ma trận với nhân một hàng.
6. 0 thuộc W; tổ hợp tuyến tính hai vector có tổng tọa độ0 vẫn có tổng0. Viết x=−y−z được cơ sở {(-1,1,0),(-1,0,1)}; hai vector độc lập và sinh W, dim2.
7. v3=v1+v2 nên phụ thuộc; {v1,v2} độc lập vì tọa độ thứ1/2 buộc hệ số0. Đó là một cơ sở span, dimension2.
8. Giải c1+c2=4,c1−c2=2 → [v]B=(3,1).
9. rank1. Ax=0 tương đương x1+2x2+3x3=0; kernel=span{(-2,1,0),(-3,0,1)}. Image=span{(1,2)} lấy từ cột gốc. rank1+nullity2=3.
10. A=[[1,1,0],[0,1,1]], kernel span{(-1,1,-1)}, image R², không đơn ánh và có toàn ánh. Hai cột1/3 đã tạo cơ sở R².
11. T(b1)=(2,3) có tọa độ B=(5/2,−1/2); T(b2)=(2,−3) có tọa độ B=(−1/2,5/2). Ma trận là [[5/2,−1/2],[−1/2,5/2]]. Có thể kiểm tra P^-1 diag(2,3) P.
12. U∩W=span{e2}, dim1. U+W=R³, dim3=2+2−1.
13. det(A−λI)=(2−λ)(3−λ). Với2: y=0 nên chọn (1,0); với3: y=x nên chọn(1,1). P=[[1,1],[0,1]], D=[[2,0],[0,3]], AP=PD nên A=PDP^-1.
14. dot=2, u·u=2 nên projection=(1,1). Phần dư=(1,−1), khoảng cách=sqrt2.
15. Normal equations: 3a+3b=5,3a+5b=6; b=1/2,a=7/6. Phần dư y−ŷ=(-1/6,1/3,-1/6); SSE=1/6. Kiểm tra A^T residual=0.

## Bài tự luyện thêm (chưa cho đáp số)

Thay vế phải câu3 thành2; tìm cơ sở không gian x−2y+z=0; tìm null space ma trận3×4 có rank2; dựng hai ánh xạ có cùng kernel nhưng khác image; tìm ví dụ hai ma trận AB≠BA; chứng minh hợp hai đường thẳng qua0 thường không là không gian con. Hãy kiểm tra bằng định nghĩa thay vì chỉ thử số.
