# IE005 — Bản đồ ngành và phương pháp học

> [!TIP]
> **Nhớ nhanh:** CNTT giải quyết nhu cầu bằng **con người + quy trình + dữ liệu + công nghệ**. Sản phẩm đi theo vòng lặp **hiểu vấn đề → xây → kiểm thử → vận hành → cải tiến**. Luôn kiểm chứng nguồn, bảo vệ dữ liệu và ghi nhận phần tham khảo.

### 5 ý cốt lõi

- Một hệ thống cần công nghệ, dữ liệu, con người **và** quy trình.
- Làm rõ vấn đề và tiêu chí đo được trước khi chọn công cụ.
- Internet là hạ tầng; Web là một dịch vụ trên Internet.
- Kiểm thử giảm rủi ro, không chứng minh đã hết mọi lỗi.
- Ghi nguồn, bảo vệ dữ liệu và tự kiểm chứng đầu ra AI.

<details><summary>Mở phần giải thích và ví dụ</summary>

## 1. CNTT giải quyết vấn đề gì?

Một hệ thống thông tin phối hợp con người, quy trình, dữ liệu, phần mềm và hạ tầng. CNTT thiết kế, xây dựng, triển khai và vận hành những thành phần đó để đạt mục tiêu: ghi nhận giao dịch đúng, hỗ trợ quyết định, kết nối người dùng, tự động hóa công việc.

Ví dụ thư viện: độc giả tìm sách trên giao diện; ứng dụng xử lý quy tắc mượn; CSDL lưu sách và lượt mượn; hạ tầng giữ dịch vụ hoạt động; nhân viên xử lý mất sách/ngoại lệ. Thành công cần cả phần mềm lẫn quy trình và dữ liệu tốt.

Dữ liệu là biểu diễn sự kiện/giá trị. Thông tin là dữ liệu được tổ chức và đặt trong ngữ cảnh. Tri thức giúp giải thích và ra quyết định. Số `85` chưa đủ nghĩa; `85% yêu cầu trả lời dưới 1 giây trong tuần này` đã có ngữ cảnh và phương pháp đo.

## 2. Các nhóm kiến thức liên hệ nhau

| Nhóm | Câu hỏi trung tâm | Ví dụ |
|---|---|---|
| Khoa học máy tính | Bài toán giải được và hiệu quả đến đâu? | Thuật toán tìm đường, độ phức tạp |
| Kỹ thuật phần mềm | Xây và duy trì sản phẩm đáng tin thế nào? | Yêu cầu, thiết kế, kiểm thử |
| Hệ thống thông tin | Dữ liệu/quy trình hỗ trợ tổ chức thế nào? | Hệ quản trị, phân tích nghiệp vụ |
| Mạng và hệ thống | Kết nối và vận hành dịch vụ ra sao? | Routing, Linux, cloud |
| An toàn thông tin | Bảo vệ tài sản trước rủi ro thế nào? | Phân quyền, phân tích mối đe dọa |
| Khoa học dữ liệu / AI | Học mẫu và dự đoán từ dữ liệu ra sao? | Thống kê, mô hình, đánh giá |
| Kỹ thuật máy tính | Kết hợp phần cứng và phần mềm thế nào? | Vi xử lý, hệ nhúng |

Ranh giới không tuyệt đối: sản phẩm AI vẫn cần dữ liệu, phần mềm, hạ tầng và bảo mật. Không chọn ngành chỉ vì một công cụ đang nổi; chọn vấn đề muốn giải, cách làm việc phù hợp và nền tảng sẵn sàng luyện.

## 3. Phần cứng, phần mềm, mạng, dữ liệu

Phần cứng thi hành lệnh; OS phân phối tài nguyên; ứng dụng biểu diễn nghiệp vụ; mạng trao đổi thông điệp; CSDL quản lý dữ liệu có cấu trúc. API là hợp đồng cho phần mềm tương tác, gồm đầu vào, đầu ra và cách báo lỗi. Giao diện đẹp chưa đảm bảo API đúng hay dữ liệu an toàn.

Lập trình là mô tả cách xử lý bài toán; thuật toán là quy trình giải; cấu trúc dữ liệu là cách tổ chức dữ liệu; chương trình là một hiện thực cụ thể. Độ phức tạp O(n) mô tả xu hướng theo kích thước đầu vào với mô hình giả định, không phải số giây cố định.

Internet là mạng của các mạng; Web là một dịch vụ hoạt động trên Internet. Cloud cung cấp tài nguyên/dịch vụ theo mô hình sử dụng; không phải mọi phần mềm có kết nối Internet đều là cloud. AI tạo ra đầu ra cần đánh giá; giọng văn tự tin không phải bằng chứng đúng.

## 4. Vòng đời phát triển và vận hành

Chu trình phổ biến: hiểu vấn đề → yêu cầu → thiết kế → hiện thực → kiểm thử → triển khai → vận hành → phản hồi. Thực tế lặp nhiều vòng. Yêu cầu chức năng mô tả hệ thống làm gì; phi chức năng mô tả chất lượng/ràng buộc như latency, availability, khả năng tiếp cận, bảo mật.

Ví dụ yêu cầu mơ hồ: “tìm sách nhanh”. Yêu cầu đo được: “với bộ dữ liệu và tải giả định đã nêu, 95% truy vấn tìm sách trả dưới 2 giây”. Tiêu chí chấp nhận cần điều kiện đo, không chỉ một con số đẹp.

Kiểm thử đơn vị kiểm tra thành phần nhỏ; tích hợp kiểm tra phối hợp; hệ thống kiểm tra toàn bộ; nghiệm thu kiểm tra yêu cầu người dùng. Review và kiểm thử phát hiện lỗi, không chứng minh chương trình tuyệt đối không còn lỗi. Version control giữ lịch sử và hỗ trợ cộng tác, không thay thế backup cho mọi loại dữ liệu.

## 5. Vai trò nghề nghiệp

Developer viết và bảo trì phần mềm; QA/test engineer thiết kế kiểm tra và giúp kiểm soát chất lượng; business analyst làm rõ nhu cầu/quy trình; data engineer xây pipeline dữ liệu; data analyst phân tích và truyền đạt; system/network engineer triển khai/vận hành; security engineer bảo vệ và đánh giá rủi ro; UX designer nghiên cứu và thiết kế trải nghiệm.

Tên vị trí thay đổi theo tổ chức. Đọc trách nhiệm, kỹ năng, mức độ tự chủ và sản phẩm công việc, không chỉ tên. Người mới nên có năng lực nền: tư duy logic, một ngôn ngữ lập trình, SQL, Git, mạng/OS cơ bản, tiếng Anh đọc hiểu, viết báo cáo và hợp tác.

Bằng chứng năng lực tốt: bài làm có yêu cầu rõ, mã chạy được, kiểm tra hợp lý, README hướng dẫn và giải thích quyết định. Số lượng chứng chỉ hoặc repository không tự thay thế khả năng giải thích và thực hiện công việc.

## 6. Tự học và nghiên cứu thông tin

Trước buổi học: đọc mục tiêu, nhận diện 3 từ chưa hiểu. Trong buổi: ghi định nghĩa, ví dụ và câu hỏi. Sau buổi: đóng tài liệu, tự nhớ lại, giải bài rồi kiểm tra. Active recall buộc nhớ lại; spaced repetition phân tán lần ôn; deliberate practice tập trung vào lỗi có phản hồi.

Đọc nguồn theo thứ tự: đề cương/slide lớp → giáo trình và tài liệu tác giả → tài liệu chuẩn/hãng → bài giải cộng đồng để so sánh. Với mỗi kết luận hỏi: ai viết, khi nào, dựa trên bằng chứng nào, có giới hạn gì? Một bài blog có thể minh họa tốt nhưng sai phiên bản hoặc thiếu giả định.

Khi dùng AI: chia nhỏ câu hỏi, cung cấp ngữ cảnh, kiểm tra nguồn, chạy ví dụ và tự giải thích. Không đưa dữ liệu cá nhân/secret vào công cụ khi chưa được phép. Tôn trọng quy định môn học về việc dùng AI và ghi nhận hỗ trợ nếu được yêu cầu.

## 7. Đạo đức và trách nhiệm nghề nghiệp

Ưu tiên lợi ích của người chịu tác động; tránh gây hại; trung thực về năng lực và giới hạn; tôn trọng quyền riêng tư, công sức và bản quyền; chỉ truy cập tài nguyên được phép. Khi phát hiện lỗi, báo qua kênh phù hợp, cung cấp cách tái hiện tối thiểu và tránh làm lộ dữ liệu.

Tình huống dữ liệu: một CSV chứa tên, số điện thoại và điểm không nên đưa vào repo học tập công khai. Dùng dữ liệu giả, giảm trường dữ liệu và giới hạn quyền. Xóa tên chưa chắc đã ẩn danh nếu nhiều trường vẫn nhận diện được người.

Tình huống học thuật: tham khảo thuật toán không đồng nghĩa được chép lời giải nộp dưới tên mình. Ghi nguồn, phân biệt trích dẫn và phần tự làm, tuân thủ quy định giảng viên. Đây là nguyên tắc học tập; câu hỏi pháp lý cụ thể cần đối chiếu quy định hiện hành của tổ chức.

## 8. Làm việc nhóm và trình bày

Chia việc thành đầu ra kiểm chứng được, có người phụ trách và hạn hoàn thành. Issue tốt có bối cảnh, kỳ vọng, tiêu chí đạt và phụ thuộc. Họp ngắn tập trung vào tiến độ, trở ngại và quyết định cần chốt; ghi quyết định để tránh hiểu khác nhau.

Feedback mô tả hành vi/sản phẩm và ảnh hưởng, kèm cách cải thiện. Ví dụ “README thiếu bước tạo CSDL nên người mới không chạy được” hữu ích hơn “làm tài liệu tệ”. Khi bất đồng kỹ thuật, so phương án bằng yêu cầu, bằng chứng và chi phí thay đổi.

Báo cáo: vấn đề → mục tiêu → phương pháp → kết quả → giới hạn → nguồn. Slide một thông điệp chính mỗi trang, biểu đồ có đơn vị và nguồn, demo có cách tái hiện. Kết luận phải theo kết quả, không theo kỳ vọng ban đầu.

## 9. Lập kế hoạch năng lực

Chọn mục tiêu vừa sức trong 8–12 tuần, ghi rõ sản phẩm, thước đo và thời gian. Ví dụ “xây ứng dụng thư viện nhỏ có 3 bảng, 5 truy vấn, kiểm tra dữ liệu và hướng dẫn chạy” cụ thể hơn “học hết backend”.

Đánh giá hàng tuần: làm được gì không cần nhìn hướng dẫn, lỗi nào lặp, bằng chứng nào mới và nên đổi điều gì. Học rộng để hiểu hệ thống, học sâu một phần để tạo sản phẩm. Kế hoạch được phép đổi khi có bằng chứng, không cần khóa cứng vào một nghề ngay buổi đầu.

</details>
