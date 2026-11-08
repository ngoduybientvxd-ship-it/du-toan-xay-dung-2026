# HỆ THỐNG TÍNH DỰ TOÁN XÂY DỰNG CÔNG TRÌNH NGUỒN VỐN NHÀ NƯỚC (2026)

Dự án phần mềm & bộ bảng tính tự động xác định **Dự toán xây dựng công trình sử dụng vốn đầu tư công và vốn nhà nước ngoài đầu tư công**, được thiết kế tuân thủ chặt chẽ hệ thống văn bản quy phạm pháp luật mới nhất có hiệu lực trong năm **2026**.

---

## 1. Căn cứ Pháp lý Áp dụng (Cập nhật 2026)

1. **Luật Xây dựng số 135/2025/QH15** (ban hành ngày 10/12/2025, có hiệu lực thi hành từ ngày **01/01/2026**).
2. **Nghị định số 206/2026/NĐ-CP** ngày 15/06/2026 của Chính phủ quy định chi tiết về quản lý chi phí đầu tư xây dựng (có hiệu lực từ ngày **01/07/2026**, thay thế Nghị định 10/2021/NĐ-CP).
3. **Thông tư số 36/2026/TT-BXD** ngày 26/06/2026 của Bộ Xây dựng hướng dẫn một số nội dung, phương pháp xác định và quản lý chi phí đầu tư xây dựng (có hiệu lực từ ngày **01/07/2026**, hợp nhất tại Văn bản hợp nhất số **89/2026/VBHN-TT-BXD**).
4. **Quyết định số 1538/QĐ-BXD** ngày 28/08/2026 của Bộ Xây dựng về việc **đính chính Thông tư số 36/2026/TT-BXD**:
   - Đính chính công thức tính **Chi phí nhà tạm để ở và điều hành thi công ($LT$)** tại Bảng 3.8 và Bảng 3.9 Phụ lục III thành:
     $$LT = G_{XDTT} \times \text{Tỷ lệ} \times (1 + T_{GTGT})$$
   - Đính chính nội dung STT 1 Bảng 3.4 từ *"Bảo dưỡng..."* thành *"Sửa chữa công trình có chi phí xây dựng < 500 triệu đồng (66,0% trên chi phí nhân công)"*.
5. **Thông tư số 37/2026/TT-BXD** ngày 26/06/2026 của Bộ Xây dựng hướng dẫn phương pháp xác định định mức dự toán và các chỉ tiêu kinh tế - kỹ thuật (đơn giá nhân công, giá ca máy và thiết bị thi công, chỉ số giá xây dựng).
6. **Thông tư số 38/2026/TT-BXD** ngày 26/06/2026 của Bộ Xây dựng ban hành **Định mức xây dựng** (có hiệu lực từ ngày **01/07/2026**):
   - **Phụ lục II**: Định mức dự toán xây dựng công trình.
   - **Phụ lục III**: Định mức dự toán lắp đặt máy và thiết bị công nghệ.
   - **Phụ lục VIII**: Định mức chi phí quản lý dự án và tư vấn đầu tư xây dựng.

---

## 2. Cấu trúc Dự án

```text
du-toan-xay-dung-2026/
├── index.html                        # Giao diện Web App chính (7 phân hệ nghiệp vụ)
├── styles.css                        # Hệ thống giao diện kỹ thuật (Sáng / Tối, chuẩn in ấn A4)
├── app.js                            # Bộ máy tính toán Frontend & xuất Excel (.xls) đa sheet
├── data/
│   ├── regulations_2026.json         # Bảng định mức tỷ lệ TT 36/2026 (PL III) & TT 38/2026 (PL VIII)
│   ├── bang_gia_co_so.json           # CSDL giá Vật liệu (33), Nhân công (3), Máy thi công (14)
│   ├── dinh_muc_tt38_2026.json       # CSDL 35 mã hiệu định mức xây dựng & lắp đặt TT 38/2026
│   └── du_an_mau_dan_dung.json       # 2 dự án mẫu hoàn chỉnh (Dân dụng & Công nghiệp)
├── scripts/
│   ├── du_toan_engine.py             # Bộ máy tính toán Python chuẩn hóa 2026
│   ├── build_web_bundle.py           # Đóng gói dữ liệu JSON vào app.js & HTML độc lập
│   └── create_gsheet_template.py     # Khởi tạo & nạp công thức tự động lên Google Sheets
├── exports/
│   └── csv/                          # Bộ 8 bảng biểu CSV xuất tự động từ bộ máy tính toán
└── tests/
    └── test_du_toan.py               # Bộ kiểm thử tự động (Unit Tests) kiểm증 toàn bộ công thức
```

---

## 3. Hướng dẫn Sử dụng

### 3.1. Chạy Kiểm thử & Bộ máy Tính toán bằng Python
```bash
python3 tests/test_du_toan.py
python3 scripts/du_toan_engine.py
```

### 3.2. Khởi chạy Ứng dụng Web Dự toán
```bash
python3 -m http.server 8080
```
Mở trình duyệt tại địa chỉ `http://localhost:8080` để sử dụng đầy đủ 7 phân hệ:
1. **Thông tin & Tham số dự án**: Cài đặt loại công trình, cấp công trình, bước thiết kế, hệ số $K_{NC}, K_M$, thuế suất GTGT và dự phòng phí.
2. **Tiên lượng & Khối lượng (BOQ)**: Bóc tách kích thước (Số lượng × Dài × Rộng × Cao) và danh mục thiết bị công trình.
3. **Giá VL - NC - Máy**: Điều chỉnh đơn giá vật liệu theo công bố giá địa phương, đơn giá nhân công và giá ca máy theo TT 37/2026/TT-BXD.
4. **Phân tích Vật tư & Đơn giá**: Chiết tính chi tiết hao phí VL, NC, M cho từng công tác theo TT 38/2026/TT-BXD.
5. **TH Dự toán Chi phí XD (Bảng 3.8)**: Tổng hợp chi phí xây dựng hạng mục theo đúng mẫu Bảng 3.8 Phụ lục III TT 36/2026/TT-BXD (đã cập nhật đính chính QĐ 1538/QĐ-BXD).
6. **Tổng hợp Dự toán Công trình**: Tổng hợp 6 khoản mục ($G_{XD}, G_{TB}, G_{QLDA}, G_{TV}, G_K, G_{DP}$).
7. **Tra cứu Định mức & Nội suy**: Máy tính nội suy tuyến tính tự động Phụ lục VIII TT 38/2026/TT-BXD và thư viện định mức.

---

## 4. Lộ trình Mở rộng Đa Giai đoạn (Multi-Session Roadmap)

- **Giai đoạn 1 (Hoàn thành trong phiên hiện tại)**: Trọng tâm chuyên sâu **Công trình Dân dụng & Công nghiệp** (Trụ sở, trường học, bệnh viện, nhà xưởng sản xuất, kho vận công nghiệp).
- **Giai đoạn 2 (Phiên tiếp theo)**: Mở rộng bộ định mức chuyên ngành **Công trình Giao thông** (Đường bộ, cầu cống, nút giao, hầm giao thông).
- **Giai đoạn 3 (Phiên tiếp theo)**: Mở rộng bộ định mức chuyên ngành **Công trình Nông nghiệp & Phát triển nông thôn** (Thủy lợi, đê kè, hồ chứa, trạm bơm).
- **Giai đoạn 4 (Phiên tiếp theo)**: Mở rộng bộ định mức chuyên ngành **Công trình Hạ tầng kỹ thuật** (Cấp thoát nước đô thị, chiếu sáng, công viên cây xanh, xử lý nước thải).
