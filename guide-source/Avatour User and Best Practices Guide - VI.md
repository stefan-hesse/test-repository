# Avatour User and Best Practices Guide

## 1. Dành cho tất cả người dùng Avatour {#for-all-avatour-users}

Nếu bạn là người mới sử dụng Avatour, các tài liệu sau đây sẽ cung cấp những thông tin giới thiệu hữu ích về nền tảng này và các tính năng của nó:

1. [Video "Cách thức hoạt động của Avatour"](https://avatour.com/how-it-works)  
Một bản tóm tắt ngắn gọn về các tính năng chính của Avatour và cách nền tảng này hỗ trợ hợp tác từ xa mang lại trải nghiệm đắm chìm.
2. [Câu hỏi thường gặp](https://avatour.com/faqs)  
Các câu trả lời cho những câu hỏi thường gặp.
3. [Thuật ngữ](https://avatour.com/glossary)  
Định nghĩa các thuật ngữ và khái niệm chính của Avatour thường được sử dụng.
4. Trang web  
Hãy đặc biệt tham khảo [Các tính năng của Avatour](https://avatour.com/features) cùng với các phần dành riêng cho Các trường hợp sử dụng và Ngành nghề để tìm hiểu cách Avatour có thể hỗ trợ các nhu cầu cụ thể của bạn.

## 2. Các loại người dùng Avatour  {#avatour-user-types}

### 2.1 Người tham dự cuộc họp (Không cần tài khoản)
Người dùng có thể tham gia cuộc họp mà không cần đăng ký tài khoản Avatour.
Ngoại lệ: Nếu người tổ chức đã giới hạn cuộc họp chỉ dành cho người dùng đã đăng ký — ví dụ: chỉ cho phép nhân viên nội bộ tham gia qua Đăng nhập một lần (SSO) — lời mời lịch sẽ thông báo rằng người tham gia phải đăng nhập để xác thực.

Người dùng truy cập cuộc họp như sau:

- Nhận lời mời lịch từ người tổ chức.
- Sử dụng liên kết cuộc họp trong lời mời để tham gia.
- Nhập mật khẩu cuộc họp nếu người chủ trì đã kích hoạt tính năng này.
- Người tham gia có thể tham gia mà không cần tài khoản Avatour trừ khi cuộc họp bị hạn chế và yêu cầu đăng nhập để xác thực.

#### 2.1.1 Người tham gia 

- Có thể tham gia và tương tác đầy đủ (webcam, micrô, trò chuyện và chức năng Trình bày).
- Tối đa 20 người tham gia tương tác cho mỗi cuộc họp.

#### 2.1.2 Người theo dõi

- Có thể xem cuộc họp và chỉ tham gia qua trò chuyện.
- Không thể chia sẻ video, sử dụng micrô, trình chiếu, phát/tạm dừng Tài nguyên hoặc chụp Ảnh chụp nhanh.
- Tối đa 10 Người xem cho mỗi cuộc họp.
- Cộng với Người tham gia, một cuộc họp có thể chứa tối đa 30 người tham dự.

### 2.2 Người dùng đã đăng ký

Người dùng đã đăng ký có tài khoản Avatour. Tài khoản được tạo theo một trong các cách sau:

- **Được quản trị viên mời:** Trong quá trình thiết lập ban đầu, Avatour sẽ thiết lập một **tenant chuyên dụng** cho tổ chức và tạo một hoặc nhiều **tài khoản quản trị viên**. Sau đó, các quản trị viên có thể **mời người dùng** trong tổ chức và phân công họ vào các **nhóm**, qua đó xác định vai trò của họ trên nền tảng (Khách, Người chủ trì hoặc Quản trị viên). Người dùng được mời sẽ nhận được một **liên kết đăng ký** để hoàn tất việc thiết lập tài khoản và đặt mật khẩu.  
- **Được người chủ trì mời:** Chủ nhà có thể thêm người dùng với tư cách là **người cộng tác có quyền chỉnh sửa** vào một Không gian làm việc. Việc này sẽ tiêu tốn một **giấy phép Chủ nhà** và đảm bảo người dùng có quyền truy cập ở cấp độ Chủ nhà.  
- **Tự động cấp quyền thông qua SSO (chỉ dành cho gói Enterprise/Business):** Tài khoản có thể được tạo tự động bởi IdP. Theo mặc định, các tài khoản được cấp quyền qua SSO sẽ được thêm vào **nhóm Khách**, trừ khi được ghi đè thông qua **bản đồ nhóm SAML**. Quản trị viên vẫn có thể mời người dùng và chỉ định tư cách thành viên nhóm trực tiếp ngay cả khi SSO được bật.

**Tóm tắt:**  

Người dùng đã đăng ký và tư cách thành viên nhóm của họ có thể được quản lý theo nhiều cách:

- **Quản lý bởi quản trị viên:** Một quản trị viên trong bảng điều khiển Avatour có thể tạo người dùng và gán họ vào các nhóm, từ đó xác định vai trò của họ trên nền tảng (Khách, Chủ nhà hoặc Quản trị viên).  
- **Cấp quyền SSO:** Đối với khách hàng gói Enterprise hoặc Business đã bật SSO, IdP có thể tự động cấp quyền cho các tài khoản và chỉ định tư cách thành viên nhóm, từ đó xác định vai trò của người dùng trên nền tảng.  
- **Người dùng được Chủ nhà mời:** Chủ nhà có thể mời người dùng khác làm cộng tác viên Biên tập viên cho các Không gian làm việc cụ thể. Việc gán vai trò cộng tác viên Biên tập viên sẽ tiêu tốn một giấy phép Chủ nhà.

**Thực hành tốt nhất được khuyến nghị (Khách hàng Enterprise):**  
Đối với các tổ chức dự kiến có số lượng lớn người dùng cần truy cập vào Avatour, nên **tích hợp Đăng nhập Một Lần (SSO)** và quản lý người dùng cùng tư cách thành viên nhóm từ **IdP**. Cách tiếp cận này giúp tối ưu hóa việc cấp quyền tài khoản, phân công nhóm và quản lý giấy phép, từ đó giảm bớt gánh nặng quản trị và đảm bảo kiểm soát truy cập nhất quán.

#### 2.2.1 Người dùng khách

- Được thêm vào **nhóm Khách**.  
- Có thể **xem Tài sản** trong các Không gian làm việc mà họ đã được thêm vào với tư cách là **người cộng tác ở vai trò Người xem**.  
- Không thể tạo không gian làm việc, tổ chức cuộc họp hoặc tải lên nội dung.  
- Các tài khoản Khách được cấp qua SSO **xác thực thông qua IdP**; không yêu cầu mật khẩu do Avatour quản lý.

---

#### 2.2.2 Người dùng có giấy phép (Truy cập Bảng điều khiển Web)

##### Người dùng Chủ trì (Nhóm: Chủ trì)

- Có thể tạo/quản lý Không gian làm việc, mời cộng tác viên vào không gian làm việc, **tổ chức các cuộc họp trực tiếp**, tải lên **Hình ảnh chụp nhanh**.  
- Có quyền truy cập vào **Bảng điều khiển Người tổ chức** và **Ứng dụng Điều hành** trên các camera 360° được hỗ trợ.  

##### Người dùng Quản trị (Nhóm: Admin)

- Bao gồm tất cả các tính năng của Người chủ trì cùng với quyền quản trị tài khoản đầy đủ.

**Các đặc quyền Quản trị bổ sung bao gồm:**

**Quản lý tài khoản**  

- Tạo người dùng mới và gán họ vào các nhóm.
- Đặt lại mật khẩu khi được quản lý bởi Avatour (không áp dụng khi SSO được kích hoạt). 
- Nâng cấp người dùng Khách lên thành Người chủ trì.  
- Vô hiệu hóa người dùng (tài khoản Quản trị viên phải được chuyển đổi thành Người chủ trì trước khi xóa).  
- Chuyển tài sản từ một người dùng Người chủ trì sang người dùng khác trong quá trình xóa.

**Cài đặt**  

- Cấu hình **cài đặt bảo mật toàn tổ chức** cho tài sản, không gian làm việc và các cuộc họp được tổ chức trên nền tảng (ví dụ: liệu Host có bắt buộc phải có mặt để bắt đầu cuộc họp hay không, liệu khuôn mặt có nên bị làm mờ trên tất cả video được tải lên nền tảng hay không).  
- Bật hoặc tắt **các tính năng AI** hoặc **chức năng ghi hình**.  
- Áp dụng nhận diện thương hiệu của công ty một cách nhất quán trên toàn nền tảng nếu đã cấu hình **tên miền tùy chỉnh**.
  

**Tài sản & Phân tích** 
 
- Xem tất cả Tài sản được tải lên bởi bất kỳ người dùng nào trong tổ chức.  
- Xem xét việc sử dụng nền tảng trong toàn tổ chức.

---

#### 2.2.3 Quyền của người cộng tác trong không gian làm việc

Quyền trong không gian làm việc xác định những việc người dùng có thể thực hiện **trong một không gian làm việc cụ thể**. Các quyền này tách biệt với tư cách thành viên nhóm ở cấp nền tảng (Khách, Người chủ trì, Quản trị viên).

- **Người cộng tác với quyền Chỉnh sửa:** Người dùng có quyền này có thể:
  - Quản lý Tài sản (tải lên, xóa, làm mờ khuôn mặt, tạo bản tóm tắt)  
  - Quản lý cài đặt cuộc họp (bật/tắt tính năng ghi âm, cho phép hoặc loại bỏ người tham gia)  
  - Lên lịch và chủ trì các cuộc họp trực tiếp  
  - Tạo báo cáo dựa trên các mẫu có sẵn  
  - Thêm hoặc xóa người cộng tác khỏi Không gian làm việc  

- **Người cộng tác ở vai trò Người xem:** Người dùng có quyền này chỉ có quyền truy cập đọc đối với Tài sản trong Không gian làm việc. Họ **không thể chỉnh sửa Tài sản, quản lý cuộc họp hoặc quản lý người cộng tác**, nhưng họ **có thể tạo Ghi chú trên Tài sản**. 
  
## 3. Đối với người tham gia cuộc họp từ xa và khách đến thăm không gian làm việc {#for-remote-meeting-participants-and-workspace-visitors}

Avatour cho phép người dùng hợp tác theo hai cách chính:

- **Tham gia cuộc họp Avatour (Hợp tác đồng bộ):**  
  Bạn có thể nhận được **lời mời qua lịch** để tham gia cuộc họp Avatour. Trong cuộc họp, các thành viên có thể thực hiện **chuyến tham quan địa điểm từ xa trực tiếp** hoặc cùng nhau xem xét các tài sản một cách đồng bộ.

- **Truy cập Không gian làm việc (Hợp tác không đồng bộ):**  
  Bạn cũng có thể được mời với tư cách là **người cộng tác trong Không gian làm việc** để xem xét các tài sản **theo cách không đồng bộ** (theo lịch trình của riêng bạn).

### 3.1 Cách tham gia cuộc họp Avatour và truy cập Không gian làm việc Avatour {#how-to-join-an-avatour-meeting-and-visit-an-avatour-workspace}
#### 3.1.1 Bất kỳ thiết bị "màn hình phẳng" nào có trình duyệt web {#any-flat-screen}
Bạn có thể tham gia cuộc họp Avatour từ **bất kỳ máy tính để bàn, máy tính xách tay, điện thoại thông minh hoặc máy tính bảng nào** bằng trình duyệt web.  

##### Tham gia cuộc họp Avatour

> **Lưu ý:** Để tham gia cuộc họp Avatour, bạn cần **cấp quyền sử dụng micrô**. Vui lòng chấp nhận mọi yêu cầu cấp quyền từ trình duyệt của bạn.

1. **Qua lời mời lịch (được khuyến nghị):**  
   - Thông thường, bạn sẽ nhận được một **lời mời lịch** kèm theo **liên kết tham gia trực tiếp** (ví dụ: `https://avatour.live/join?s=xxxxx`). 
 - Nhấp vào liên kết này sẽ tự động điền **mã cuộc họp gồm 5 ký tự** và đưa bạn vào cuộc họp.
   - **Yêu cầu xác thực:** Một số cuộc họp chỉ dành cho người dùng đã đăng ký. Trong trường hợp này, lời mời sẽ thông báo rằng bạn cần **đăng nhập để truy cập cuộc họp**. 
 - **Cuộc họp được bảo vệ bằng mật khẩu:** Một số cuộc họp có thể yêu cầu mật khẩu. Trong trường hợp đó, thư mời sẽ bao gồm mật khẩu mà bạn phải nhập để tham gia.

2. **Qua mã cuộc họp:** 
 - Nếu người tổ chức chia sẻ riêng một **mã cuộc họp gồm 5 ký tự**, hãy truy cập [https://avatour.live/join](https://avatour.live/join), nhập **tên** và **mã cuộc họp** của bạn, rồi tham gia cuộc họp.  
   - Nếu cuộc họp được **bảo vệ bằng mật khẩu**, hãy nhập mật khẩu do người chủ trì cung cấp. 
 - Nếu cuộc họp yêu cầu **xác thực**, bạn sẽ cần **đăng nhập bằng tài khoản Avatour của mình** trước khi tham gia.

> **Mẹo 1:** Nếu camera hoặc micrô của bạn không hoạt động, có thể chúng đang được ứng dụng khác sử dụng (ví dụ: Microsoft Teams hoặc Zoom). Hãy đóng tất cả các ứng dụng có thể đang sử dụng camera hoặc micrô của bạn, sau đó rời khỏi và tham gia lại cuộc họp Avatour.  

> **Mẹo 2:** Nếu bạn vẫn không thể tham gia cuộc họp, hãy thực hiện bài kiểm tra này: [https://avatour.live/test](https://avatour.live/test).  
> Bài kiểm tra này có thể xác định xem **tường lửa hoặc mạng công ty** của bạn có đang chặn truy cập hay không, đồng thời cung cấp thông tin để hướng dẫn các cuộc thảo luận với đội ngũ CNTT của bạn.  

> **Mẹo 3:** **Không** sử dụng ứng dụng Avatour trên iOS hoặc Android để tham gia cuộc họp. Các ứng dụng này chỉ cần thiết khi **phát trực tiếp cuộc họp từ camera Insta360**, vì những camera này không thể chạy phần mềm Avatour 360° trực tiếp và cần có điện thoại thông minh để hỗ trợ.

##### Truy cập Không gian làm việc Avatour (mà không tham gia Cuộc họp Avatour)

Bạn có thể truy cập Không gian làm việc theo các cách sau:

- **Không gian làm việc công khai:**  
  Nếu Không gian làm việc là công khai, bạn có thể truy cập liên kết trực tiếp — không cần đăng nhập.

- **Không gian làm việc có giới hạn:**  
  Nếu Không gian làm việc có giới hạn, bạn phải được thêm vào với tư cách là **người cộng tác** có quyền **Biên tập viên** hoặc **Người xem**.

  1. Khi bạn được thêm vào với tư cách cộng tác viên, bạn sẽ nhận được một **thông báo qua email** kèm theo liên kết đến Không gian làm việc.
  2. Nhấp vào liên kết trong email để mở Không gian làm việc. Nếu bạn chưa đăng nhập, hệ thống sẽ yêu cầu bạn **đăng nhập hoặc hoàn tất đăng ký**.
  3. Sau khi đăng nhập, Không gian làm việc sẽ tự động mở ra.

  Ngoài ra, bạn có thể đăng nhập tại [https://avatour.live/login](https://avatour.live/login) và truy cập Không gian làm việc từ **danh sách Không gian làm việc** của mình.

#### 3.1.2 Kính thực tế ảo {#vr-headset}
Bạn có thể tham gia cuộc họp và truy cập Workspace từ nhiều loại kính thực tế ảo tương thích của Meta và Pico. Để thực hiện điều này: 

1. Cài đặt ứng dụng Avatour của chúng tôi từ cửa hàng ứng dụng VR tương ứng: [Cách cài đặt ứng dụng Avatour VR](https://avatour.com/support/which-vr-headsets-can-i-use-with-avatour)
2. Mở ứng dụng của chúng tôi và nhập mã cuộc họp hoặc chọn một Không gian làm việc để tham gia cuộc họp. Để biết thêm thông tin về cách sử dụng ứng dụng VR của chúng tôi, hãy xem bài viết trong Cơ sở kiến thức [tại đây](https://avatour.com/support/what-features-are-available-to-vr-guests).

### 3.2 Công cụ hợp tác trong cuộc họp và Không gian làm việc {#meeting-tools}

Avatour cho phép hợp tác trong hai bối cảnh chính:

1. **Cuộc họp (đồng bộ):** Hợp tác theo thời gian thực với những người tham gia khác, bao gồm tham quan địa điểm trực tiếp hoặc cùng nhau xem lại các tài sản đã ghi lại.  
2. **Không gian làm việc (không đồng bộ):** Xem lại và tương tác với các tài sản theo lịch trình của riêng bạn, 24/7.

Các **công cụ hợp tác phần lớn tương tự nhau** giữa các cuộc họp và không gian làm việc, với một số khác biệt do bối cảnh đồng bộ so với không đồng bộ.

#### 3.2.1 Bố cục giao diện

Giao diện Avatour được tổ chức xoay quanh ba khu vực chính:

- **Bảng điều khiển bên trái** – Tài nguyên không gian làm việc và các công cụ hỗ trợ  
- **Khung trung tâm** – Khu vực xem chính cho video trực tiếp hoặc tài nguyên  
- **Bảng điều khiển bên phải** – Thông tin bối cảnh, chẳng hạn như người tham gia, cuộc họp hoặc trò chuyện  

Hầu hết các tương tác đều được khởi tạo từ **menu dưới cùng**.  
Khi nhấp vào một tùy chọn trong menu, một **bảng điều khiển bên** sẽ mở ra ở bên trái hoặc bên phải màn hình, trong khi **khung trung tâm** vẫn là khu vực hiển thị chính.

---
#### 3.2.2 Ví dụ về giao diện cuộc họp

Dưới đây là một ví dụ về giao diện trong một cuộc họp Avatour:

![Giao diện người dùng cuộc họp Avatour với Bảng tài nguyên, Khung vẽ trống và Bảng người tham gia](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-assets-blank-participants_pugprq.png)  
*Cuộc họp Avatour với Bảng tài nguyên (bên trái), Bảng vẽ (giữa) và Bảng người tham gia (bên phải)*

---

#### 3.2.3 Ví dụ về giao diện Không gian làm việc

Dưới đây là ví dụ về giao diện Không gian làm việc:

![Không gian làm việc Avatour với Bảng tài sản, Bảng vẽ trống và Bảng cuộc họp](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png)  
*Không gian làm việc Avatour với Bảng tài sản (bên trái), Bảng vẽ (giữa) và Bảng cuộc họp (bên phải)*

---

#### 3.2.4 Tổng quan về menu dưới cùng

Menu dưới cùng cung cấp quyền truy cập vào các điều khiển và bảng chính của giao diện:

**Menu dưới cùng của cuộc họp**  

![Menu dưới cùng của cuộc họp Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-bottom-menu_bflaor.png)  
*Menu dưới cùng của cuộc họp Avatour*

- **Tài nguyên** – Xem lại các tệp trong không gian làm việc, bao gồm video đã ghi, hình ảnh, ảnh chụp màn hình và tệp PDF. 
- **Trò chuyện** – Gửi tin nhắn cho tất cả người tham gia cuộc họp.  
- **Camera** – Bật hoặc tắt webcam của bạn.  
- **Micro** – Tắt tiếng hoặc bật tiếng cho chính mình.  
- **Trình chiếu** – Trình chiếu tài liệu, màn hình máy tính hoặc hình ảnh từ webcam (xem phần Trình chiếu bên dưới).  
- **Công cụ Người chủ trì** (chỉ dành cho người chủ trì):  
  - **Khóa Tập trung** – Khóa chế độ xem cho tất cả người tham gia.  
  - **Tắt tiếng Tất cả** – Tắt tiếng tất cả người tham gia.  
- **Bật Chế độ Toàn màn hình** – Chuyển tab cuộc họp sang chế độ toàn màn hình.  
- **Rời cuộc họp** – Rời khỏi cuộc họp.  
- **Bắt đầu ghi hình** – Sử dụng nút này để bắt đầu và dừng ghi hình thủ công trong cuộc họp. Ngoài ra, cuộc họp có thể được ghi hình tự động nếu tính năng **tự động bắt đầu ghi hình** được bật trong cài đặt không gian làm việc. Trong cả hai trường hợp, các bản ghi sẽ được lưu vào tài nguyên của không gian làm việc.
- **Bản đồ** – Mở hoặc đóng bảng điều khiển bản đồ cho các tài nguyên có đường đi GPS. Nhấp vào một vị trí sẽ chuyển đến điểm chính xác đó trong video. Bản đồ được cập nhật trực tiếp khi video đang phát.
- **Người tham gia** – Mở hoặc đóng bảng điều khiển người tham gia.  
- **Thông tin cuộc họp** – Xem mã cuộc họp, liên kết mời và truy cập các hướng dẫn liên quan.  

![Thông tin cuộc họp Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-info-side-pane_nx7dp4.png)  
*Bảng điều khiển bên Thông tin cuộc họp Avatour*

- **Cài đặt** – Điều chỉnh cài đặt ngôn ngữ, âm thanh và video. Đối với các cuộc họp video 360° trực tiếp, hãy sử dụng **Hiển thị tốc độ bit** để theo dõi số liệu kết nối.

> Mẹo: Gửi liên kết cuộc họp hoặc thêm liên kết đó vào mục lịch để mời người tham gia.

---

##### Menu Trình chiếu

Tùy chọn **Trình chiếu** trong menu dưới cùng của cuộc họp cho phép bạn chia sẻ nội dung với tất cả người tham gia.

- **Camera** – Chia sẻ camera của điện thoại thông minh/máy tính bảng. Tính năng này cũng có thể được sử dụng trong cuộc họp video 360° trực tiếp để hiển thị lớp phủ hình ảnh thứ hai nhằm phóng to hoặc làm nổi bật các chi tiết cụ thể. 
- **Màn hình máy tính** – Chia sẻ màn hình máy tính của bạn với tất cả người tham gia.  
- **Tài nguyên** – Trình chiếu một tài nguyên từ không gian làm việc. Khi chọn một tài nguyên, **Thanh công cụ Tài nguyên** sẽ mở ra, cung cấp các điều khiển phát lại và công cụ cộng tác dành riêng cho tài nguyên đang được trình chiếu.

##### Thanh công cụ Tài nguyên (Cuộc họp)

Khi trình chiếu một tài nguyên trong cuộc họp, **Thanh công cụ Tài nguyên** sẽ xuất hiện phía trên khung vẽ. Dưới đây là các công cụ và mục menu có sẵn khi <u>trình chiếu một tài nguyên trong cuộc họp</u> – được giải thích từ trái sang phải.

![Menu Avatour khi trình chiếu tài nguyên trong cuộc họp](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting_oflsr5.png) *Menu Avatour khi trình chiếu tài nguyên trong cuộc họp*


- **Dòng thời gian video / Thanh tiến trình** – Hiển thị tiến trình video kèm theo các ghi chú và chủ đề chính được trích xuất từ âm thanh. Nhấp vào một ghi chú hoặc chủ đề để chuyển đến thời điểm đó và mở ghi chú. Bao gồm các nút điều khiển **Phát / Tạm dừng**.   
- **Ảnh chụp nhanh** – Chụp ảnh 360° hoặc 2D từ tài sản.  
- **Đèn chiếu** – Làm nổi bật một khu vực cụ thể cho tất cả người tham gia trong các phiên trực tiếp.  
- **Hiển thị/Ẩn Góc nhìn (POV)** – Hiển thị hướng nhìn của từng người tham gia trong video 360°.  
- **Ghi chú** – Tạo ghi chú gắn với các thời điểm cụ thể trong tài sản. Ghi chú có thể được phân loại (Quan sát, Vấn đề, Hành động, Khuyến nghị), theo dõi theo trạng thái (Chưa giải quyết → Đang xử lý → Đã giải quyết) và chia sẻ qua liên kết trực tiếp.  

  ![Ghi chú Avatour và Bộ lọc ghi chú](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-note-and-filters_g181oc.png) *Ghi chú Avatour và Bộ lọc ghi chú*

- **Ghi chú từ lệnh thoại** – Đây là các vị trí giữ chỗ được tạo tự động khi bản ghi âm phát hiện các cụm từ như “chèn ghi chú”, “ghi chú” hoặc “tạo ghi chú”. Các ghi chú này xuất hiện trên dòng thời gian và cần được người dùng **định vị và hoàn thiện**. 

  ![Ghi chú Avatour - Được tạo bởi lệnh thoại](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-notes-voice-command-generated_ic5cu4.png) *Ghi chú Avatour - Được tạo bởi lệnh thoại*

- **Bảng ghi chú và tóm tắt** – Mở một bảng bên hiển thị tất cả các ghi chú, các chủ đề chính và bản tóm tắt cho tài sản đó. Nhấp vào một mục sẽ đưa bạn đến thời điểm đó trong video.  

  ![Tóm tắt điều hành tài sản Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-exec-summary_cqpqbs.png) *Tóm tắt chính của Avatour khi trình bày một tài sản trong cuộc họp*

  ![Các chủ đề của Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-topics_duuq1a.png) *Các chủ đề của Avatour khi trình bày một tài sản trong cuộc họp*

  Từ **Bảng điều khiển bên**, bạn có thể **in báo cáo tài sản** hoặc **tải xuống dưới dạng TXT hoặc CSV**. Báo cáo có thể bao gồm ghi chú, các chủ đề do AI tạo ra và bản ghi chép đầy đủ. Bạn cũng có thể **chọn các yếu tố cần bao gồm** trước khi xuất.  

  ![Menu in báo cáo tài sản Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-report-print-menus_kn0syn.png)  
  *Menu in / tải xuống báo cáo tài sản Avatour*  

  ![Lựa chọn thành phần báo cáo tài sản Avatour để in](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-report-element-selection_ud8c5k.png)  
  *Menu Lựa chọn thành phần báo cáo tài sản Avatour*

- **Chia sẻ liên kết** – Chia sẻ liên kết đến một ghi chú hoặc cảnh cụ thể trong tài sản.  
- **Phụ đề (CC)** – Hiển thị bản chép lời trên màn hình trong khi phát video.

##### Thanh công cụ tài nguyên (Không gian làm việc)

Khi xem xét một tài nguyên trong không gian làm việc, thanh công cụ có giao diện tương tự nhưng được tối ưu hóa cho việc sử dụng cá nhân:

![Menu Avatour khi trình bày tài sản bên ngoài cuộc họp, ví dụ: khi truy cập không gian làm việc](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-workspace_iri8gc.png) *Menu Avatour khi trình chiếu tài nguyên trong không gian làm việc*

- **Dòng thời gian video / Thanh tiến trình** – Hiển thị tiến trình video kèm theo ghi chú và các chủ đề chính được trích xuất từ bản âm thanh. Nhấp vào bất kỳ vị trí nào trên dòng thời gian để di chuyển qua video. Nhấp vào một ghi chú hoặc chủ đề để chuyển đến thời điểm đó và mở ghi chú. Bao gồm các nút điều khiển **Phát / Tạm dừng**.  
- **Ảnh chụp nhanh, Ghi chú, Bảng tóm tắt ghi chú, Liên kết chia sẻ, Phụ đề**  
- Không khả dụng: **Spotlight, POV** (các tính năng này yêu cầu có người tham gia trực tiếp)  
- Các nút điều khiển bổ sung:
  - **Bước 10 giây** – Bỏ qua về phía trước/phía sau  
  - **Tốc độ phát lại** – Điều chỉnh tốc độ (0,5×–2×)  
  - **Cắt video** – Cắt phần đầu hoặc phần cuối của tài liệu


## 4. Dành cho người dùng chủ và quản trị viên - Bảng điều khiển web Avatour {#for-host-and-admin-users-avatour-web-console}

Khi đăng nhập vào Tài khoản người dùng Avatour, bạn sẽ truy cập vào **Bảng điều khiển web**.  

### 4.1 Bảng điều khiển web - Tổng quan về Menu chính {#web-console-overview-main-menu}

Ở phía bên trái, bạn sẽ thấy các mục menu sau:

![Bảng điều khiển web Avatour - Menu chính](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu_qwpthq.png) *Bảng điều khiển web Avatour - Menu chính*

- **Không gian làm việc** – Sắp xếp nội dung của bạn một cách hiệu quả. Mỗi không gian làm việc chứa các mục **Tài sản**, **Người cộng tác**, **Cuộc họp** và **Cài đặt**.  
- **Tài nguyên** – Truy cập và quản lý tất cả tài nguyên của bạn (video, hình ảnh, tệp PDF). Quản trị viên có thể xem tất cả tài nguyên của tài khoản, và các tài nguyên được chia sẻ sẽ hiển thị cho tất cả người dùng.  
- **Hồ sơ** – Quản lý ngôn ngữ và mật khẩu của bạn.  
- **Phân tích** – Theo dõi hoạt động phiên làm việc, mức độ sử dụng không gian làm việc và các chỉ số ROI.  
- **Cài đặt** *(Chỉ dành cho quản trị viên)* – Cấu hình các thiết lập mặc định cho không gian làm việc, cuộc họp và tài sản trên toàn tổ chức. Quản trị viên cũng có thể tùy chỉnh thương hiệu (logo, màu sắc, hình nền).  
- **Tài khoản** *(Chỉ dành cho quản trị viên)* – Quản lý người dùng đã đăng ký và camera 360°.  
- **Đăng nhập thiết bị** – Nhập mã hiển thị trên camera 360° của bạn để ghép nối thiết bị với tài khoản.  
- **Hướng dẫn** – Truy cập các hướng dẫn có hướng dẫn chi tiết.  
- **Đăng xuất** – Đăng xuất khỏi bảng điều khiển.

> Các phần như Hồ sơ, Đăng nhập thiết bị, Hướng dẫn và Đăng xuất đều dễ hiểu và không có các phần con chi tiết.

---

### 4.2 Bảng điều khiển web - Chi tiết theo mục menu (kèm hình ảnh) {#web-console-details-by-menu-item}

#### 4.2.1 Không gian làm việc

Không gian làm việc là các đơn vị tổ chức linh hoạt, cho phép bạn quản lý tài sản, cộng tác viên và các cuộc họp tại một nơi. Bạn có thể tạo một không gian làm việc mới bằng nút **Không gian làm việc mới** ở góc trên bên phải.

![Bảng điều khiển web Avatour - Mục menu chính Không gian làm việc](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspaces_hnhkjj.png) *Bảng điều khiển web Avatour - Mục menu chính Không gian làm việc*

Nhấp vào biểu tượng chuông để xem tóm tắt hoạt động của không gian làm việc trong 7 ngày qua.

![Avatour Web Console - Hoạt động gần đây trong không gian làm việc](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspace-recent-activities_gby1ws.png) *Hoạt động gần đây trong không gian làm việc*

Bên trong không gian làm việc:

![Không gian làm việc Avatour với Bảng tài sản, Bảng vẽ trống và Bảng cuộc họp](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png) *Không gian làm việc với Tài nguyên (bên trái), Bảng vẽ (giữa), Cuộc họp (bên phải)*

- **Tài nguyên** – Quản lý các tệp được phân bổ cho không gian làm việc này.  
- **Người cộng tác** – 
  Kiểm soát quyền truy cập vào không gian làm việc bằng cách 
  - **Người xem** – Có thể xem tài nguyên. Lời mời sẽ tạo tài khoản Khách nếu cần.  
  - **Người chỉnh sửa** – Quyền kiểm soát toàn bộ không gian làm việc, tương đương với quyền của Chủ phòng. Lời mời sẽ nâng cấp người dùng lên Chủ phòng nếu cần.  
> Nhiều người dùng có thể truy cập không gian làm việc cùng lúc mà không cần tổ chức cuộc họp. Các không gian làm việc công khai và cài đặt quyền truy cập cuộc họp cung cấp các phương thức truy cập thay thế.  
- **Báo cáo** – Tạo báo cáo bằng cách sử dụng mẫu danh sách kiểm tra trên các tài nguyên được chọn trong không gian làm việc.  

![Báo cáo không gian làm việc và lựa chọn tài sản của Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-selection-and-workspace-report_itjt8f.png) *Báo cáo không gian làm việc và lựa chọn tài sản*

- **Bản đồ** – Hiển thị vị trí các tài sản được hỗ trợ GPS trên bản đồ.  
- **Cuộc họp** – Tổ chức các cuộc họp trong không gian làm việc.  
- **Cài đặt** – Định cấu hình các thiết lập mặc định cho không gian làm việc và cuộc họp:

![Cài đặt Avatour - Chế độ xem không gian làm việc](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-settings_llcei3.png) *Cài đặt không gian làm việc*

**Cài đặt không gian làm việc**

- **Mẫu báo cáo** – Chọn mẫu danh sách kiểm tra cho báo cáo AI.  
- **Bật thông báo** – Email tóm tắt hàng ngày về các thay đổi trạng thái ghi chú.  

![Thông báo qua email - Ví dụ](https://res.cloudinary.com/avatour/image/upload/c_crop,h_600,w_600,x_170,y_60/Screenshot_2026-03-05_140654_bjk0xk.png) *Ví dụ về thông báo qua email*

- **Không gian làm việc công khai** – Bất kỳ ai có liên kết đều có thể xem tài sản trực tiếp.

**Cài đặt cuộc họp**
  
* **Yêu cầu xác thực** – Người tham gia phải đăng nhập.  
* **Cho phép truy cập khách** – Cho phép người dùng chưa đăng ký xem tài nguyên.  
* **Tự động bắt đầu ghi âm / Bắt đầu thủ công** – Chọn chế độ ghi âm tự động hoặc bắt đầu thủ công cho cuộc họp.  
* **Yêu cầu người chủ trì** – Người chủ trì phải chấp nhận người tham gia; cuộc họp kết thúc khi người chủ trì rời khỏi.  
* **Cho phép truy cập với tư cách người xem** – Tham gia mà không cần mic hoặc camera; giao tiếp qua chat.  
* **Cuộc họp được bảo vệ bằng mật khẩu** – Yêu cầu mật khẩu để tham gia.  
* **Hiển thị câu hỏi về tiết kiệm chi phí đi lại** – Hỏi người tham gia xem cuộc họp có giúp giảm chi phí đi lại hay không.  

> Các cài đặt có thể được kết hợp (ví dụ: không yêu cầu người chủ trì nhưng được bảo vệ bằng mật khẩu).

---

#### 4.2.2 Tài nguyên

Quản lý tất cả video 360°/2D, hình ảnh và tệp PDF. Tải lên/tải xuống tài nguyên, phân bổ vào không gian làm việc, chia sẻ với người dùng khác, đổi tên, in/tải xuống báo cáo, kích hoạt tính năng làm mờ khuôn mặt và tóm tắt bằng AI.

![Bảng điều khiển web Avatour - Mục menu chính Tài sản](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-assets_ky5emz.png) *Mục menu chính Tài sản*

---

#### 4.2.3 Phân tích

Cung cấp thông tin chi tiết về các cuộc họp, tình hình sử dụng không gian làm việc và các chỉ số ROI.

![Avatour Web Console - Mục menu chính Phân tích (1 trong 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-1-of-3_ds3epe.png) *Tổng quan về Phân tích*

![Bảng điều khiển web Avatour - Mục menu chính: Phân tích (2 trong 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-2-of-3_vpcsme.png) *Hoạt động cuộc họp & Sử dụng không gian làm việc*

![Bảng điều khiển web Avatour - Mục menu chính Phân tích (3 trong 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-3-of-3_hn2pmr.png) *Sử dụng giấy phép thiết bị & ROI* 

## 5. Tại chỗ - Cách sử dụng bộ công cụ Avatour Turnkey {#onsite-how-to-use-the-avatour-turnkey-kit}

### 5.1 Bắt đầu
Tại đây, bạn sẽ tìm thấy một hướng dẫn trực tuyến rất chi tiết để thực hiện những bước đầu tiên với Bộ công cụ Avatour Turnkey: [Hướng dẫn Khởi động Nhanh – Bộ công cụ Avatour Turnkey 3.1 (Cài đặt Pilot PanoX V2)](https://avatour.com/quickstart-panox-v2)

Và đây cũng là hình ảnh kèm hướng dẫn mà bạn sẽ tìm thấy bên trong nắp hộp của bộ kit 3.1.
![Hình ảnh bên trong nắp hộp bộ Avatour Kit](https://res.cloudinary.com/avatour/image/upload/v1775994773/avatour-turnkey-kit-3.1-inside-lid-picture_dq4ipl.png) *Hình ảnh bên trong nắp hộp bộ kit Avatour* 

Hãy làm theo hướng dẫn để mở hộp, lắp ráp và bật nguồn máy ảnh của bạn.

---

### 5.2 Mẹo hữu ích

#### Pin ngoài – Thời lượng ghi hình dài hơn & Cải thiện khả năng tản nhiệt 

- **Nếu bộ kit của bạn bao gồm pin Ulanzi:** Gắn pin vào giữa chân đế tripod và thanh kéo dài, sau đó kết nối pin với máy quay qua cổng USB-C.  

- **Nếu bộ sản phẩm của bạn bao gồm thanh pin Telesin:** Gắn máy quay trực tiếp lên thanh pin có thể kéo dài của Telesin và kết nối qua cổng USB-C.  

Sử dụng pin ngoài:

1. Kéo dài thời lượng pin tổng thể từ ~40 phút (chỉ dùng pin máy quay) lên ~3 giờ.  
2. Tăng độ ổn định cho thiết lập máy ảnh.  
3. Giúp ngăn ngừa nguy cơ quá nhiệt.  

> Chúng tôi khuyến nghị luôn sử dụng pin ngoài ngay từ đầu, đặc biệt là trong các cuộc họp trực tiếp.

#### Lưu ý về âm thanh cho các cuộc họp trực tiếp và ghi hình

- **Môi trường ồn ào:** 
  Sử dụng tai nghe Shokz đi kèm trong bộ sản phẩm để thu âm thanh rõ ràng.  
  - **Bật/Tắt nguồn:** Nhấn và giữ nút “+” trong 3 giây (đèn LED xanh dương = bật, đèn LED đỏ = tắt).  
  - **Chế độ ghép nối Bluetooth:** Khi tai nghe đang tắt, nhấn và giữ nút “+” trong 5 giây (đèn LED nhấp nháy màu xanh dương/đỏ).  
  - **Âm lượng:** Sử dụng các nút “+” và “-”.  

- **Môi trường yên tĩnh hơn / nhiều người tham gia gần camera:** 
  Sử dụng loa kẹp NoxGear. Loa này không có chất lượng âm thanh cao như các loa hội nghị (ví dụ: Jabra Speak), nhưng dễ dàng kẹp vào áo và thu âm giọng nói xung quanh hiệu quả.  
  - **Bật/Tắt nguồn:** Nhấn giữ nút Phát/Tạm dừng trong 2 giây.  
  - **Chế độ ghép nối Bluetooth:** Tự động chuyển sang chế độ ghép nối khi bật nguồn (đèn LED nhấp nháy màu xanh lam/đỏ; sáng liên tục màu xanh lam khi đã ghép nối).  
  - **Âm lượng:** Sử dụng các nút “+” và “-”.  

- **Sử dụng thiết bị của riêng bạn:** Nếu bạn muốn dùng thiết bị khác (ví dụ: loa hội nghị hoặc tai nghe cá nhân), bạn có thể ghép nối qua camera: Cài đặt → Bluetooth.  

#### Kết nối, Kết nối, Kết nối
**Trước khi bắt đầu:** Đảm bảo kết nối internet qua:

- **WiFi cục bộ** (ưu tiên)
- **Mạng di động** (nếu nằm ngoài phạm vi phủ sóng WiFi)

**Băng thông khuyến nghị:** 10 Mbps tải lên/tải xuống để phát trực tiếp 360° đầy đủ (~5 Mbps). Băng thông thấp hơn (1–2 Mbps) chỉ hoạt động khi đứng yên.

##### Kiểm tra tốc độ mạng
- **Kiểm tra tại một vị trí:** Sử dụng bất kỳ công cụ kiểm tra tốc độ nào bạn thường dùng (ví dụ: [Speedtest](https://www.speedtest.net)) để xác minh cả băng thông tải lên và tải xuống.   
- **Kiểm tra khi di chuyển trong khu vực:** Từ camera: Cài đặt → Mạng → Kiểm tra kết nối. Đi bộ qua toàn bộ khu vực để xác nhận phạm vi phủ sóng và băng thông.

##### WiFi cục bộ
- Rất được khuyến nghị để đảm bảo kết nối ổn định.  
- Nếu bộ phận CNTT yêu cầu đưa vào danh sách trắng, hãy tìm địa chỉ MAC: Cài đặt → Giới thiệu → Địa chỉ WiFi.

##### Mạng di động
**Tùy chọn A: Điểm phát sóng và SIM do bộ sản phẩm cung cấp**  

- Gắn điểm phát sóng GlocalMe vào thanh pin Telesin (bằng nam châm).  
- Đảm bảo không có nhiễu và duy trì kết nối khi di chuyển xa khỏi camera.  
- Khắc phục sự cố:
  - Xác nhận SIM được cài đặt sẵn (không phải Cloud SIM).  
  - Bật 5G trong Trình quản lý thẻ SIM.  
  - Kiểm tra xem APN có đúng với khu vực của bạn không ([Hướng dẫn thiết lập APN](https://avatour.com/support/how-do-i-change-the-apn-on-my-glocalme-hotspot)).

**Tùy chọn B: Điểm phát sóng cá nhân / SIM**
- Sử dụng điện thoại thông minh của riêng bạn hoặc thiết bị phát sóng chuyên dụng.  

**Lưu ý quan trọng:**  
> Tắt điểm phát sóng khi đang kết nối với WiFi; chỉ bật khi nằm ngoài vùng phủ sóng. Hệ điều hành của máy ảnh sẽ tự động chuyển đổi giữa các mạng WiFi dựa trên cường độ tín hiệu và có thể vô tình chuyển sang điểm phát sóng ngay cả khi có WiFi.

> Mạng di động có thể hạn chế băng thông một cách bất ngờ. Hãy kiểm tra giới hạn gói dữ liệu với nhà mạng của bạn hoặc liên hệ với bộ phận hỗ trợ của Avatour nếu bạn đang sử dụng điểm phát sóng và SIM của chúng tôi.

##### Các tình huống băng thông thấp
- Quay sẵn video tại địa điểm để phát lại sau ([hướng dẫn quay phim](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).  
- Chia sẻ luồng camera từ điện thoại thông minh để bổ sung cho các khu vực có băng thông thấp (tốc độ tải lên 0,1–0,3 Mbps).

##### Không có kết nối
- Chỉ có thể sử dụng video đã quay sẵn ([hướng dẫn quay phim](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).

#### Những người tham gia khác tại chỗ – Các phương pháp hay nhất

Khi nhiều người tham gia tham gia một cuộc họp trực tiếp trên Avatour từ cùng một địa điểm với camera 360°, việc quản lý cẩn thận **âm thanh và băng thông** là rất quan trọng:  

- Mỗi điện thoại thông minh, máy tính bảng hoặc máy tính xách tay được kết nối tại chỗ đều tiêu tốn băng thông mạng và có thể ảnh hưởng tiêu cực đến luồng video từ camera 360°.  
- Nhiều micrô và loa trong cùng một không gian có thể gây ra **hiện tượng phản hồi âm thanh**, khiến trải nghiệm cuộc họp trở nên khó chịu cho tất cả người tham gia.

#### Người tham gia tại chỗ khác – Các thực hành tốt nhất

Khi nhiều người tham gia tham gia cuộc họp Avatour trực tiếp từ cùng một địa điểm với camera 360°, việc quản lý cẩn thận **âm thanh và băng thông** là rất quan trọng:  

- Mỗi chiếc điện thoại thông minh, máy tính bảng hoặc máy tính xách tay được kết nối tại chỗ đều tiêu tốn băng thông mạng và có thể ảnh hưởng tiêu cực đến luồng hình ảnh từ camera 360°.  
- Nhiều micro và loa trong cùng một không gian có thể gây ra **hiện tượng phản hồi âm thanh**, khiến trải nghiệm cuộc họp trở nên khó chịu cho tất cả người tham gia.

Để giải quyết những thách thức này, hãy tuân thủ các **thực hành tốt nhất** sau:

- **Sử dụng tai nghe có dây hoặc không dây:** Tốt nhất là loại có tính năng khử tiếng ồn để ngăn chặn tiếng vang và phản hồi âm thanh.  
- **Chế độ Tại chỗ:** Tham gia cuộc họp ở chế độ Tại chỗ khi có mặt thực tế gần camera 360°.  
  - Chế độ này được tối ưu hóa cho việc sử dụng tại chỗ: 
 - Tắt tiếng mic và loa của người tham gia theo mặc định. 
 - **Không** truyền hình ảnh từ camera của người tham gia.  
    - **Không** hiển thị hình ảnh từ camera 360° trên trình duyệt của người tham gia. 
 - Tiết kiệm băng thông mạng, đảm bảo camera 360° có băng thông tải lên tối đa cho luồng phát trực tiếp. 
 - Hữu ích khi người dùng muốn chia sẻ chi tiết cụ thể; bạn **có thể chia sẻ lại hình ảnh từ camera của mình** để người xem tập trung vào những góc nhìn cụ thể.  
- **Tắt tiếng khi không đang nói:** Ngăn chặn tiếng vang âm thanh không mong muốn và các yếu tố gây xao nhãng.  
- **Sử dụng mạng riêng biệt nếu có thể:** Kết nối điện thoại thông minh của bạn với mạng khác với mạng của camera để giảm nhiễu.  

Tuân thủ các hướng dẫn này sẽ đảm bảo một chuyến tham quan trực tiếp mượt mà, chất lượng cao cho cả người tham gia tại chỗ và từ xa.

### 5.3 Ứng dụng camera Avatour

Dưới đây là các menu (1) Màn hình chính, (2) Cài đặt và (3) Cài đặt mạng.

![Ứng dụng camera Avatour 360° - Ba menu](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-cam-app-3-menu-screens_nju8bt.png) *Ứng dụng máy ảnh Avatour 360° - 3 menu*

**Chụp nhanh** - Dùng để quay video 360° ngoại tuyến. - Để biết mô tả chi tiết, hãy xem [Làm thế nào để quay và tải lên video 360° bằng ứng dụng Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app). Chúng tôi khuyên bạn nên sử dụng thiết bị âm thanh bên ngoài (kết nối qua Bluetooth). Lưu ý: Bạn cũng có thể quay video 2D và chụp ảnh thông thường - chỉ cần chuyển chế độ giữa 360° và 2D ở góc dưới bên phải khi ở màn hình QC.

**Họp trực tiếp** - Dành cho hội nghị truyền hình 360° trực tiếp. Bạn sẽ thấy các không gian làm việc của mình và khi nhấp vào một trong số đó, luồng video trực tiếp từ camera 360° sẽ được khởi động. Trước khi tham gia cuộc họp bằng camera 360°, bạn cần kết nối thiết bị âm thanh qua Bluetooth. Để biết mô tả chi tiết, hãy xem [Cách bắt đầu cuộc họp Live Capture bằng camera Pilot?](https://avatour.com/support/how-to-start-a-live-capture-meeting-with-your-pilot-camera)

> Khi tổ chức cuộc họp Live Capture bằng camera 360°, bạn sẽ có các công cụ họp tương tự như trên nền tảng web. Dưới đây là liên kết đến bài viết trong Cơ sở Kiến thức của chúng tôi giải thích chi tiết hơn về các công cụ này: [Công cụ Ứng dụng Điều hành](https://avatour.com/support/what-avatour-app-tools-are-available-to-labpano-pilot-camera-operators)

**Thư viện** - Tại đây, bạn có thể tìm thấy tất cả các video và hình ảnh 360° của mình để tải lên Bảng điều khiển web Avatour.

**Cài đặt** - Trong phần Cài đặt, bạn có các tùy chọn sau:

- **Mạng**: Tùy chọn này cho phép bạn thay đổi mạng WiFi mà camera đang kết nối hoặc chạy kiểm tra kết nối mạng để xem thông lượng phát trực tuyến của bạn
- **Quay trực tiếp**: Điều chỉnh cài đặt Quay trực tiếp tùy thuộc vào băng thông có sẵn, độ nhạy VR của khách hoặc liệu ống kính bảo vệ của camera có được lắp đặt hay không:
  - **Tốc độ khung hình mục tiêu**: Điều chỉnh tốc độ khung hình cho video Ghi hình trực tiếp trong khoảng 15 fps, 24 fps và 30 fps. Tốc độ khung hình cao hơn sẽ tạo ra video mượt mà hơn, nhưng sẽ yêu cầu băng thông tải lên lớn hơn. Mặc định: 15 fps
  - **Tốc độ bit mục tiêu**: Cho phép bạn tăng hoặc giảm tốc độ bit phát trực tuyến tối đa cho tính năng Ghi hình trực tiếp. Bạn có thể đặt tốc độ bit mục tiêu trong khoảng từ 1 Mbps đến 10 Mbps. Tốc độ bit cao hơn sẽ mang lại độ phân giải video cao hơn, nhưng sẽ yêu cầu băng thông tải lên nhiều hơn. Mặc định: 5 Mbps
  - **Tối ưu hóa chuyển động**: Tính năng này sẽ giảm tốc độ khung hình video, giúp giảm tải cho băng thông tải lên của mạng và tăng tốc độ bit phát trực tuyến. Ngoài ra, tùy chọn này còn giúp giảm tình trạng say chuyển động cho người tham gia VR. Mặc định: Tắt
  - **Thấu kính bảo vệ**: Tùy chọn này sẽ ảnh hưởng đến cách ghép nối video 360° tùy thuộc vào việc ống kính bảo vệ đã được lắp đặt trên máy ảnh của bạn hay chưa. Nếu bạn không có ống kính bảo vệ, hãy đặt tùy chọn này thành “Không”. Nếu bạn nhận được Bộ Kit 3.0, máy ảnh của bạn đã được cài đặt sẵn ống kính bảo vệ và bạn nên đặt tùy chọn này thành “Có”. Mặc định: Có

- **Chế độ Quay nhanh**: Điều chỉnh cài đặt Chế độ Quay nhanh tùy theo tốc độ khung hình video ưa thích, băng thông khả dụng để tải lên video đã quay, hoặc tùy thuộc vào việc máy ảnh của bạn có được lắp kính bảo vệ hay không. Chế độ Quay nhanh có độ phân giải cố định là 4K, thường mang lại sự cân bằng tốt giữa chất lượng video và kích thước tệp. (Để có độ phân giải cao hơn, bạn có thể sử dụng các ứng dụng camera gốc, kể cả trên PanoX V2; để biết chi tiết, xem [Làm thế nào để quay và tải lên video 360 độ bằng ứng dụng Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)):
  - **Tốc độ khung hình mục tiêu**: Điều chỉnh tốc độ khung hình cho các bản ghi video Quick Capture trong khoảng 15 fps, 24 fps và 30 fps. Tốc độ khung hình cao hơn sẽ tạo ra video mượt mà hơn, nhưng sẽ làm tăng kích thước tệp video và thời gian tải lên. Khuyến nghị: 30 fps
  - **Tốc độ bit mục tiêu**: Đặt tốc độ bit mục tiêu cho các bản tải lên Quick Capture trong khoảng từ 5 Mbps đến 20 Mbps. Tốc độ bit thấp hơn sẽ tăng tốc độ tải lên, nhưng sẽ làm giảm chất lượng video. Khuyến nghị: 20 Mbps
  - **Ống kính bảo vệ**: *Xem phần Ống kính bảo vệ cho Live Capture ở trên*

  > Xem thêm [Công cụ tính kích thước tệp video Avatour 360°](https://avatour.com/support/avatour-360deg-video-file-size-calculator) để biết thêm lời khuyên về các cài đặt trên và kích thước tệp video.

- **Giới thiệu**: Xem số sê-ri thiết bị và phiên bản phần mềm


**Tài khoản** - Để đăng nhập bằng tài khoản chủ hoặc quản trị viên Avatour của bạn.

## 6. Lời khuyên về các phương pháp hay nhất {#best-practice-advice}

### 6.1 Những lần sử dụng đầu tiên (không chính thức) và làm quen

Để bắt đầu sử dụng và làm quen với Avatour Web Console và Avatour Turnkey Kit, chúng tôi khuyên bạn nên thực hiện các bước sau:

1. Mang bộ sản phẩm về nhà và thử nghiệm cùng gia đình và bạn bè bằng kết nối internet tại nhà.
2. Mang bộ sản phẩm đến văn phòng và kết nối với mạng công ty (có thể phát sinh các vấn đề liên quan đến công ty, ví dụ như tường lửa công ty – nhưng từ bước 1, bạn đã biết rằng Avatour hoạt động tốt và đây là vấn đề mà đội ngũ CNTT của bạn cần giải quyết với sự hỗ trợ từ Avatour).
3. Bắt đầu sử dụng Avatour tại chỗ (ngoài văn phòng) tại địa điểm họp mà những người tham gia từ xa thường phải di chuyển đến. Có thể sẽ phát sinh thêm các vấn đề liên quan đến kết nối. Avatour sẽ hỗ trợ phối hợp cùng đội ngũ CNTT của bạn.
4. Bắt đầu sử dụng với những người tham gia từ xa cả trong và ngoài công ty.

### 6.2 Trước khi tổ chức cuộc họp trực tiếp bằng video 360°

- Chúng tôi khuyến nghị thực hiện một chuyến tham quan video 360° được ghi lại trước bất kỳ chuyến tham quan trực tiếp nào nếu thời gian cho phép, vì ba lý do sau: (1) Có giải pháp dự phòng cho buổi tham quan trực tiếp, (2) có tài liệu để lưu trữ và xem lại sau này (bên cạnh bản ghi lại của buổi tham quan trực tiếp) và (3) bắt đầu xây dựng thư viện video 360° của tất cả các địa điểm của quý vị, điều này có thể hữu ích cho nhiều trường hợp sử dụng. 
- Sạc đầy đủ tất cả các thành phần bộ thiết bị trong ít nhất 90 phút trước cuộc họp trực tiếp. Dù sao, chúng tôi cũng khuyến nghị nên để tất cả các thiết bị sạc liên tục khi không sử dụng. Như vậy, tất cả các thiết bị sẽ luôn sẵn sàng, kể cả cho các cuộc họp đột xuất không theo kế hoạch.
- Lắp ráp đầy đủ bộ kit (1. chân đế tripod + 2. pin Ulanzi + 3. gậy kéo dài + 4. camera 360°).

- Xác nhận đã tạo Workspace để tổ chức cuộc họp trực tiếp và bao gồm tất cả các tài nguyên liên quan.

- Mời tất cả người tham gia vào cuộc họp thông qua Không gian làm việc của bạn. Thao tác này sẽ tạo lời mời trên lịch của tất cả người tham gia và bao gồm liên kết mời tham gia cuộc họp.

- Ghép nối và kết nối tai nghe Bluetooth hoặc loa mà bạn dự định sử dụng cho chuyến tham quan với camera.

- Tất cả người dùng điện thoại thông minh tại hiện trường nên kết nối từ một mạng khác với mạng của camera. Điều này sẽ giảm tải cho băng thông mạng của camera.

- Nếu bạn là người điều khiển camera một mình, hãy mang theo điện thoại thông minh để có thể chia sẻ màn hình điện thoại và hiển thị các chi tiết nhỏ.

- Xác nhận camera 360° có thể kết nối với mạng Wi-Fi tại địa phương.

- Trước khi bắt đầu cuộc họp Avatour, hãy lên kế hoạch lộ trình di chuyển trong cơ sở. Thực hiện một cuộc họp Avatour thử nghiệm với camera và kiểm tra xem tất cả các khu vực đều có tốc độ bit trên 1 Mbps. Thông tin này có thể xem trực tiếp trên màn hình camera hoặc, đối với người tham gia từ xa, bằng cách vào Cài đặt và kích hoạt tùy chọn “Hiển thị Tốc độ Bit”.

- Nếu bạn nhận thấy một số khu vực có băng thông thấp hoặc không có băng thông, tốt nhất là nên chụp ảnh hoặc quay video. Sau đó, bạn có thể trình chiếu những nội dung này trong cuộc họp để người tham gia từ xa xem xét. Bạn có thể tham khảo hướng dẫn tại đây để tìm hiểu về tính năng “Quick Capture” (Chụp nhanh) để quay và tải lên video/hình ảnh: [Làm thế nào để quay và tải lên video 360 độ bằng ứng dụng Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)

- Nếu có người tham gia từ xa chưa từng sử dụng Avatour trước đây, hãy cung cấp cho họ một bản tóm tắt ngắn gọn về nền tảng này, các tính năng của nó (video trực tiếp 360 độ, tài nguyên, ảnh chụp nhanh, chú thích, tính năng Spotlight) và các công cụ hỗ trợ cuộc họp.

- Bạn có thể bắt đầu bằng một giải pháp hội nghị video khác (ví dụ: Teams, Zoom, Google Meet), nhưng trước khi chuyển sang Avatour, hãy đóng hoàn toàn ứng dụng hội nghị video kia. Trong một số trường hợp, các ứng dụng khác này sẽ ưu tiên sử dụng micrô/loa/webcam của thiết bị bạn, dẫn đến việc các thiết bị này bị vô hiệu hóa đối với Avatour. Ngoài ra, KHÔNG chạy Avatour VÀ một ứng dụng hội nghị video khác cùng lúc vì điều này sẽ làm giảm băng thông khả dụng.

- Nếu bạn dự định sử dụng camera 360° trong môi trường có nhiệt độ cao, nên sử dụng mô-đun làm mát (chỉ dành cho Pilot Pano). Điều này sẽ giúp giảm nguy cơ camera quá nhiệt và tự động tắt nguồn.

### 6.3 Khi vận hành camera tại hiện trường cho cuộc họp video trực tiếp 360°

- Khi vận hành camera, hãy đảm bảo rằng bạn **đi chậm** và **thường xuyên dừng lại để đặt camera xuống chân máy**. Điều này giúp (1) cải thiện chất lượng video do bạn tạo ra ít dữ liệu video hơn khi không di chuyển máy ảnh một cách không cần thiết và (2) giảm thiểu thời gian gián đoạn video tiềm ẩn khi kết nối mạng của máy ảnh chuyển đổi giữa các điểm truy cập Wi-Fi.

- Giữ máy ảnh trước mặt bạn và cao hơn tầm mắt. Điều này giúp tất cả người tham gia từ xa có thể quan sát được phần lớn khu vực xung quanh bạn.

- Trong trường hợp cần giữ máy quay ổn định, hãy sử dụng chân máy và điều chỉnh độ cao phù hợp, tốt nhất là ngang tầm mắt.

- Luôn kết nối máy quay với mạng WiFi địa phương khi có thể. Đối với khu vực không có kết nối WiFi, hãy sử dụng điểm phát sóng (hotspot) được cung cấp. Điểm phát sóng này có thẻ SIM sẽ kết nối với mạng di động đáng tin cậy gần bạn. Luôn tắt điểm phát sóng khi không sử dụng trong nhà, vì nếu không, camera 360° có thể kết nối với điểm phát sóng – điều mà chúng ta không mong muốn khi ở trong nhà. Khi ở ngoài trời, hãy để điểm phát sóng gần camera 360°.

- Khi tốc độ truyền dữ liệu trên camera bắt đầu giảm xuống dưới 2 Mbps, hãy đi chậm lại hoặc dừng hẳn cho đến khi tín hiệu ổn định trở lại. Điều này thường xảy ra khi bạn chuyển từ điểm truy cập WiFi này sang điểm truy cập khác. 

- Nếu bạn biết kết nối và video sẽ bị gián đoạn khi di chuyển đến một vị trí cụ thể (Ví dụ: di chuyển từ khu vực sản xuất trong nhà sang khu vực ngoài trời), hãy thông báo trước cho những người tham gia từ xa.

- Nếu cần trình chiếu nội dung có chi tiết cao hoặc chữ nhỏ, hãy sử dụng điện thoại thông minh của chính bạn hoặc của một người tham gia tại hiện trường để tham gia cuộc họp và chia sẻ camera phía sau của điện thoại đó.

- Nếu có thể, chúng tôi khuyến nghị nên có thêm một người tại hiện trường để hỗ trợ việc chia sẻ camera điện thoại thông minh như đã mô tả ở trên, vì điều này thường rất hữu ích hoặc cần thiết.

- Tốt nhất, những người dùng điện thoại thông minh tại hiện trường nên tham gia cuộc họp (1) ở chế độ tại hiện trường và (2) trên một mạng khác với mạng mà camera đang sử dụng để không chiếm dụng băng thông tải lên quan trọng của camera 360°.

- Tất cả những người tham gia tại hiện trường tham gia từ điện thoại thông minh của họ nên được tắt tiếng, trừ khi đang chủ động phát biểu.
