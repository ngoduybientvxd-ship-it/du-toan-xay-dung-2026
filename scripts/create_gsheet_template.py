#!/usr/bin/env python3
"""
Script tự động khởi tạo, nạp dữ liệu & công thức và định dạng Bảng tính Google Sheets
Dự toán Xây dựng Công trình Nguồn vốn Nhà nước (Hệ thống Pháp lý 2026)
Lưu trực tiếp vào thư mục Google Drive: CAC_QĐ_DU_TOAN/ (1XymH1SQV3Ng6P6xmb3EzrqAYeKWu__tE)
"""

import csv
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from du_toan_engine import calculate_project_estimate, load_all_data

ROOT = Path(__file__).resolve().parent.parent
CSV_DIR = ROOT / "exports" / "csv"
CSV_DIR.mkdir(parents=True, exist_ok=True)

DRIVE_FOLDER_ID = "1XymH1SQV3Ng6P6xmb3EzrqAYeKWu__tE"
SPREADSHEET_TITLE = "[DỰ TOÁN 2026] Dự Toán Xây Dựng Công Trình Dân Dụng & Công Nghiệp (NĐ 206/2026 & TT 36, 37, 38/2026)"


def run_cli(cmd: list[str]) -> str:
    print(">>", " ".join(cmd[:6]), "..." if len(cmd) > 6 else "")
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        print("STDERR:", proc.stderr)
        proc.check_returncode()
    return proc.stdout.strip()


def write_csv(filename: str, rows: list[list]) -> Path:
    path = CSV_DIR / filename
    max_cols = max((len(r) for r in rows), default=0)
    normalized_rows = [list(r) + [""] * (max_cols - len(r)) for r in rows]
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(normalized_rows)
    return path


def build_all_csvs(data: dict, calc: dict) -> dict[str, Path]:
    pi = calc["project_info"]
    b38 = calc["bang_3_8_summary"]
    tot = calc["total_summary"]

    # 1. 01_THONG_TIN_CHUNG
    rows_01 = [
        ["HỆ THỐNG TÍNH DỰ TOÁN XÂY DỰNG CÔNG TRÌNH NGUỒN VỐN NHÀ NƯỚC (CẬP NHẬT PHÁP LÝ 2026)", "", "", ""],
        ["Căn cứ: Luật XD 135/2025/QH15 | Nghị định 206/2026/NĐ-CP | Thông tư 36, 37, 38/2026/TT-BXD | Đính chính QĐ 1538/QĐ-BXD", "", "", ""],
        ["", "", "", ""],
        ["STT", "THÔNG SỐ DỰ ÁN & CẤU HÌNH ĐỊNH MỨC", "GIÁ TRỊ THIẾT LẬP", "CĂN CỨ PHÁP LÝ & GHI CHÚ"],
        [1, "Tên dự án đầu tư xây dựng", pi["project_name"], "Quyết định phê duyệt chủ trương đầu tư"],
        [2, "Tên công trình / Hạng mục", pi["building_name"], "Công trình Dân dụng cấp III"],
        [3, "Chủ đầu tư", pi["investor"], "Vốn đầu tư công (Ngân sách Nhà nước)"],
        [4, "Địa điểm xây dựng", pi["location"], "Áp dụng đơn giá NC, Máy vùng II"],
        [5, "Loại công trình", "Công trình Dân dụng", "Thông tư 36/2026/TT-BXD & Thông tư 38/2026/TT-BXD"],
        [6, "Cấp công trình", "Cấp III", "Thông tư 06/2021/TT-BXD"],
        [7, "Hình thức lập dự án", "Báo cáo Kinh tế - Kỹ thuật (Thiết kế 1 bước)", "Khoản 2 Mục II.1 Phụ lục III TT 36/2026/TT-BXD"],
        [8, "Thuế suất GTGT (%)", pi["vat_rate"], "Nghị định quy định thuế GTGT hiện hành"],
        [9, "Hệ số điều chỉnh nhân công (K_NC)", pi["k_nc"], "Thông tư 37/2026/TT-BXD"],
        [10, "Hệ số điều chỉnh máy thi công (K_M)", pi["k_m"], "Thông tư 37/2026/TT-BXD"],
        [11, "Định mức Chi phí chung (%)", b38["rate_cpc"], "Bảng 3.3 PL III TT 36/2026 (Lấy cột ≤ 40 tỷ cho BCKTKT)"],
        [12, "Định mức Chi phí CV không xác định khối lượng từ TK (%)", b38["rate_tt_other"], "Bảng 3.5 PL III TT 36/2026"],
        [13, "Định mức Thu nhập chịu thuế tính trước (%)", b38["rate_tl"], "Bảng 3.6 PL III TT 36/2026"],
        [14, "Định mức Chi phí nhà tạm (%)", b38["rate_lt"], "Bảng 3.7, 3.8 PL III TT 36/2026 & Đính chính QĐ 1538/QĐ-BXD"],
        [15, "Định mức Chi phí Quản lý dự án nội suy (%)", calc["qlda_summary"]["rate_pct"], "Bảng 1.1 Phụ lục VIII Thông tư 38/2026/TT-BXD"],
        [16, "Tỷ lệ Dự phòng khối lượng phát sinh DP1 (%)", pi["contingency_volume_rate"], "Điều 12 Nghị định 206/2026/NĐ-CP"],
        [17, "Tỷ lệ Dự phòng trượt giá DP2 (%)", pi["contingency_escalation_rate"], "Điều 12 Nghị định 206/2026/NĐ-CP"],
    ]

    # 2. 02_DM_TT38_2026
    rows_02 = [
        ["THƯ VIỆN ĐỊNH MỨC DỰ TOÁN XÂY DỰNG CÔNG TRÌNH — THÔNG TƯ 38/2026/TT-BXD (PHỤ LỤC II & PHỤ LỤC III)", "", "", "", ""],
        ["STT", "Mã hiệu ĐM", "Nhóm chương định mức", "Tên công tác xây dựng & lắp đặt", "Đơn vị tính", "Thành phần hao phí định mức (VL / NC / M)"],
    ]
    for i, n in enumerate(data["norms"], start=1):
        comp_str = " | ".join(
            [f"VL {x['id']}:{x['qty']}" for x in n.get("vl", [])]
            + [f"NC {x['id']}:{x['qty']}" for x in n.get("nc", [])]
            + [f"M {x['id']}:{x['qty']}" for x in n.get("m", [])]
        )
        rows_02.append([i, n["code"], n["category"], n["name"], n["unit"], comp_str])

    # 3. 03_GIA_VL_NC_M
    rows_03 = [
        ["BẢNG GIÁ VẬT LIỆU, NHÂN CÔNG, MÁY THI CÔNG & TỔNG HỢP HAO PHÍ TOÀN CÔNG TRÌNH (THÔNG TƯ 37/2026/TT-BXD)", "", "", "", "", "", "", ""],
        ["STT", "Mã VT", "Nhóm", "Tên Vật liệu / Nhân công / Máy thi công", "ĐVT", "Đơn giá gốc (VNĐ)", "Tổng hao phí dự án", "Tổng thành tiền (VNĐ)", "Nguồn công bố"],
    ]
    agg_map = {r["resource_id"]: r for r in calc["summary_resources"]}
    all_res = (
        [(r, "VL") for r in data["prices"]["vat_lieu"]]
        + [(r, "NC") for r in data["prices"]["nhan_cong"]]
        + [(r, "M") for r in data["prices"]["may_thi_cong"]]
    )
    for idx, (r, rtype) in enumerate(all_res, start=1):
        row_num = idx + 2
        agg = agg_map.get(r["id"], {"total_qty": 0.0})
        rows_03.append([
            idx,
            r["id"],
            rtype,
            r["name"],
            r["unit"],
            r["price"],
            round(agg["total_qty"], 3),
            f"=ROUND(F{row_num}*G{row_num}, 0)",
            r.get("source", ""),
        ])

    # 4. 04_TIEN_LUONG_BOQ
    rows_04 = [
        ["BẢNG TIÊN LƯỢNG & BÓC TÁCH KHỐI LƯỢNG XÂY DỰNG (BOQ) — TÍCH HỢP ĐƠN GIÁ CHI TIẾT TT 38/2026/TT-BXD", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["STT", "Hạng mục", "Mã ĐM TT38", "Tên công tác xây dựng", "ĐVT", "Số bộ phận", "Dài (m)", "Rộng (m)", "Cao/Dày (m)", "Khối lượng", "ĐG Vật liệu", "ĐG Nhân công", "ĐG Máy", "ĐG Trực tiếp", "Thành tiền Trực tiếp (VNĐ)"],
    ]
    for idx, b in enumerate(calc["detailed_boq"], start=1):
        rnum = idx + 2
        rows_04.append([
            b["stt"],
            b["section"],
            b["norm_code"],
            b["name"],
            b["unit"],
            b["count"],
            b["length"],
            b["width"],
            b["height"],
            f"=ROUND(F{rnum}*G{rnum}*H{rnum}*I{rnum}, 3)",
            b["unit_vl"],
            b["unit_nc"],
            b["unit_m"],
            f"=K{rnum}+L{rnum}+M{rnum}",
            f"=ROUND(J{rnum}*N{rnum}, 0)",
        ])
    end_boq_row = len(calc["detailed_boq"]) + 2
    rows_04.append([
        "TỔNG",
        "",
        "",
        "TỔNG CỘNG CHI PHÍ TRỰC TIẾP (T = VL + NC + M)",
        "",
        "",
        "",
        "",
        "",
        "",
        f"=SUMPRODUCT(J3:J{end_boq_row}, K3:K{end_boq_row})",
        f"=SUMPRODUCT(J3:J{end_boq_row}, L3:L{end_boq_row})",
        f"=SUMPRODUCT(J3:J{end_boq_row}, M3:M{end_boq_row})",
        "",
        f"=SUM(O3:O{end_boq_row})",
    ])

    # 5. 05_PHAN_TICH_DON_GIA
    rows_05 = [
        ["BẢNG PHÂN TÍCH VẬT TƯ & CHIẾT TÍNH ĐƠN GIÁ XÂY DỰNG CHI TIẾT (THÔNG TƯ 38/2026/TT-BXD)", "", "", "", "", "", "", "", ""],
        ["STT BOQ", "Mã ĐM", "Tên công tác xây dựng", "Loại HP", "Mã VT", "Tên Vật liệu / Nhân công / Máy", "ĐVT", "Định mức hao phí", "Khối lượng hao phí", "Đơn giá (VNĐ)", "Thành tiền (VNĐ)"],
    ]
    for mrow in calc["material_analysis_rows"]:
        rows_05.append([
            mrow["boq_stt"],
            mrow["norm_code"],
            mrow["work_name"],
            mrow["resource_type"],
            mrow["resource_id"],
            mrow["resource_name"],
            mrow["resource_unit"],
            mrow["norm_qty"],
            mrow["total_qty"],
            mrow["unit_price"],
            mrow["total_cost"],
        ])

    # 6. 06_BANG_3_8_CHI_PHI_XD
    total_row_boq = end_boq_row + 1
    rows_06 = [
        ["BẢNG 3.8 — BẢNG TỔNG HỢP DỰ TOÁN CHI PHÍ XÂY DỰNG (PHỤ LỤC III TT 36/2026/TT-BXD & ĐÍNH CHÍNH QĐ 1538/QĐ-BXD)", "", "", "", "", ""],
        ["STT", "KHOẢN MỤC CHI PHÍ", "CÔNG THỨC XÁC ĐỊNH", "TỶ LỆ (%)", "KÝ HIỆU", "GIÁ TRỊ (ĐỒNG)", "CĂN CỨ PHÁP LÝ"],
        ["I", "CHI PHÍ TRỰC TIẾP", "T = VL + NC + M", "", "T", "=SUM(F4:F6)", "Tổng hợp từ Bảng 04_TIEN_LUONG_BOQ"],
        ["1", "Chi phí vật liệu", "∑ (KL_i × ĐG_VL_i)", "", "VL", f"=ROUND('04_TIEN_LUONG_BOQ'!K{total_row_boq}, 0)", "Theo công bố giá VLXD địa phương"],
        ["2", "Chi phí nhân công", "∑ (KL_i × ĐG_NC_i) × K_NC", "", "NC", f"=ROUND('04_TIEN_LUONG_BOQ'!L{total_row_boq}, 0)", "Thông tư 37/2026/TT-BXD"],
        ["3", "Chi phí máy và thiết bị thi công", "∑ (KL_i × ĐG_M_i) × K_M", "", "M", f"=ROUND('04_TIEN_LUONG_BOQ'!M{total_row_boq}, 0)", "Thông tư 37/2026/TT-BXD"],
        ["II", "CHI PHÍ GIÁN TIẾP (Chưa gồm nhà tạm)", "C + TT", "", "GT", "=F8+F9", "Điều 13 Nghị định 206/2026/NĐ-CP"],
        ["1", "Chi phí chung", "T × Định mức CPC (%)", b38["rate_cpc"], "C", "=ROUND(F3*D8/100, 0)", "Bảng 3.3 Phụ lục III TT 36/2026/TT-BXD"],
        ["2", "Chi phí một số công việc không xác định được khối lượng từ thiết kế", "T × Định mức TT (%)", b38["rate_tt_other"], "TT", "=ROUND(F3*D9/100, 0)", "Bảng 3.5 Phụ lục III TT 36/2026/TT-BXD"],
        ["III", "THU NHẬP CHỊU THUẾ TÍNH TRƯỚC", "(T + C) × Định mức TL (%)", b38["rate_tl"], "TL", "=ROUND((F3+F8)*D10/100, 0)", "Bảng 3.6 Phụ lục III TT 36/2026/TT-BXD"],
        ["IV", "CHI PHÍ XÂY DỰNG TRƯỚC THUẾ (Chưa gồm nhà tạm)", "G = T + C + TL + TT", "", "G_XDTT", "=F3+F8+F9+F10", "Bảng 3.8 Phụ lục III TT 36/2026/TT-BXD"],
        ["V", "THUẾ GIÁ TRỊ GIA TĂNG XÂY DỰNG", "G_XDTT × T_GTGT (%)", b38["vat_rate_pct"], "GTGT", "=ROUND(F11*D12/100, 0)", "Thuế suất GTGT hiện hành"],
        ["VI", "CHI PHÍ XÂY DỰNG SAU THUẾ (Chưa gồm nhà tạm)", "G_XDTT + GTGT", "", "G_XDST", "=F11+F12", "Bảng 3.8 Phụ lục III TT 36/2026/TT-BXD"],
        ["VII", "CHI PHÍ NHÀ TẠM ĐỂ Ở VÀ ĐIỀU HÀNH THI CÔNG (Trước thuế)", "G_XDTT × Định mức LT (%)", b38["rate_lt"], "LT_TT", "=ROUND(F11*D14/100, 0)", "Bảng 3.7 Phụ lục III TT 36/2026/TT-BXD"],
        ["VIII", "CHI PHÍ NHÀ TẠM ĐỂ Ở VÀ ĐIỀU HÀNH THI CÔNG (Sau thuế)", "G_XDTT × Tỷ lệ × (1 + T_GTGT)", b38["rate_lt"], "LT", "=F14+ROUND(F14*D12/100, 0)", "Đính chính theo Quyết định 1538/QĐ-BXD ngày 28/08/2026"],
        ["TỔNG", "TỔNG CHI PHÍ XÂY DỰNG HẠNG MỤC (TRƯỚC THUẾ, GỒM NHÀ TẠM)", "G_XDTT + LT_TT", "", "G_XD_TT", "=F11+F14", "Đưa vào Bảng Tổng hợp Dự toán Công trình"],
        ["TỔNG", "TỔNG CHI PHÍ XÂY DỰNG HẠNG MỤC (SAU THUẾ, GỒM NHÀ TẠM)", "G_XDST + LT", "", "G_XD", "=F13+F15", "Đưa vào Bảng Tổng hợp Dự toán Công trình"],
    ]

    # 7. 07_DU_TOAN_CONG_TRINH
    rows_07 = [
        ["BẢNG TỔNG HỢP DỰ TOÁN XÂY DỰNG CÔNG TRÌNH (NGHỊ ĐỊNH 206/2026/NĐ-CP & THÔNG TƯ 36, 38/2026/TT-BXD)", "", "", "", "", "", ""],
        ["STT", "NỘI DUNG KHOẢN MỤC CHI PHÍ", "CĂN CỨ PHÁP LÝ / ĐỊNH MỨC", "TỶ LỆ (%)", "TRƯỚC THUẾ (VNĐ)", "THUẾ GTGT (VNĐ)", "SAU THUẾ (VNĐ)"],
        ["I", "CHI PHÍ XÂY DỰNG (G_XD)", "Bảng 3.8 PL III TT 36/2026 & QĐ 1538/QĐ-BXD", "", "='06_BANG_3_8_CHI_PHI_XD'!F16", "='06_BANG_3_8_CHI_PHI_XD'!F17-E3", "='06_BANG_3_8_CHI_PHI_XD'!F17"],
        ["II", "CHI PHÍ THIẾT BỊ (G_TB)", "Chương II Thông tư 36/2026/TT-BXD", "", tot["G_TB"]["before_tax"], "=ROUND(E4*0.08, 0)", "=E4+F4"],
        ["III", "CHI PHÍ QUẢN LÝ DỰ ÁN (G_QLDA)", "Bảng 1.1 Phụ lục VIII Thông tư 38/2026/TT-BXD", calc["qlda_summary"]["rate_pct"], "=ROUND((E3+E4)*D5/100, 0)", "=ROUND(E5*0.08, 0)", "=E5+F5"],
        ["IV", "CHI PHÍ TƯ VẤN ĐẦU TƯ XÂY DỰNG (G_TV)", "Phần II Phụ lục VIII Thông tư 38/2026/TT-BXD", "", tot["G_TV"]["before_tax"], tot["G_TV"]["vat"], "=E6+F6"],
        ["V", "CHI PHÍ KHÁC (G_K)", "Điều 11 Nghị định 206/2026/NĐ-CP", "", tot["G_K"]["before_tax"], tot["G_K"]["vat"], "=E7+F7"],
        ["CỘNG", "TỔNG CỘNG TRƯỚC DỰ PHÒNG (I + II + III + IV + V)", "Cơ sở tính chi phí dự phòng", "", "=SUM(E3:E7)", "=SUM(F3:F7)", "=SUM(G3:G7)"],
        ["VI", "CHI PHÍ DỰ PHÒNG (G_DP = G_DP1 + G_DP2)", "Điều 12 Nghị định 206/2026/NĐ-CP", pi["contingency_volume_rate"] + pi["contingency_escalation_rate"], "=E10+E11", "=F10+F11", "=G10+G11"],
        ["6.1", "Dự phòng khối lượng công việc phát sinh (G_DP1)", "5,0% × Tổng trước dự phòng", pi["contingency_volume_rate"], "=ROUND(E8*D10/100, 0)", "=ROUND(F8*D10/100, 0)", "=E10+F10"],
        ["6.2", "Dự phòng cho yếu tố trượt giá (G_DP2)", "2,5% × Tổng trước dự phòng", pi["contingency_escalation_rate"], "=ROUND(E8*D11/100, 0)", "=ROUND(F8*D11/100, 0)", "=E11+F11"],
        ["TỔNG", "TỔNG DỰ TOÁN XÂY DỰNG CÔNG TRÌNH (G_DTXD)", "I + II + III + IV + V + VI", "", "=E8+E9", "=F8+F9", "=G8+G9"],
    ]

    # 8. 08_BANG_TRA_NOI_SUY
    b33 = data["regulations"]["tt36_phu_luc_3"]["bang_3_3_cpc_du_toan"]
    b11 = data["regulations"]["tt38_phu_luc_8"]["bang_1_1_qlda"]
    rows_08 = [
        ["BẢNG TRA ĐỊNH MỨC CHI PHÍ CHUNG (BẢNG 3.3 TT 36/2026) & ĐỊNH MỨC QLDA, TƯ VẤN (PHỤ LỤC VIII TT 38/2026)", "", "", "", "", "", "", "", ""],
        ["PHẦN A: BẢNG 3.3 — ĐỊNH MỨC CHI PHÍ CHUNG TÍNH TRÊN CHI PHÍ TRỰC TIẾP (%) — TRA CẬN TRÊN THEO DẤU ≤", "", "", "", "", "", "", "", ""],
        ["Loại công trình", "≤ 40 tỷ", "≤ 60 tỷ", "≤ 100 tỷ", "≤ 300 tỷ", "≤ 500 tỷ", "≤ 750 tỷ", "≤ 1.000 tỷ", "> 1.000 tỷ"],
        ["1. Công trình Dân dụng", *b33["rates"]["dan_dung"]],
        ["— Tu bổ, phục hồi di tích", *b33["rates"]["dan_dung_di_tich"]],
        ["2. Công trình Công nghiệp", *b33["rates"]["cong_nghiep"]],
        ["— Công trình hầm thủy điện, hầm lò", *b33["rates"]["cong_nghiep_ham"]],
        ["3. Công trình Giao thông", *b33["rates"]["giao_thong"]],
        ["4. Công trình Nông nghiệp & PTNT", *b33["rates"]["nong_nghiep"]],
        ["5. Công trình Hạ tầng kỹ thuật", *b33["rates"]["ha_tang_ky_thuat"]],
        ["", "", "", "", "", "", "", "", ""],
        ["PHẦN B: BẢNG 1.1 PHỤ LỤC VIII TT 38/2026 — ĐỊNH MỨC CHI PHÍ QUẢN LÝ DỰ ÁN (%) — NỘI SUY TUYẾN TÍNH", "", "", "", "", "", "", "", ""],
        ["Loại công trình / Quy mô (Tỷ đồng)", *b11["thresholds_ty_dong"][:8]],
        ["1. Công trình Dân dụng", *b11["rates"]["dan_dung"][:8]],
        ["2. Công trình Công nghiệp", *b11["rates"]["cong_nghiep"][:8]],
        ["3. Công trình Giao thông", *b11["rates"]["giao_thong"][:8]],
        ["4. Công trình Nông nghiệp & PTNT", *b11["rates"]["nong_nghiep"][:8]],
        ["5. Công trình Hạ tầng kỹ thuật", *b11["rates"]["ha_tang_ky_thuat"][:8]],
    ]

    return {
        "01_THONG_TIN_CHUNG": write_csv("01_THONG_TIN_CHUNG.csv", rows_01),
        "02_DM_TT38_2026": write_csv("02_DM_TT38_2026.csv", rows_02),
        "03_GIA_VL_NC_M": write_csv("03_GIA_VL_NC_M.csv", rows_03),
        "04_TIEN_LUONG_BOQ": write_csv("04_TIEN_LUONG_BOQ.csv", rows_04),
        "05_PHAN_TICH_DON_GIA": write_csv("05_PHAN_TICH_DON_GIA.csv", rows_05),
        "06_BANG_3_8_CHI_PHI_XD": write_csv("06_BANG_3_8_CHI_PHI_XD.csv", rows_06),
        "07_DU_TOAN_CONG_TRINH": write_csv("07_DU_TOAN_CONG_TRINH.csv", rows_07),
        "08_BANG_TRA_NOI_SUY": write_csv("08_BANG_TRA_NOI_SUY.csv", rows_08),
    }


def main():
    data = load_all_data()
    preset = data["presets"]["presets"]["dan_dung_tru_so"]
    calc = calculate_project_estimate(
        preset["project_info"],
        preset["boq_items"],
        preset["equipment_items"],
        data["prices"],
        data["norms"],
        data["regulations"],
    )
    csv_files = build_all_csvs(data, calc)
    print("Generated 8 CSV sheets in:", CSV_DIR)

    # 1. Use created Google Sheet ID (already moved into CAC_QĐ_DU_TOAN/ and 8 sheets created)
    spreadsheet_id = "1arnHEBqURqtyFNLKfxakUgOqwG6NgZDTenwB_LoxdwI"
    print("Using Spreadsheet ID:", spreadsheet_id)

    # 2. Import all 8 CSVs into their respective sheets
    import_order = [
        "01_THONG_TIN_CHUNG",
        "02_DM_TT38_2026",
        "03_GIA_VL_NC_M",
        "04_TIEN_LUONG_BOQ",
        "05_PHAN_TICH_DON_GIA",
        "06_BANG_3_8_CHI_PHI_XD",
        "07_DU_TOAN_CONG_TRINH",
        "08_BANG_TRA_NOI_SUY",
    ]
    for sname in import_order:
        run_cli(["gsheets", "mutate", "import-csv", spreadsheet_id, str(csv_files[sname]), "--sheet", sname])

    # 5. Format Title & Header rows on first sheet (sheet-id 0)
    run_cli([
        "gsheets", "mutate", "format", spreadsheet_id,
        "--sheet-id", "0",
        "--start-row", "1", "--end-row", "4",
        "--start-col", "1", "--end-col", "4",
        "--bold", "--bg-color", "#0F172A", "--fg-color", "#FFFFFF"
    ])

    url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/edit"
    meta_out = ROOT / "exports" / "google_sheet_info.json"
    meta_out.write_text(json.dumps({
        "spreadsheet_id": spreadsheet_id,
        "title": SPREADSHEET_TITLE,
        "url": url,
        "drive_folder_id": DRIVE_FOLDER_ID,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print("DONE! Google Sheet URL:", url)


if __name__ == "__main__":
    main()
