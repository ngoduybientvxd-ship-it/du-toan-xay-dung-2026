#!/usr/bin/env python3
"""
Nâng cấp Cơ sở dữ liệu sang chuẩn DỰ TOÁN G8 VERSION 2026:
- Bổ sung dữ liệu định mức Ca máy theo Thông tư 37/2026/TT-BXD (Nguyên giá, số ca/năm, định mức Khấu hao, Sửa chữa, Chi phí khác, Tiêu hao nhiên liệu Diesel/Điện/Xăng, Hệ số thợ điều khiển máy)
- Bổ sung dữ liệu Cước vận chuyển vật liệu (Tỷ trọng tấn/ĐVT, cự ly vận chuyển km, cấp đường 1-4)
- Bổ sung thông tin Công văn 12637/BXD-KTQLXD ngày 11/08/2026, Nghị định 144/2025/NĐ-CP và Nghị định 254/2025/NĐ-CP vào regulations_2026.json
"""

import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

# 1. Cập nhật regulations_2026.json
reg_path = DATA_DIR / "regulations_2026.json"
reg = json.loads(reg_path.read_text(encoding="utf-8"))

existing_codes = {item["code"] for item in reg["metadata"]["legal_basis"]}
new_legal_docs = [
    {
        "code": "144/2025/NĐ-CP",
        "name": "Nghị định 144/2025/NĐ-CP của Chính phủ (Khoản 1 Điều 12)",
        "issued_date": "20/05/2025",
        "effective_date": "01/07/2025",
        "role": "Bãi bỏ quy định UBND cấp tỉnh công bố bộ đơn giá xây dựng công trình địa phương; Dự toán G8 tính trực tiếp từ Định mức 38/2026/TT-BXD kết hợp Giá tháng VL, NC, Máy."
    },
    {
        "code": "254/2025/NĐ-CP",
        "name": "Nghị định 254/2025/NĐ-CP của Chính phủ về quản lý, thanh toán, quyết toán dự án sử dụng vốn đầu tư công",
        "issued_date": "15/09/2025",
        "effective_date": "01/11/2025",
        "role": "Quy định biểu mẫu thanh toán, quyết toán mới: Mẫu số 03.a/TT (Bảng xác định giá trị KL công việc hoàn thành) và Mẫu số 03.c/QT (Quyết toán A-B)."
    },
    {
        "code": "12637/BXD-KTQLXD",
        "name": "Công văn số 12637/BXD-KTQLXD của Bộ Xây dựng (cập nhật trên G8 ngày 20/08/2026)",
        "issued_date": "11/08/2026",
        "effective_date": "11/08/2026",
        "role": "Hướng dẫn: Chi phí xây dựng để tính chi phí QLDA và Tư vấn XD là tổng của 3 khoản mục: Trực tiếp (T) + Gián tiếp (GT) + Thu nhập chịu thuế tính trước (TL) và KHÔNG bao gồm chi phí nhà tạm để ở và điều hành thi công (tùy chọn tích/bỏ tích 'Có nhà tạm' trên G8)."
    },
    {
        "code": "40/2026/TT-BXD",
        "name": "Thông tư 40/2026/TT-BXD của Bộ Xây dựng",
        "issued_date": "26/06/2026",
        "effective_date": "01/07/2026",
        "role": "Hướng dẫn xác định chi phí bảo trì công trình xây dựng."
    }
]
for doc in new_legal_docs:
    if doc["code"] not in existing_codes:
        reg["metadata"]["legal_basis"].append(doc)

reg["g8_input_defaults"] = {
    "diesel_price_vnd_liter": 18500,
    "gasoline_price_vnd_liter": 19800,
    "electricity_price_vnd_kwh": 2160,
    "road_class_rates_vnd_ton_km": {
        "loai_1": 2400,
        "loai_2": 2850,
        "loai_3": 3400,
        "loai_4": 4200
    }
}

reg_path.write_text(json.dumps(reg, ensure_ascii=False, indent=2), encoding="utf-8")

# 2. Cập nhật bang_gia_co_so.json với thông số Cước vận chuyển & Định mức Ca máy TT 37/2026/TT-BXD
prices_path = DATA_DIR / "bang_gia_co_so.json"
prices = json.loads(prices_path.read_text(encoding="utf-8"))

# Trọng lượng đơn vị (tấn/ĐVT) và cự ly vận chuyển mặc định cho Vật liệu
vl_transport_specs = {
    "VL001": {"weight_ton": 0.001, "dist_km": 15, "road_class": "loai_1"},
    "VL002": {"weight_ton": 1.350, "dist_km": 18, "road_class": "loai_2"},
    "VL003": {"weight_ton": 1.450, "dist_km": 22, "road_class": "loai_2"},
    "VL004": {"weight_ton": 1.550, "dist_km": 25, "road_class": "loai_2"},
    "VL005": {"weight_ton": 1.500, "dist_km": 25, "road_class": "loai_2"},
    "VL007": {"weight_ton": 0.0018, "dist_km": 12, "road_class": "loai_1"},
    "VL008": {"weight_ton": 0.0014, "dist_km": 12, "road_class": "loai_1"},
    "VL009": {"weight_ton": 0.001, "dist_km": 20, "road_class": "loai_1"},
    "VL010": {"weight_ton": 0.001, "dist_km": 20, "road_class": "loai_1"},
    "VL011": {"weight_ton": 0.001, "dist_km": 20, "road_class": "loai_1"},
    "VL012": {"weight_ton": 0.001, "dist_km": 20, "road_class": "loai_1"},
    "VL033": {"weight_ton": 0.156, "dist_km": 25, "road_class": "loai_1"},
}

for vl in prices["vat_lieu"]:
    spec = vl_transport_specs.get(vl["id"], {"weight_ton": 0.0, "dist_km": 0, "road_class": "loai_1"})
    vl["base_price"] = vl.get("base_price", vl["price"])
    vl["weight_ton"] = spec["weight_ton"]
    vl["dist_km"] = spec["dist_km"]
    vl["road_class"] = spec["road_class"]
    vl["transport_cost"] = vl.get("transport_cost", 0)

# Thông số định mức Ca máy theo Thông tư 37/2026/TT-BXD
machine_tt37_specs = {
    "M001": {"nguyen_gia": 1680000000, "so_ca_nam": 280, "khau_hao": 17.0, "sua_chua": 6.5, "khac": 5.0, "fuel_type": "diesel", "fuel_qty": 48.0, "nc_id": "NC002", "nc_qty": 1.0},
    "M002": {"nguyen_gia": 1420000000, "so_ca_nam": 270, "khau_hao": 17.0, "sua_chua": 6.2, "khac": 5.0, "fuel_type": "diesel", "fuel_qty": 42.0, "nc_id": "NC002", "nc_qty": 1.0},
    "M003": {"nguyen_gia": 18500000, "so_ca_nam": 190, "khau_hao": 22.0, "sua_chua": 7.5, "khac": 4.0, "fuel_type": "gasoline", "fuel_qty": 3.6, "nc_id": "NC001", "nc_qty": 1.0},
    "M004": {"nguyen_gia": 16200000, "so_ca_nam": 185, "khau_hao": 20.0, "sua_chua": 6.8, "khac": 4.0, "fuel_type": "electric", "fuel_qty": 14.5, "nc_id": "NC001", "nc_qty": 1.0},
    "M005": {"nguyen_gia": 11500000, "so_ca_nam": 180, "khau_hao": 20.0, "sua_chua": 6.5, "khac": 4.0, "fuel_type": "electric", "fuel_qty": 9.2, "nc_id": "NC001", "nc_qty": 0.9},
    "M006": {"nguyen_gia": 5800000, "so_ca_nam": 160, "khau_hao": 24.0, "sua_chua": 8.0, "khac": 4.0, "fuel_type": "electric", "fuel_qty": 6.8, "nc_id": "NC001", "nc_qty": 0.95},
    "M007": {"nguyen_gia": 5200000, "so_ca_nam": 160, "khau_hao": 24.0, "sua_chua": 8.0, "khac": 4.0, "fuel_type": "electric", "fuel_qty": 5.2, "nc_id": "NC001", "nc_qty": 0.95},
    "M008": {"nguyen_gia": 2150000000, "so_ca_nam": 250, "khau_hao": 16.5, "sua_chua": 6.0, "khac": 5.0, "fuel_type": "diesel", "fuel_qty": 56.0, "nc_id": "NC003", "nc_qty": 2.0},
    "M009": {"nguyen_gia": 19500000, "so_ca_nam": 200, "khau_hao": 19.0, "sua_chua": 6.5, "khac": 4.0, "fuel_type": "electric", "fuel_qty": 18.0, "nc_id": "NC001", "nc_qty": 1.0},
    "M010": {"nguyen_gia": 24000000, "so_ca_nam": 200, "khau_hao": 19.0, "sua_chua": 6.5, "khac": 4.0, "fuel_type": "electric", "fuel_qty": 62.0, "nc_id": "NC002", "nc_qty": 1.0},
    "M011": {"nguyen_gia": 68000000, "so_ca_nam": 220, "khau_hao": 18.0, "sua_chua": 6.5, "khac": 4.5, "fuel_type": "electric", "fuel_qty": 28.0, "nc_id": "NC002", "nc_qty": 1.0},
    "M012": {"nguyen_gia": 2850000000, "so_ca_nam": 260, "khau_hao": 15.0, "sua_chua": 5.8, "khac": 5.0, "fuel_type": "electric", "fuel_qty": 145.0, "nc_id": "NC003", "nc_qty": 2.0},
    "M013": {"nguyen_gia": 2450000000, "so_ca_nam": 250, "khau_hao": 15.5, "sua_chua": 6.0, "khac": 5.0, "fuel_type": "electric", "fuel_qty": 120.0, "nc_id": "NC003", "nc_qty": 2.0},
    "M014": {"nguyen_gia": 1180000000, "so_ca_nam": 280, "khau_hao": 16.5, "sua_chua": 6.2, "khac": 5.0, "fuel_type": "diesel", "fuel_qty": 36.0, "nc_id": "NC002", "nc_qty": 1.0},
}

for m in prices["may_thi_cong"]:
    sp = machine_tt37_specs.get(m["id"], {})
    m.update(sp)
    m["announced_price"] = m.get("announced_price", m["price"])

prices_path.write_text(json.dumps(prices, ensure_ascii=False, indent=2), encoding="utf-8")
print("Successfully upgraded regulations_2026.json and bang_gia_co_so.json with G8 2026 specs!")
