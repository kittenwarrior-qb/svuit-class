# MA003 — Kiến thức đại số tuyến tính

Các ví dụ dùng trường số thực trừ khi nói khác. Ký hiệu vector là cột; A có m hàng, n cột thì A: R^n→R^m. Ghi kích thước trước phép tính giúp tránh nhiều lỗi.

## 1. Hệ phương trình tuyến tính

Hệ `Ax=b` có nghiệm khi b thuộc không gian sinh bởi các cột A. Ma trận mở rộng `[A|b]` biểu diễn đồng thời hệ số và vế phải. Ba phép biến đổi hàng sơ cấp giữ tập nghiệm: đổi hai hàng; nhân một hàng với số khác 0; cộng bội một hàng vào hàng khác.

Gauss đưa về dạng bậc thang rồi thế lùi; Gauss–Jordan đưa tiếp về RREF. Pivot là phần tử dẫn đầu hàng khác 0; cột không có pivot tương ứng biến tự do. Hạng = số pivot, không đếm cột vế phải như cột ẩn.

Định lý Rouché–Capelli: hệ có nghiệm khi rank(A)=rank([A|b]). Nếu bằng n thì nghiệm duy nhất; nếu nhỏ hơn n thì có n−rank(A) biến tự do và vô số nghiệm trên R. Hàng `[0 ... 0 | c]`, c≠0 chứng minh vô nghiệm.

### Ví dụ giải từng bước

`x+2y=5`, `3x+4y=11`. Lấy R2←R2−3R1 được `−2y=−4`; y=2, x=1. RREF là `[[1,0|1],[0,1|2]]`. Kiểm tra vào cả hai phương trình: 1+4=5; 3+8=11.

Với `x+y+z=2`, `2x+2y+2z=4`, chỉ có một hàng độc lập. Đặt y=s,z=t: `(x,y,z)=(2,0,0)+s(−1,1,0)+t(−1,0,1)`. Đây là không gian affine; vì vế phải khác 0, tập nghiệm nói chung không là không gian con. Hệ thuần nhất Ax=0 luôn có nghiệm 0 và tập nghiệm là kernel, một không gian con.

## 2. Phép toán ma trận

Nếu A m×n, B n×p thì AB m×p với `(AB)ij=Σk Aik Bkj`. Nhân không giao hoán nói chung. `A+B` chỉ khi cùng kích thước. `A^T` đổi hàng/cột; `(AB)^T=B^T A^T`. I là đơn vị, 0 là ma trận không theo kích thước.

Ví dụ A=`[[1,2],[3,4]]`, B=`[[0,1],[1,0]]`: AB=`[[2,1],[4,3]]`, BA=`[[3,4],[1,2]]`, cho thấy AB≠BA. Không rút gọn AB=AC thành B=C nếu chưa biết A khả nghịch hoặc điều kiện tương ứng.

Ma trận vuông A khả nghịch nếu có A^-1 sao cho AA^-1=A^-1A=I. Có thể tìm bằng `[A|I]→[I|A^-1]` nếu đủ pivot; không cần tính nghịch đảo để giải mọi hệ. Với A 2×2, det=ad−bc≠0 thì A^-1=(1/det)`[[d,−b],[−c,a]]`.

Các điều tương đương với A n×n khả nghịch: det(A)≠0; rank(A)=n; Ax=0 chỉ có nghiệm 0; cột A là cơ sở R^n; Ax=b có đúng một nghiệm với mọi b. `(AB)^-1=B^-1A^-1` nếu cả hai khả nghịch.

## 3. Định thức

Định thức gán số cho ma trận vuông, đo hệ số thể tích có dấu của ánh xạ. det=0 khi các cột phụ thuộc. Ma trận tam giác có det bằng tích đường chéo; det(AB)=det(A)det(B); det(A^T)=det(A).

Biến đổi hàng: đổi hai hàng làm đổi dấu; nhân một hàng với k làm det nhân k; cộng bội hàng khác giữ det. Nhân **toàn ma trận n×n** với k làm det nhân k^n, không chỉ k. Theo dõi các hệ số khi dùng khử để tính định thức.

Khai triển theo hàng/cột dùng cofactor `Cij=(−1)^(i+j) det(Mij)`. Chọn hàng/cột nhiều 0 để giảm việc. Quy tắc đường chéo Sarrus chỉ cho 3×3, không mở rộng trực tiếp lên 4×4.

Cramer cho hệ vuông det(A)≠0: xi=det(Ai)/det(A), Ai thay cột i bằng b. Nếu det(A)=0, Cramer không kết luận nghiệm duy nhất; dùng hạng/khử để biện luận. Máy tính số thường giải hệ bằng phân rã thay vì tính nhiều định thức.

## 4. Không gian vector và không gian con

Không gian vector trên R có phép cộng và nhân vô hướng thỏa các tiên đề. Ví dụ R^n, đa thức bậc không quá n, ma trận cùng kích thước. Không gian con W⊆V phải không rỗng và đóng dưới cộng/nhân vô hướng; cách kiểm tra gọn: 0∈W và với u,v∈W, a,b∈R thì au+bv∈W.

Ví dụ W={(x,y,z):x+y+z=0} là kernel của ánh xạ tuyến tính nên là không gian con. Mặt phẳng x+y+z=1 không chứa 0 nên không là không gian con. Tập vector có x≥0 không đóng dưới nhân vô hướng âm. Hợp hai không gian con không luôn là không gian con; giao luôn là không gian con.

Span(v1,...,vk) là tập mọi tổ hợp tuyến tính Σci vi, cũng là không gian con nhỏ nhất chứa các vector đó. Muốn kiểm tra w thuộc span, giải ma trận có các vi làm cột với vế phải w. Không chỉ so sánh số vector với số chiều.

## 5. Độc lập tuyến tính, cơ sở và tọa độ

v1,...,vk độc lập nếu Σci vi=0 chỉ có nghiệm mọi ci=0. Nếu có nghiệm hệ số không đồng thời 0 thì phụ thuộc. Có vector 0 trong tập thì phụ thuộc; hơn n vector trong R^n luôn phụ thuộc, nhưng ít hơn n vẫn có thể phụ thuộc.

Cơ sở B là tập vừa độc lập vừa sinh không gian. Mọi vector có biểu diễn duy nhất theo B; số vector trong cơ sở là dimension. Tọa độ [v]B là các hệ số biểu diễn, không mặc định bằng tọa độ chuẩn.

Ví dụ B={(1,1),(1,−1)}, v=(4,2). Giải c1+c2=4, c1−c2=2 được (c1,c2)=(3,1), nên [v]B=(3,1). Ma trận P có cột là các vector B trong tọa độ chuẩn: v=P[v]B; [v]B=P^-1v.

Tìm cơ sở column space A: khử A, chọn **cột pivot từ ma trận gốc**. Các hàng khác 0 của RREF tạo cơ sở row space; null space tìm bằng giải Ax=0. Biến đổi hàng thay đổi column space nói chung, nên không lấy cột RREF làm cơ sở column space gốc.

Rank-nullity: rank(A)+nullity(A)=n, số cột A. Row rank bằng column rank. Nếu U,W hữu hạn chiều: dim(U+W)=dim(U)+dim(W)−dim(U∩W). Không cộng chiều mà quên phần giao.

## 6. Ánh xạ tuyến tính

T:V→W tuyến tính khi T(au+bv)=aT(u)+bT(v). T(0)=0 là điều kiện cần nhưng chưa đủ. Ví dụ T(x,y)=(x+y,2x) tuyến tính; F(x,y)=(x+1,y) không vì F(0)≠0; G(x)=x² có G(0)=0 nhưng không cộng tính trên R.

Kernel={v:T(v)=0}; image={T(v):v∈V}. T đơn ánh khi kernel={0}. T toàn ánh khi image=W. Nếu dim(V)=dim(W)<∞, đơn ánh tương đương toàn ánh; khi khác chiều phải kiểm tra riêng.

Ma trận biểu diễn chuẩn của T:R^n→R^m có cột j=T(ej). Ví dụ T(x,y,z)=(x+y,y+z): A=`[[1,1,0],[0,1,1]]`. Kernel giải x=−y,z=−y, nên span{(−1,1,−1)}, dimension1. Image=R² vì rank2; rank+nullity=3 đúng bằng dimension miền xác định.

Với cơ sở B của miền và C của đích, `[T(v)]C = [T]C←B [v]B`; cột j là `[T(bj)]C`. Khi toán tử T:V→V và đổi cơ sở bằng P (tọa độ cũ=P×tọa độ mới), ma trận mới B=P^-1AP. Kiểm tra chiều và ý nghĩa P, đừng học công thức đổi cơ sở không có quy ước.

## 7. Trị riêng và chéo hóa — mở rộng

Cần kiểm tra đề cương G12 trước khi ưu tiên. Vector v≠0 là vector riêng nếu Av=λv. Tìm λ từ det(A−λI)=0, rồi giải (A−λI)v=0. Giá trị riêng có thể 0; vector riêng không được 0. Tổng trị riêng theo bội đại số bằng trace và tích bằng det khi xét đủ nghiệm trên trường phù hợp.

A chéo hóa được nếu có n vector riêng độc lập: A=PDP^-1 với cột P là vector riêng theo đúng thứ tự các λ trên D. Có n trị riêng phân biệt là điều kiện đủ; có trị riêng lặp không tự chứng minh không chéo hóa. Cần so bội hình học và đại số cho từng λ.

Ví dụ A=`[[2,1],[0,3]]`: λ=2 có v=(1,0), λ=3 có v=(1,1). P=`[[1,1],[0,1]]`, D=diag(2,3), kiểm tra AP=PD. Ma trận `[[1,1],[0,1]]` có λ=1 lặp nhưng eigenspace chỉ dimension1 nên không chéo hóa trên R.

## 8. Tích vô hướng, trực giao, projection — mở rộng

Trên R^n, dot(u,v)=Σui vi, norm ||v||=sqrt(v·v). Trực giao khi u·v=0. Tập vector khác 0 đôi một trực giao là độc lập. Chuẩn hóa q=v/||v|| chỉ khi v≠0.

Projection lên một vector khác 0: proj_u(v)=(v·u)/(u·u) u. Projection lên không gian có cơ sở trực chuẩn q1,...,qk là Σ(v·qi)qi. Không dùng công thức cộng này với cơ sở chưa trực chuẩn.

Gram–Schmidt: w1=v1; wk=vk−Σj<k proj_wj(vk); nếu wk≠0 thì chuẩn hóa. Nếu xuất hiện 0 trong số học chính xác thì đầu vào có phụ thuộc; với float gần 0 cần xét ổn định số và dung sai.

Ví dụ chiếu v=(2,0) lên u=(1,1) được (1,1); phần dư (1,−1) trực giao u. Khoảng cách tới đường sinh bởi u bằng norm phần dư =sqrt2.

## 9. Bình phương tối thiểu — mở rộng

Khi Ax=b vô nghiệm, tìm x tối thiểu ||Ax−b||². Điều kiện chuẩn A^T A x=A^T b. Nếu cột A độc lập thì A^T A khả nghịch và nghiệm duy nhất; nếu không thì có thể nhiều nghiệm. Tính số thường dùng QR/SVD để tránh vấn đề điều kiện số của normal equations.

Ví dụ fit y=a+bt cho (0,1),(1,2),(2,2): A=`[[1,0],[1,1],[1,2]]`, b=(1,2,2). A^T A=`[[3,3],[3,5]]`, A^T b=(5,6), giải a=7/6,b=1/2. Sai số là tổng bình phương phần dư, không yêu cầu đường đi qua cả ba điểm.

## 10. Trình bày lời giải và tự kiểm tra

Ghi miền/điều kiện tham số, từng phép biến đổi quan trọng và kết luận bằng lời. Kiểm tra hệ bằng thế nghiệm, nghịch đảo bằng nhân I, cơ sở bằng độc lập+sinh, ánh xạ bằng tác động lên cơ sở, trị riêng bằng Av=λv. Đáp số từ phần mềm giúp đối chiếu, không thay chứng minh.
