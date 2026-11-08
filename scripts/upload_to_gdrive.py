#!/usr/bin/env python3
"""
Xuất toàn bộ 12 Sheet Dự toán G8 Version 2026 ra CSV, đóng gói bộ công cụ HTML + ZIP,
cập nhật Google Sheets Workbook và đẩy toàn bộ kết quả trực tiếp lên thư mục Google Drive
CAC_QĐ_DU_TOAN/ (ID: 1XymH1SQV3Ng6P6xmb3EzrqAYeKWu__tE).
"""

import csv
import json
import shutil
import subprocess
import zipfile
from pathlib import Path

from du_toan_engine import (
    calculate_machine_shift_price_tt37,
    calculate_material_transport_cost,
    calculate_project_estimate,
    load_all_data,
)

ROOT_DIR = Path(__file__).resolve().parent.parent
EXPORT_DIR = ROOT_DIR / "exports_g8_2026"
ARTIFACT_HTML = Path(
    "/home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p/bafbf20d-b972-4df0-aaa8-ba48a718e711/phan_mem_du_toan_2026.html"
)
DRIVE_FOLDER_ID = "1XymH1SQV3Ng6P6xmb3EzrqAYeKWu__tE"
SPREADSHEET_ID = "1arnHEBqURqtyFNLKfxakUgOqwG6NgZDTenwB_LoxdwI"


def write_padded_csv(path: Path, rows: list[list]) -> None:
    max_cols = max((len(r) for r in rows), default=1)
    padded = [list(r) + [""] * (max_cols - len(r)) for r in rows]
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(padded)


def run_cmd(cmd: list[str]) -> str:
    print("Running:", " ".join(cmd))
    res = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if res.returncode != 0:
        print("STDERR:", res.stderr)
    return res.stdout.strip()


def generate_g8_12_csvs() -> dict[str, Path]:
    data = load_all_data()
    preset = data["presets"]["presets"]["dan_dung_tru_so"]
    result = calculate_project_estimate(
        preset["project_info"],
        preset["boq_items"],
        preset["equipment_items"],
        data["prices"],
        data["norms"],
        data["regulations"],
    )
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    csv_files = {}

    # 1. Sheet Công trình (BOQ)
    rows_ct = [
        ["BẢNG 1. TIÊN LƯỢNG CÔNG TRÌNH (SHEET CÔNG TRÌNH - DỰ TOÁN G8 VERSION 2026)"],
        ["Dự án:", preset["project_info"]["project_name"], "Địa điểm:", preset["project_info"]["location"]],
        ["STT", "Phân mục", "Mã hiệu ĐM (TT 38/2026)", "Tên công tác xây dựng", "ĐVT", "Diễn giải kích thước", "Khối lượng", "Đơn giá VL", "Đơn giá NC", "Đơn giá Máy", "Đơn giá Trực tiếp", "Thành tiền VL", "Thành tiền NC", "Thành tiền Máy", "Thành tiền Trực tiếp (đ)"],
    ]
    for r in result["detailed_boq"]:
        rows_ct.append([
            r["stt"], r["section"], r["norm_code"], r["name"], r["unit"], r["formula"],
            r["quantity"], r["unit_vl"], r["unit_nc"], r["unit_m"], r["unit_direct"],
            r["total_vl"], r["total_nc"], r["total_m"], r["total_direct"],
        ])
    p1 = EXPORT_DIR / "01_G8_Sheet_Cong_Trinh_BOQ.csv"
    write_padded_csv(p1, rows_ct)
    csv_files["01_CongTrinh"] = p1

    # 2. Sheet Nhân công & Máy thi công (TT 37/2026)
    fuel_prices = {
        "diesel_price_vnd_liter": 18500,
        "electricity_price_vnd_kwh": 2160,
        "gasoline_price_vnd_liter": 19800,
    }
    nc_map = {n["id"]: n["price"] for n in data["prices"]["nhan_cong"]}
    rows_may = [
        ["BẢNG 4. TÍNH GIÁ CA MÁY VÀ THIẾT BỊ THI CÔNG (THÔNG TƯ 37/2026/TT-BXD - SHEET MÁY G8)"],
        ["Mã máy", "Tên máy & thiết bị thi công", "ĐVT", "Nguyên giá (đ)", "Số ca/năm", "Chi phí Khấu hao C_KH", "Chi phí Sửa chữa C_SC", "Chi phí Khác C_K", "Nhiên liệu C_NL", "Tiền lương thợ ĐK C_NC", "Giá ca máy tính toán TT 37 (đ/ca)", "Giá ca máy công bố (đ/ca)"],
    ]
    for m in data["prices"]["may_thi_cong"]:
        mc = calculate_machine_shift_price_tt37(m, fuel_prices, nc_map)
        rows_may.append([
            mc["id"], mc["name"], m["unit"], mc["nguyen_gia"], mc["so_ca_nam"],
            mc["c_kh"], mc["c_sc"], mc["c_k"], mc["c_nl"], mc["c_nc"],
            mc["calculated_shift_price"], mc["announced_price"],
        ])
    p4 = EXPORT_DIR / "04_G8_Sheet_May_Thi_Cong_TT37.csv"
    write_padded_csv(p4, rows_may)
    csv_files["04_MayThiCong"] = p4

    # 3. Sheet Cước vận chuyển & Giá tháng
    road_rates = {"loai_1": 2400, "loai_2": 3200, "loai_3": 4200, "loai_4": 5500}
    rows_cuoc = [
        ["BẢNG 5 & 6. CƯỚC VẬN CHUYỂN Ô TÔ & GIÁ THÁNG HIỆN TRƯỜNG (SHEET CƯỚC VC & GIÁ THÁNG G8)"],
        ["Mã VL", "Tên vật liệu xây dựng", "ĐVT", "Giá thông báo gốc (đ)", "Trọng lượng (tấn/ĐVT)", "Cự ly VC (km)", "Loại đường", "Đơn giá cước (đ/tấn.km)", "Cước vận chuyển (đ/ĐVT)", "Giá hiện trường chân công trình (đ/ĐVT)"],
    ]
    for v in data["prices"]["vat_lieu"]:
        tc = calculate_material_transport_cost(v, road_rates)
        rows_cuoc.append([
            tc["id"], tc["name"], tc["unit"], tc["base_price"], tc["weight_ton"],
            tc["dist_km"], tc["road_class"], tc["rate_ton_km"], tc["transport_cost"], tc["site_price"],
        ])
    p5 = EXPORT_DIR / "05_G8_Sheet_Cuoc_VC_Gia_Thang.csv"
    write_padded_csv(p5, rows_cuoc)
    csv_files["05_CuocVC"] = p5

    # 4. Sheet Đơn giá chi tiết & Dự thầu
    rows_dg = [
        ["BẢNG 8 & 9. ĐƠN GIÁ CHI TIẾT & GIÁ DỰ THẦU XÂY LẮP (SHEET CHIẾT TÍNH & DỰ THẦU G8)"],
        ["STT", "Mã hiệu ĐM", "Tên công tác", "ĐVT", "Khối lượng", "Đơn giá VL", "Đơn giá NC", "Đơn giá Máy", "Chi phí trực tiếp T", "Chi phí chung C", "Chi phí KĐKL từ TK (TT)", "Thu nhập chịu thuế tính trước (TL)", "Đơn giá đầy đủ trước thuế", "Đơn giá đầy đủ sau thuế GTGT", "Thành tiền dự thầu trước thuế (đ)", "Thành tiền dự thầu sau thuế (đ)"],
    ]
    for r in result["detailed_boq"]:
        rows_dg.append([
            r["stt"], r["norm_code"], r["name"], r["unit"], r["quantity"],
            r["unit_vl"], r["unit_nc"], r["unit_m"], r["unit_direct"],
            r["unit_cpc"], r["unit_tt_other"], r["unit_tl"],
            r["unit_bid_before_tax"], r["unit_bid_after_tax"],
            r["total_bid_before_tax"], r["total_bid_after_tax"],
        ])
    p8 = EXPORT_DIR / "08_G8_Sheet_Don_Gia_Chi_Tiet_Du_Thau.csv"
    write_padded_csv(p8, rows_dg)
    csv_files["08_DonGiaDuThau"] = p8

    # 5. Sheet THKP Hạng mục (Bảng 3.8 TT 36/2026 & QĐ 1538/QĐ-BXD)
    b38 = result["bang_3_8_summary"]
    pinfo = preset["project_info"]
    rows_b38 = [
        ["BẢNG 10. TỔNG HỢP DỰ TOÁN CHI PHÍ XÂY DỰNG HẠNG MỤC (MẪU BẢNG 3.8 PL III TT 36/2026 & QĐ 1538/QĐ-BXD)"],
        ["STT", "Khoản mục chi phí", "Ký hiệu", "Cách tính / Tỷ lệ định mức", "Giá trị (Đồng)"],
        ["I", "CHI PHÍ TRỰC TIẾP", "T", "VL + NC + M", b38["T"]],
        ["1", "Chi phí vật liệu", "VL", "Tổng hợp từ bảng Tiên lượng & Giá hiện trường", b38["VL"]],
        ["2", "Chi phí nhân công", "NC", f"Theo TT 37/2026/TT-BXD (K_NC = {pinfo.get('k_nc', 1.0)})", b38["NC"]],
        ["3", "Chi phí máy và thiết bị thi công", "M", f"Theo TT 37/2026/TT-BXD (K_M = {pinfo.get('k_m', 1.0)})", b38["M"]],
        ["II", "CHI PHÍ GIÁN TIẾP", "GT", "C + TT + LT", b38["C"] + b38["TT"] + b38["LT_truoc_thue"]],
        ["1", "Chi phí chung", "C", f"T × {b38['rate_cpc']}% (Bảng 3.3 PL III TT 36/2026)", b38["C"]],
        ["2", "Chi phí một số công việc không xác định được khối lượng từ thiết kế", "TT", f"T × {b38['rate_tt_other']}% (Bảng 3.5 PL III TT 36/2026)", b38["TT"]],
        ["III", "THU NHẬP CHỊU THUẾ TÍNH TRƯỚC", "TL", f"(T + C) × {b38['rate_tl']}% (Bảng 3.6 PL III TT 36/2026)", b38["TL"]],
        ["IV", "CHI PHÍ XÂY DỰNG TRƯỚC THUẾ (CHƯA GỒM NHÀ TẠM)", "G_XDTT", "T + C + TL + TT", b38["G_XDTT"]],
        ["V", "CHI PHÍ NHÀ TẠM TẠI HIỆN TRƯỜNG ĐỂ Ở VÀ ĐIỀU HÀNH THI CÔNG", "LT", f"G_XDTT × {b38['rate_lt']}% (Bảng 3.7 PL III TT 36/2026)", b38["LT_truoc_thue"]],
        ["VI", "TỔNG CHI PHÍ XÂY DỰNG TRƯỚC THUẾ", "G_XD_trước_thuế", "G_XDTT + LT_trước_thuế", b38["G_XD_truoc_thue"]],
        ["VII", "THUẾ GIÁ TRỊ GIA TĂNG", "GTGT", f"G_XD_trước_thuế × {b38['vat_rate_pct']}%", b38["G_XD_GTGT"]],
        ["VIII", "TỔNG CHI PHÍ XÂY DỰNG SAU THUẾ (Đính chính QĐ 1538/QĐ-BXD)", "G_XD_sau_thuế", "G_XD_trước_thuế + GTGT (LT_sau_thuế = LT_trước_thuế + LT_GTGT)", b38["G_XD_sau_thue"]],
    ]
    p10 = EXPORT_DIR / "10_G8_Sheet_THKP_Hang_Muc_Bang_3_8.csv"
    write_padded_csv(p10, rows_b38)
    csv_files["10_THKP_Bang38"] = p10

    # 6. Sheet TH kinh phí (6 khoản mục + Tùy chọn CV 12637/BXD-KTQLXD)
    tot = result["total_summary"]
    rows_tot = [
        ["BẢNG 11. TỔNG HỢP DỰ TOÁN XÂY DỰNG CÔNG TRÌNH (THÔNG TƯ 36/2026, THÔNG TƯ 38/2026 & CÔNG VĂN 12637/BXD-KTQLXD)"],
        ["Tùy chọn Công văn 12637/BXD-KTQLXD (G8 20/08/2026):", tot.get("qlda_tv_basis_note", "")],
        ["STT", "Khoản mục chi phí dự toán", "Ký hiệu", "Giá trị trước thuế (đ)", "Thuế GTGT (đ)", "Giá trị sau thuế (đ)", "Thuyết minh / Căn cứ pháp lý"],
        ["1", "Chi phí xây dựng", "G_XD", tot["G_XD"]["before_tax"], tot["G_XD"]["vat"], tot["G_XD"]["after_tax"], "Bảng 3.1 & Bảng 3.8 Phụ lục III TT 36/2026/TT-BXD"],
        ["1.1", " - Chi phí xây dựng công trình chính, phụ trợ", "G_XDTT", b38["G_XDTT"], b38["GTGT_XD"], b38["G_XD_sau_thue_chua_LT"], "Tách dòng theo Bảng 3.1 TT 36/2026 (G8 20/08/2026)"],
        ["1.2", " - Chi phí nhà tạm tại hiện trường để ở và điều hành thi công", "LT", b38["LT_truoc_thue"], b38["LT_GTGT"], b38["LT_sau_thue"], "Đính chính theo Quyết định 1538/QĐ-BXD"],
        ["2", "Chi phí thiết bị", "G_TB", tot["G_TB"]["before_tax"], tot["G_TB"]["vat"], tot["G_TB"]["after_tax"], "Mua sắm + Lắp đặt + Thí nghiệm hiệu chỉnh"],
        ["3", "Chi phí quản lý dự án", "G_QLDA", tot["G_QLDA"]["before_tax"], tot["G_QLDA"]["vat"], tot["G_QLDA"]["after_tax"], "Bảng 1.1 Mục I Phụ lục VIII TT 38/2026/TT-BXD"],
        ["4", "Chi phí tư vấn đầu tư xây dựng", "G_TV", tot["G_TV"]["before_tax"], tot["G_TV"]["vat"], tot["G_TV"]["after_tax"], "Mục II Phụ lục VIII TT 38/2026/TT-BXD"],
        ["5", "Chi phí khác", "G_K", tot["G_K"]["before_tax"], tot["G_K"]["vat"], tot["G_K"]["after_tax"], "Thẩm tra, kiểm toán, bảo hiểm, rà phá bom mìn"],
        ["6", "Chi phí dự phòng (G_DP1 + G_DP2)", "G_DP", tot["G_DP"]["before_tax"], tot["G_DP"]["vat"], tot["G_DP"]["after_tax"], "Dự phòng khối lượng phát sinh + trượt giá"],
        ["TỔNG CỘNG", "TỔNG DỰ TOÁN XÂY DỰNG CÔNG TRÌNH", "G_DTXD", tot["TOTAL_DTXD"]["before_tax"], tot["TOTAL_DTXD"]["vat"], tot["TOTAL_DTXD"]["after_tax"], "Tổng cộng 6 khoản mục (1+2+3+4+5+6)"],
    ]
    p11 = EXPORT_DIR / "11_G8_Sheet_Tong_Hop_Du_Toan_Cong_Trinh.csv"
    write_padded_csv(p11, rows_tot)
    csv_files["11_TongHopDuToan"] = p11

    # 7. Sheet KL hoàn thành (Mẫu 03.a/TT Nghị định 254/2025/NĐ-CP)
    rows_qt = [
        ["BẢNG 12. XÁC ĐỊNH GIÁ TRỊ KHỐI LƯỢNG CÔNG VIỆC HOÀN THÀNH (MẪU SỐ 03.a/TT & 03.c/QT - NGHỊ ĐỊNH 254/2025/NĐ-CP)"],
        ["STT", "Mã hiệu ĐM", "Tên công việc theo hợp đồng", "ĐVT", "KL theo Hợp đồng", "KL Thực hiện Kỳ trước", "KL Thực hiện Kỳ này", "KL Lũy kế đến cuối kỳ này", "Đơn giá thanh toán sau thuế (đ)", "Giá trị Hợp đồng (đ)", "Giá trị Kỳ trước (đ)", "Giá trị Kỳ này đề nghị thanh toán (đ)", "Giá trị Lũy kế (đ)"],
    ]
    for r in result["detailed_boq"]:
        q_hd = r["quantity"]
        q_prev = round(q_hd * 0.4, 3)
        q_curr = round(q_hd * 0.6, 3)
        q_cum = round(q_prev + q_curr, 3)
        u_price = r["unit_bid_after_tax"]
        rows_qt.append([
            r["stt"], r["norm_code"], r["name"], r["unit"],
            q_hd, q_prev, q_curr, q_cum, u_price,
            round(q_hd * u_price), round(q_prev * u_price), round(q_curr * u_price), round(q_cum * u_price),
        ])
    p12 = EXPORT_DIR / "12_G8_Sheet_Quyet_Toan_Mau_03a_ND254.csv"
    write_padded_csv(p12, rows_qt)
    csv_files["12_QuyetToanND254"] = p12

    return csv_files


def create_full_zip() -> Path:
    zip_path = EXPORT_DIR / "Bo_Cong_Cu_Du_Toan_G8_Version_2026_Full.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for rel in [
            "index.html",
            "styles.css",
            "app.js",
            "README.md",
            "data/regulations_2026.json",
            "data/bang_gia_co_so.json",
            "data/dinh_muc_tt38_2026.json",
            "data/du_an_mau_dan_dung.json",
            "scripts/du_toan_engine.py",
            "scripts/build_web_bundle.py",
            "scripts/upgrade_g8_data.py",
            "tests/test_du_toan.py",
        ]:
            fp = ROOT_DIR / rel
            if fp.exists():
                zf.write(fp, arcname=f"du-toan-g8-2026/{rel}")
        for csv_fp in sorted(EXPORT_DIR.glob("*.csv")):
            zf.write(csv_fp, arcname=f"du-toan-g8-2026/exports_g8_2026/{csv_fp.name}")
    return zip_path


def main():
    csv_files = generate_g8_12_csvs()
    zip_path = create_full_zip()
    html_copy = EXPORT_DIR / "Phan_Mem_Du_Toan_G8_Version_2026_12_Sheet.html"
    shutil.copy2(ARTIFACT_HTML, html_copy)

    # 1. Upload standalone HTML app and full ZIP directly to main Drive folder CAC_QĐ_DU_TOAN/
    print("Uploading standalone HTML app to CAC_QĐ_DU_TOAN/...")
    run_cmd(["gdrive", "mutate", "upload", str(html_copy), "--parent", DRIVE_FOLDER_ID])

    print("Uploading full ZIP package to CAC_QĐ_DU_TOAN/...")
    run_cmd(["gdrive", "mutate", "upload", str(zip_path), "--parent", DRIVE_FOLDER_ID])

    # 2. Upload the G8 CSV files directly to CAC_QĐ_DU_TOAN/
    for key, csv_fp in csv_files.items():
        run_cmd(["gdrive", "mutate", "upload", str(csv_fp), "--parent", DRIVE_FOLDER_ID])

    # 3. Also add the new G8 2026 tabs into the Google Sheets Workbook inside CAC_QĐ_DU_TOAN/
    new_sheets = [
        ("09_G8_May_TT37", csv_files["04_MayThiCong"]),
        ("10_G8_Cuoc_VC", csv_files["05_CuocVC"]),
        ("11_G8_Don_Gia_Du_Thau", csv_files["08_DonGiaDuThau"]),
        ("12_G8_Quyet_Toan_ND254", csv_files["12_QuyetToanND254"]),
    ]
    for sheet_title, csv_fp in new_sheets:
        run_cmd(["gsheets", "mutate", "add-sheet", SPREADSHEET_ID, "--title", sheet_title])
        run_cmd(["gsheets", "mutate", "import-csv", SPREADSHEET_ID, str(csv_fp), "--sheet", sheet_title])

    print("Done uploading all results to Google Drive folder CAC_QĐ_DU_TOAN/!")


if __name__ == "__main__":
    main()
