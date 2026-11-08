#!/usr/bin/env python3
"""
Bộ máy tính toán Chuyên gia DỰ TOÁN G8 VERSION 2026 (Nguồn vốn Nhà nước)
Cập nhật toàn diện hệ thống pháp lý & hướng dẫn mới nhất đến tháng 11/2026:
1. Luật Xây dựng số 135/2025/QH15 (hiệu lực 01/01/2026)
2. Nghị định 144/2025/NĐ-CP (Khoản 1 Điều 12: bỏ sách đơn giá tỉnh, tính trực tiếp từ Định mức BXD)
3. Nghị định 254/2025/NĐ-CP (Mẫu 03.a/TT & Mẫu 03.c/QT thanh quyết toán vốn đầu tư công)
4. Nghị định 206/2026/NĐ-CP ngày 15/06/2026 về quản lý chi phí đầu tư xây dựng
5. Thông tư 36/2026/TT-BXD ngày 26/06/2026 hướng dẫn xác định và quản lý chi phí ĐTXD
6. Quyết định 1538/QĐ-BXD ngày 28/08/2026 đính chính Thông tư 36/2026/TT-BXD
7. Công văn 12637/BXD-KTQLXD ngày 11/08/2026 của Bộ Xây dựng (cập nhật G8 ngày 20/08/2026):
   Hướng dẫn Chi phí xây dựng làm cơ sở tính QLDA và Tư vấn ĐTXD (tùy chọn Có/Không gồm Chi phí nhà tạm)
8. Thông tư 37/2026/TT-BXD ngày 26/06/2026 hướng dẫn định mức, giá nhân công & giá ca máy
9. Thông tư 38/2026/TT-BXD ngày 26/06/2026 ban hành Định mức xây dựng (Phụ lục II, III, VIII)
10. Thông tư 40/2026/TT-BXD ngày 26/06/2026 hướng dẫn chi phí bảo trì công trình xây dựng
"""

from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Dict, List, Optional


DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def load_all_data(data_dir: Path = DATA_DIR) -> Dict[str, Any]:
    """Đọc toàn bộ cơ sở dữ liệu JSON của dự án."""
    with open(data_dir / "regulations_2026.json", "r", encoding="utf-8") as f:
        regulations = json.load(f)
    with open(data_dir / "bang_gia_co_so.json", "r", encoding="utf-8") as f:
        prices = json.load(f)
    with open(data_dir / "dinh_muc_tt38_2026.json", "r", encoding="utf-8") as f:
        norms = json.load(f)
    with open(data_dir / "du_an_mau_dan_dung.json", "r", encoding="utf-8") as f:
        presets = json.load(f)
    return {
        "regulations": regulations,
        "prices": prices,
        "norms": norms,
        "presets": presets,
    }


def calculate_machine_shift_price_tt37(
    machine: Dict[str, Any],
    fuel_prices: Dict[str, float],
    nc_price_map: Dict[str, float],
) -> Dict[str, Any]:
    """
    Tính Giá ca máy và thiết bị thi công theo Thông tư 37/2026/TT-BXD (Sheet 'Máy' trong Dự toán G8):
        C_CM = C_KH + C_SC + C_NL + C_NC + C_K
    Trong đó:
        - C_KH = (Nguyên giá × Định mức khấu hao %/năm) / Số ca năm
        - C_SC = (Nguyên giá × Định mức sửa chữa %/năm) / Số ca năm
        - C_K  = (Nguyên giá × Định mức chi phí khác %/năm) / Số ca năm
        - C_NL = Định mức tiêu hao nhiên liệu × Đơn giá nhiên liệu (Diesel / Điện / Xăng) × Hệ số nhiên liệu phụ (1.03)
        - C_NC = Thành phần cấp bậc thợ điều khiển máy × Đơn giá nhân công
    """
    nguyen_gia = float(machine.get("nguyen_gia", 0.0))
    so_ca_nam = max(float(machine.get("so_ca_nam", 250.0)), 1.0)
    kh_pct = float(machine.get("khau_hao", 16.0)) / 100.0
    sc_pct = float(machine.get("sua_chua", 6.0)) / 100.0
    khac_pct = float(machine.get("khac", 5.0)) / 100.0

    c_kh = round((nguyen_gia * kh_pct) / so_ca_nam, 0)
    c_sc = round((nguyen_gia * sc_pct) / so_ca_nam, 0)
    c_k = round((nguyen_gia * khac_pct) / so_ca_nam, 0)

    fuel_type = machine.get("fuel_type", "diesel")
    fuel_qty = float(machine.get("fuel_qty", 0.0))
    if fuel_type == "diesel":
        fuel_unit_price = float(fuel_prices.get("diesel_price_vnd_liter", 18500.0))
        kp_coeff = 1.03  # Hệ số nhiên liệu phụ cho động cơ diesel
    elif fuel_type == "gasoline":
        fuel_unit_price = float(fuel_prices.get("gasoline_price_vnd_liter", 19800.0))
        kp_coeff = 1.02
    else:
        fuel_unit_price = float(fuel_prices.get("electricity_price_vnd_kwh", 2160.0))
        kp_coeff = 1.00

    c_nl = round(fuel_qty * fuel_unit_price * kp_coeff, 0)

    nc_id = machine.get("nc_id", "NC002")
    nc_qty = float(machine.get("nc_qty", 1.0))
    nc_unit_price = float(nc_price_map.get(nc_id, 322000.0))
    c_nc = round(nc_qty * nc_unit_price, 0)

    c_cm = c_kh + c_sc + c_nl + c_nc + c_k
    return {
        "id": machine["id"],
        "name": machine["name"],
        "nguyen_gia": nguyen_gia,
        "so_ca_nam": so_ca_nam,
        "c_kh": c_kh,
        "c_sc": c_sc,
        "c_nl": c_nl,
        "c_nc": c_nc,
        "c_k": c_k,
        "calculated_shift_price": c_cm,
        "announced_price": float(machine.get("announced_price", machine.get("price", c_cm))),
    }


def calculate_material_transport_cost(
    vl: Dict[str, Any],
    road_rates: Dict[str, float],
) -> Dict[str, Any]:
    """
    Tính Cước vận chuyển vật liệu đến chân công trình (Sheet 'Cước VC' trong Dự toán G8):
        Cước VC (đ/ĐVT) = Trọng lượng đơn vị (tấn/ĐVT) × Cự ly (km) × Đơn giá cước theo loại đường (đ/tấn.km)
    """
    weight_ton = float(vl.get("weight_ton", 0.0))
    dist_km = float(vl.get("dist_km", 0.0))
    road_class = vl.get("road_class", "loai_1")
    rate_ton_km = float(road_rates.get(road_class, 2400.0))
    transport_cost = round(weight_ton * dist_km * rate_ton_km, 0)
    base_price = float(vl.get("base_price", vl.get("price", 0.0)))
    return {
        "id": vl["id"],
        "name": vl["name"],
        "unit": vl["unit"],
        "base_price": base_price,
        "weight_ton": weight_ton,
        "dist_km": dist_km,
        "road_class": road_class,
        "rate_ton_km": rate_ton_km,
        "transport_cost": transport_cost,
        "site_price": base_price + transport_cost,
    }


def step_lookup_le(
    value_ty_dong: float,
    thresholds: List[float],
    rates: List[float],
    labels: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Tra định mức theo ngưỡng cận trên có dấu '≤' (Bảng 3.3 & Bảng 3.7 Phụ lục III Thông tư 36/2026/TT-BXD).
    """
    for idx, threshold in enumerate(thresholds):
        if value_ty_dong <= threshold:
            label = labels[idx] if labels and idx < len(labels) else f"≤ {threshold}"
            return {
                "rate": float(rates[idx]),
                "matched_index": idx,
                "matched_threshold_ty": threshold,
                "matched_label": label,
                "method": "Tra cận trên theo cột có dấu ≤ (TT 36/2026/TT-BXD)",
            }
    last_idx = len(rates) - 1
    label = labels[last_idx] if labels and last_idx < len(labels) else f"> {thresholds[-2]}"
    return {
        "rate": float(rates[last_idx]),
        "matched_index": last_idx,
        "matched_threshold_ty": thresholds[last_idx],
        "matched_label": label,
        "method": "Tra cận trên theo cột > ngưỡng lớn nhất (TT 36/2026/TT-BXD)",
    }


def interpolate_rate_tt38(
    gt_ty_dong: float,
    thresholds: List[float],
    rates: List[float],
) -> Dict[str, Any]:
    """
    Nội suy tuyến tính định mức tỷ lệ phần trăm (%) theo Phụ lục VIII Thông tư 38/2026/TT-BXD:
        N_t = N_b - ((N_b - N_a) / (G_a - G_b)) * (G_t - G_b)
    """
    if not thresholds or not rates or len(thresholds) != len(rates):
        raise ValueError("Danh sách thresholds và rates phải có cùng độ dài và khác rỗng.")

    if gt_ty_dong <= thresholds[0]:
        return {
            "rate": round(float(rates[0]), 4),
            "gt": round(gt_ty_dong, 6),
            "gb": thresholds[0],
            "ga": thresholds[0],
            "nb": float(rates[0]),
            "na": float(rates[0]),
            "formula_text": f"G_t = {gt_ty_dong:.3f} tỷ ≤ {thresholds[0]} tỷ ⇒ N_t = {rates[0]:.3f}%",
        }

    for i in range(len(thresholds) - 1):
        gb = float(thresholds[i])
        ga = float(thresholds[i + 1])
        nb = float(rates[i])
        na = float(rates[i + 1])
        if gb <= gt_ty_dong <= ga:
            nt = nb if ga == gb else nb - ((nb - na) / (ga - gb)) * (gt_ty_dong - gb)
            nt_rounded = round(nt, 4)
            return {
                "rate": nt_rounded,
                "gt": round(gt_ty_dong, 6),
                "gb": gb,
                "ga": ga,
                "nb": nb,
                "na": na,
                "formula_text": (
                    f"N_t = {nb} - (({nb} - {na}) / ({ga} - {gb})) × ({gt_ty_dong:.3f} - {gb}) = {nt_rounded:.4f}%"
                ),
            }

    last_idx = len(thresholds) - 1
    return {
        "rate": round(float(rates[last_idx]), 4),
        "gt": round(gt_ty_dong, 6),
        "gb": thresholds[last_idx],
        "ga": thresholds[last_idx],
        "nb": float(rates[last_idx]),
        "na": float(rates[last_idx]),
        "formula_text": f"G_t = {gt_ty_dong:.3f} tỷ ≥ {thresholds[last_idx]} tỷ ⇒ N_t = {rates[last_idx]:.3f}%",
    }


def calculate_project_estimate(
    project_info: Dict[str, Any],
    boq_items: List[Dict[str, Any]],
    equipment_items: List[Dict[str, Any]],
    prices_data: Dict[str, List[Dict[str, Any]]],
    norms_list: List[Dict[str, Any]],
    regulations: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Thực hiện toàn bộ chuỗi tính toán của Phần mềm DỰ TOÁN G8 VERSION 2026:
      - Sheet Công trình -> Sheet Đầu vào -> Sheet Nhân công -> Sheet Máy -> Sheet Cước VC
      - Sheet Giá tháng -> Sheet Hao phí vật tư -> Sheet Đơn giá chi tiết -> Sheet Dự thầu
      - Sheet THKP Hạng mục (Bảng 3.8 TT 36/2026 & QĐ 1538/QĐ-BXD)
      - Sheet TH chi phí XD (Bảng 3.1 TT 36/2026 tách dòng Nhà tạm)
      - Sheet TH kinh phí (Tích hợp tùy chọn Công văn 12637/BXD-KTQLXD ngày 11/08/2026)
      - Sheet KL hoàn thành (Mẫu 03.a/TT & 03.c/QT Nghị định 254/2025/NĐ-CP)
    """
    vl_map = {item["id"]: item for item in prices_data.get("vat_lieu", [])}
    nc_map = {item["id"]: item for item in prices_data.get("nhan_cong", [])}
    m_map = {item["id"]: item for item in prices_data.get("may_thi_cong", [])}
    res_map = {**vl_map, **nc_map, **m_map}
    norm_map = {n["code"]: n for n in norms_list}

    k_nc = float(project_info.get("k_nc", 1.0))
    k_m = float(project_info.get("k_m", 1.0))
    vat_rate = float(project_info.get("vat_rate", 8.0)) / 100.0
    building_type = project_info.get("building_type", "dan_dung")
    building_grade = project_info.get("building_grade", "cap_3")
    design_step = project_info.get("design_step", "tkbvtc_2_buoc")
    is_bcktkt = bool(project_info.get("is_bcktkt", False))
    is_mountain_island = bool(project_info.get("is_mountain_island", False))
    # Tùy chọn 'Có nhà tạm' khi tính QLDA & Tư vấn theo CV 12637/BXD-KTQLXD ngày 11/08/2026 (mặc định True hoặc theo cấu hình)
    include_lt_in_qlda_tv = bool(project_info.get("include_lt_in_qlda_tv", True))

    tt36 = regulations["tt36_phu_luc_3"]
    bang_3_3 = tt36["bang_3_3_cpc_du_toan"]
    cpc_rates_for_type = bang_3_3["rates"].get(building_type, bang_3_3["rates"]["dan_dung"])
    rate_tl = float(tt36["bang_3_6_thu_nhap_chiu_thue"]["rates"].get(building_type, 5.5))
    rate_tt_other = float(tt36["bang_3_5_chi_phi_tt"]["rates"].get(building_type, 2.5))

    detailed_boq: List[Dict[str, Any]] = []
    material_analysis_rows: List[Dict[str, Any]] = []
    aggregated_resources: Dict[str, Dict[str, Any]] = {}

    total_vl = 0.0
    total_nc = 0.0
    total_m = 0.0

    for idx, item in enumerate(boq_items, start=1):
        norm_code = item["norm_code"]
        norm = norm_map.get(norm_code)
        if not norm:
            raise KeyError(f"Không tìm thấy mã hiệu định mức: {norm_code}")

        qty = float(item.get("quantity", 0.0))
        unit_vl = 0.0
        unit_nc = 0.0
        unit_m = 0.0
        item_components: List[Dict[str, Any]] = []

        for comp_type, comp_list in [("VL", norm.get("vl", [])), ("NC", norm.get("nc", [])), ("M", norm.get("m", []))]:
            for comp in comp_list:
                res_id = comp["id"]
                norm_qty = float(comp["qty"])
                res_info = res_map.get(res_id, {"name": res_id, "unit": "", "price": 0.0})
                base_price = float(res_info["price"])

                if comp_type == "NC":
                    effective_price = base_price * k_nc
                elif comp_type == "M":
                    effective_price = base_price * k_m
                else:
                    effective_price = base_price + float(res_info.get("transport_cost", 0.0))

                comp_unit_cost = norm_qty * effective_price
                comp_total_qty = norm_qty * qty
                comp_total_cost = comp_total_qty * effective_price

                if comp_type == "VL":
                    unit_vl += comp_unit_cost
                elif comp_type == "NC":
                    unit_nc += comp_unit_cost
                elif comp_type == "M":
                    unit_m += comp_unit_cost

                comp_record = {
                    "boq_stt": idx,
                    "norm_code": norm_code,
                    "work_name": item.get("custom_name") or norm["name"],
                    "work_unit": norm["unit"],
                    "work_qty": qty,
                    "resource_type": comp_type,
                    "resource_id": res_id,
                    "resource_name": res_info["name"],
                    "resource_unit": res_info["unit"],
                    "norm_qty": norm_qty,
                    "total_qty": round(comp_total_qty, 4),
                    "unit_price": round(effective_price, 2),
                    "unit_cost": round(comp_unit_cost, 2),
                    "total_cost": round(comp_total_cost, 0),
                }
                item_components.append(comp_record)
                material_analysis_rows.append(comp_record)

                if res_id not in aggregated_resources:
                    aggregated_resources[res_id] = {
                        "resource_id": res_id,
                        "resource_type": comp_type,
                        "resource_name": res_info["name"],
                        "resource_unit": res_info["unit"],
                        "unit_price": round(effective_price, 2),
                        "total_qty": 0.0,
                        "total_cost": 0.0,
                    }
                aggregated_resources[res_id]["total_qty"] += comp_total_qty
                aggregated_resources[res_id]["total_cost"] += comp_total_cost

        line_vl = round(unit_vl * qty, 0)
        line_nc = round(unit_nc * qty, 0)
        line_m = round(unit_m * qty, 0)
        line_direct = line_vl + line_nc + line_m

        total_vl += line_vl
        total_nc += line_nc
        total_m += line_m

        detailed_boq.append({
            "stt": idx,
            "id": item.get("id", idx),
            "section": item.get("section", "I. PHẦN XÂY DỰNG"),
            "norm_code": norm_code,
            "name": item.get("custom_name") or norm["name"],
            "unit": norm["unit"],
            "formula": item.get("formula", str(qty)),
            "count": item.get("count", 1),
            "length": item.get("length", qty),
            "width": item.get("width", 1.0),
            "height": item.get("height", 1.0),
            "factor": item.get("factor", 1.0),
            "quantity": qty,
            "unit_vl": round(unit_vl, 0),
            "unit_nc": round(unit_nc, 0),
            "unit_m": round(unit_m, 0),
            "unit_direct": round(unit_vl + unit_nc + unit_m, 0),
            "total_vl": line_vl,
            "total_nc": line_nc,
            "total_m": line_m,
            "total_direct": line_direct,
            "components": item_components,
        })

    summary_resources = sorted(
        [
            {
                **v,
                "total_qty": round(v["total_qty"], 3),
                "total_cost": round(v["total_cost"], 0),
            }
            for v in aggregated_resources.values()
        ],
        key=lambda x: x["resource_id"],
    )

    tt_cost = total_vl + total_nc + total_m
    approx_gxd_ty = (tt_cost * 1.16) / 1e9
    lookup_scale_cpc_ty = float(project_info.get("tmdt_gxdtt_approved_ty") or approx_gxd_ty)
    if is_bcktkt:
        cpc_lookup = {
            "rate": float(cpc_rates_for_type[0]),
            "matched_index": 0,
            "matched_threshold_ty": bang_3_3["thresholds_ty_dong"][0],
            "matched_label": "≤ 40 (Dự án lập Báo cáo KT-KT theo khoản 2 Mục II.1 PL III TT 36/2026)",
            "method": "Cột [3] (≤ 40 tỷ đồng) cho công trình lập Báo cáo KT-KT",
        }
    else:
        cpc_lookup = step_lookup_le(
            lookup_scale_cpc_ty,
            bang_3_3["thresholds_ty_dong"],
            cpc_rates_for_type,
            bang_3_3["labels"],
        )

    rate_cpc = cpc_lookup["rate"]

    # Bổ sung chiết tính đơn giá đầy đủ (Sheet 'Đơn giá chi tiết' & 'Dự thầu' trong G8)
    for row in detailed_boq:
        u_t = row["unit_direct"]
        u_c = round(u_t * (rate_cpc / 100.0), 0)
        u_tt = round(u_t * (rate_tt_other / 100.0), 0)
        u_tl = round((u_t + u_c) * (rate_tl / 100.0), 0)
        u_full_before_vat = u_t + u_c + u_tt + u_tl
        u_vat = round(u_full_before_vat * vat_rate, 0)
        u_full_after_vat = u_full_before_vat + u_vat
        row["unit_cpc"] = u_c
        row["unit_tt_other"] = u_tt
        row["unit_tl"] = u_tl
        row["unit_bid_before_tax"] = u_full_before_vat
        row["unit_bid_after_tax"] = u_full_after_vat
        row["total_bid_before_tax"] = round(u_full_before_vat * row["quantity"], 0)
        row["total_bid_after_tax"] = round(u_full_after_vat * row["quantity"], 0)

    c_cost = round(tt_cost * (rate_cpc / 100.0), 0)
    tl_cost = round((tt_cost + c_cost) * (rate_tl / 100.0), 0)
    tt_other_cost = round(tt_cost * (rate_tt_other / 100.0), 0)
    g_xdtt = tt_cost + c_cost + tl_cost + tt_other_cost
    gtgt_xd = round(g_xdtt * vat_rate, 0)
    g_xd_sau_thue_chua_lt = g_xdtt + gtgt_xd

    bang_3_7 = tt36["bang_3_7_nha_tam"]
    is_linear_project = bool(project_info.get("is_linear_project", False))
    nha_tam_key = "cong_trinh_theo_tuyen" if is_linear_project else "cong_trinh_con_lai"
    nha_tam_lookup = step_lookup_le(
        lookup_scale_cpc_ty,
        bang_3_7["thresholds_ty_dong"],
        bang_3_7["rates"][nha_tam_key],
        bang_3_7["labels"],
    )
    rate_lt = nha_tam_lookup["rate"]
    lt_truoc_thue = round(g_xdtt * (rate_lt / 100.0), 0)
    lt_gtgt = round(lt_truoc_thue * vat_rate, 0)
    lt_sau_thue = lt_truoc_thue + lt_gtgt

    g_xd_total_truoc_thue = g_xdtt + lt_truoc_thue
    g_xd_total_gtgt = gtgt_xd + lt_gtgt
    g_xd_total_sau_thue = g_xd_sau_thue_chua_lt + lt_sau_thue

    bang_3_8_summary = {
        "VL": total_vl,
        "NC": total_nc,
        "M": total_m,
        "T": tt_cost,
        "rate_cpc": rate_cpc,
        "cpc_lookup": cpc_lookup,
        "C": c_cost,
        "rate_tl": rate_tl,
        "TL": tl_cost,
        "rate_tt_other": rate_tt_other,
        "TT": tt_other_cost,
        "G_XDTT": g_xdtt,
        "vat_rate_pct": vat_rate * 100.0,
        "GTGT_XD": gtgt_xd,
        "G_XD_sau_thue_chua_LT": g_xd_sau_thue_chua_lt,
        "rate_lt": rate_lt,
        "nha_tam_lookup": nha_tam_lookup,
        "LT_truoc_thue": lt_truoc_thue,
        "LT_GTGT": lt_gtgt,
        "LT_sau_thue": lt_sau_thue,
        "G_XD_truoc_thue": g_xd_total_truoc_thue,
        "G_XD_GTGT": g_xd_total_gtgt,
        "G_XD_sau_thue": g_xd_total_sau_thue,
    }

    # Thiết bị (G_TB)
    detailed_equipment: List[Dict[str, Any]] = []
    g_tb_mua_sam = 0.0
    for idx, eq in enumerate(equipment_items, start=1):
        eq_qty = float(eq.get("quantity", 0.0))
        eq_price = float(eq.get("unit_price", 0.0))
        eq_total = round(eq_qty * eq_price, 0)
        g_tb_mua_sam += eq_total
        detailed_equipment.append({
            "stt": idx,
            "id": eq.get("id", idx),
            "name": eq["name"],
            "unit": eq.get("unit", "hệ thống"),
            "quantity": eq_qty,
            "unit_price": eq_price,
            "total_before_tax": eq_total,
            "vat": round(eq_total * vat_rate, 0),
            "total_after_tax": round(eq_total * (1.0 + vat_rate), 0),
        })

    g_tb_truoc_thue = g_tb_mua_sam
    g_tb_gtgt = round(g_tb_truoc_thue * vat_rate, 0)
    g_tb_sau_thue = g_tb_truoc_thue + g_tb_gtgt

    # Căn cứ tính QLDA và Tư vấn ĐTXD:
    # Nếu include_lt_in_qlda_tv == False (theo Công văn 12637/BXD-KTQLXD ngày 11/08/2026 trên G8):
    # dùng g_xdtt (không gồm chi phí nhà tạm LT). Nếu True: dùng g_xd_total_truoc_thue (gồm LT).
    g_xd_basis_for_qlda_tv = g_xd_total_truoc_thue if include_lt_in_qlda_tv else g_xdtt
    g_xd_ty = g_xd_basis_for_qlda_tv / 1e9
    g_tb_ty = g_tb_truoc_thue / 1e9
    g_xd_tb_truoc_thue = g_xd_basis_for_qlda_tv + g_tb_truoc_thue
    g_xd_tb_ty = g_xd_tb_truoc_thue / 1e9

    tt38_pl8 = regulations["tt38_phu_luc_8"]
    k_region_qlda = 1.25 if is_mountain_island else 1.0

    b11 = tt38_pl8["bang_1_1_qlda"]
    qlda_interp = interpolate_rate_tt38(
        g_xd_tb_ty,
        b11["thresholds_ty_dong"],
        b11["rates"].get(building_type, b11["rates"]["dan_dung"]),
    )
    rate_qlda = round(qlda_interp["rate"] * k_region_qlda, 4)
    g_qlda_truoc_thue = round(g_xd_tb_truoc_thue * (rate_qlda / 100.0), 0)
    g_qlda_gtgt = round(g_qlda_truoc_thue * vat_rate, 0)
    g_qlda_sau_thue = g_qlda_truoc_thue + g_qlda_gtgt

    consulting_items: List[Dict[str, Any]] = []
    if is_bcktkt:
        b24 = tt38_pl8["bang_2_4_bc_ktkt"]
        bcktkt_interp = interpolate_rate_tt38(
            g_xd_tb_ty,
            b24["thresholds_ty_dong"],
            b24["rates"].get(building_type, b24["rates"]["dan_dung"]),
        )
        val_bcktkt = round(g_xd_tb_truoc_thue * (bcktkt_interp["rate"] / 100.0), 0)
        consulting_items.append({
            "code": "TV.01",
            "name": "Chi phí lập Báo cáo kinh tế - kỹ thuật (Bảng 2.4 PL VIII TT 38/2026)",
            "basis_text": "(G_XD + G_TB) trước thuế",
            "basis_value": g_xd_tb_truoc_thue,
            "rate_pct": bcktkt_interp["rate"],
            "interpolation": bcktkt_interp,
            "before_tax": val_bcktkt,
            "vat": round(val_bcktkt * vat_rate, 0),
            "after_tax": val_bcktkt + round(val_bcktkt * vat_rate, 0),
        })
    else:
        b23 = tt38_pl8["bang_2_3_bc_nckt"]
        bcnckt_interp = interpolate_rate_tt38(
            g_xd_tb_ty,
            b23["thresholds_ty_dong"],
            b23["rates"].get(building_type, b23["rates"]["dan_dung"]),
        )
        val_bcnckt = round(g_xd_tb_truoc_thue * (bcnckt_interp["rate"] / 100.0), 0)
        consulting_items.append({
            "code": "TV.01",
            "name": "Chi phí lập Báo cáo nghiên cứu khả thi ĐTXD (Bảng 2.3 PL VIII TT 38/2026)",
            "basis_text": "(G_XD + G_TB) trước thuế",
            "basis_value": g_xd_tb_truoc_thue,
            "rate_pct": bcnckt_interp["rate"],
            "interpolation": bcnckt_interp,
            "before_tax": val_bcnckt,
            "vat": round(val_bcnckt * vat_rate, 0),
            "after_tax": val_bcnckt + round(val_bcnckt * vat_rate, 0),
        })

        if building_type in ("cong_nghiep", "cong_nghiep_ham"):
            tk_table_key = "bang_2_9_tkkt_cong_nghiep" if design_step == "tkkt_3_buoc" else "bang_2_10_tkbvtc_cong_nghiep"
        else:
            tk_table_key = "bang_2_7_tkkt_dan_dung" if design_step == "tkkt_3_buoc" else "bang_2_8_tkbvtc_dan_dung"

        tk_table = tt38_pl8[tk_table_key]
        tk_rates = tk_table["rates_by_grade"].get(building_grade, tk_table["rates_by_grade"]["cap_3"])
        tk_interp = interpolate_rate_tt38(g_xd_ty, tk_table["thresholds_ty_dong"], tk_rates)
        val_tk = round(g_xd_basis_for_qlda_tv * (tk_interp["rate"] / 100.0), 0)
        consulting_items.append({
            "code": "TV.02",
            "name": f"Chi phí thiết kế xây dựng ({tk_table['title']})",
            "basis_text": "G_XD trước thuế",
            "basis_value": g_xd_basis_for_qlda_tv,
            "rate_pct": tk_interp["rate"],
            "interpolation": tk_interp,
            "before_tax": val_tk,
            "vat": round(val_tk * vat_rate, 0),
            "after_tax": val_tk + round(val_tk * vat_rate, 0),
        })

    for code, tbl_key, title in [
        ("TV.03", "bang_2_19_tham_tra_thiet_ke", "Chi phí thẩm tra thiết kế xây dựng (Bảng 2.19 PL VIII TT 38/2026)"),
        ("TV.04", "bang_2_20_tham_tra_du_toan", "Chi phí thẩm tra dự toán xây dựng (Bảng 2.20 PL VIII TT 38/2026)"),
        ("TV.05", "bang_2_22_hsmt_xay_dung", "Chi phí lập HSMT, đánh giá HSDT thi công xây dựng (Bảng 2.22 PL VIII TT 38/2026)"),
    ]:
        tbl = tt38_pl8[tbl_key]
        interp = interpolate_rate_tt38(
            g_xd_ty,
            tbl["thresholds_ty_dong"],
            tbl["rates"].get(building_type, tbl["rates"]["dan_dung"]),
        )
        val = round(g_xd_basis_for_qlda_tv * (interp["rate"] / 100.0), 0)
        consulting_items.append({
            "code": code,
            "name": title,
            "basis_text": "G_XD trước thuế",
            "basis_value": g_xd_basis_for_qlda_tv,
            "rate_pct": interp["rate"],
            "interpolation": interp,
            "before_tax": val,
            "vat": round(val * vat_rate, 0),
            "after_tax": val + round(val * vat_rate, 0),
        })

    if g_tb_truoc_thue > 0:
        b223 = tt38_pl8["bang_2_23_hsmt_thiet_bi"]
        hsmt_tb_interp = interpolate_rate_tt38(
            g_tb_ty,
            b223["thresholds_ty_dong"],
            b223["rates"].get(building_type, b223["rates"]["dan_dung"]),
        )
        val_hsmt_tb = round(g_tb_truoc_thue * (hsmt_tb_interp["rate"] / 100.0), 0)
        consulting_items.append({
            "code": "TV.06",
            "name": "Chi phí lập HSMT, đánh giá HSDT mua sắm thiết bị (Bảng 2.23 PL VIII TT 38/2026)",
            "basis_text": "G_TB trước thuế",
            "basis_value": g_tb_truoc_thue,
            "rate_pct": hsmt_tb_interp["rate"],
            "interpolation": hsmt_tb_interp,
            "before_tax": val_hsmt_tb,
            "vat": round(val_hsmt_tb * vat_rate, 0),
            "after_tax": val_hsmt_tb + round(val_hsmt_tb * vat_rate, 0),
        })

    b224 = tt38_pl8["bang_2_24_giam_sat_tcxd"]
    gs_xd_interp = interpolate_rate_tt38(
        g_xd_ty,
        b224["thresholds_ty_dong"],
        b224["rates"].get(building_type, b224["rates"]["dan_dung"]),
    )
    val_gs_xd = round(g_xd_basis_for_qlda_tv * (gs_xd_interp["rate"] / 100.0), 0)
    consulting_items.append({
        "code": "TV.07",
        "name": "Chi phí giám sát thi công xây dựng (Bảng 2.24 PL VIII TT 38/2026)",
        "basis_text": "G_XD trước thuế",
        "basis_value": g_xd_basis_for_qlda_tv,
        "rate_pct": gs_xd_interp["rate"],
        "interpolation": gs_xd_interp,
        "before_tax": val_gs_xd,
        "vat": round(val_gs_xd * vat_rate, 0),
        "after_tax": val_gs_xd + round(val_gs_xd * vat_rate, 0),
    })

    if g_tb_truoc_thue > 0:
        b225 = tt38_pl8["bang_2_25_giam_sat_ldtb"]
        gs_tb_interp = interpolate_rate_tt38(
            g_tb_ty,
            b225["thresholds_ty_dong"],
            b225["rates"].get(building_type, b225["rates"]["dan_dung"]),
        )
        val_gs_tb = round(g_tb_truoc_thue * (gs_tb_interp["rate"] / 100.0), 0)
        consulting_items.append({
            "code": "TV.08",
            "name": "Chi phí giám sát lắp đặt thiết bị (Bảng 2.25 PL VIII TT 38/2026)",
            "basis_text": "G_TB trước thuế",
            "basis_value": g_tb_truoc_thue,
            "rate_pct": gs_tb_interp["rate"],
            "interpolation": gs_tb_interp,
            "before_tax": val_gs_tb,
            "vat": round(val_gs_tb * vat_rate, 0),
            "after_tax": val_gs_tb + round(val_gs_tb * vat_rate, 0),
        })

    g_tv_truoc_thue = sum(item["before_tax"] for item in consulting_items)
    g_tv_gtgt = sum(item["vat"] for item in consulting_items)
    g_tv_sau_thue = sum(item["after_tax"] for item in consulting_items)

    other_cost_items = [
        {
            "code": "CK.01",
            "name": "Chi phí thẩm định Báo cáo KT-KT / Thiết kế triển khai sau TKCS (Thông tư Bộ Tài chính)",
            "basis_text": "Tạm tính theo biểu phí (0,12% G_XD)",
            "rate_pct": 0.12,
            "before_tax": round(g_xd_total_truoc_thue * 0.0012, 0),
            "vat": 0,
            "after_tax": round(g_xd_total_truoc_thue * 0.0012, 0),
        },
        {
            "code": "CK.02",
            "name": "Chi phí bảo hiểm công trình trong thời gian xây dựng",
            "basis_text": "0,15% (G_XD + G_TB) trước thuế",
            "rate_pct": 0.15,
            "before_tax": round((g_xd_total_truoc_thue + g_tb_truoc_thue) * 0.0015, 0),
            "vat": round(round((g_xd_total_truoc_thue + g_tb_truoc_thue) * 0.0015, 0) * vat_rate, 0),
            "after_tax": round((g_xd_total_truoc_thue + g_tb_truoc_thue) * 0.0015, 0)
            + round(round((g_xd_total_truoc_thue + g_tb_truoc_thue) * 0.0015, 0) * vat_rate, 0),
        },
        {
            "code": "CK.03",
            "name": "Chi phí kiểm toán độc lập & thẩm tra phê duyệt quyết toán vốn đầu tư",
            "basis_text": "0,45% (G_XD + G_TB) trước thuế",
            "rate_pct": 0.45,
            "before_tax": round((g_xd_total_truoc_thue + g_tb_truoc_thue) * 0.0045, 0),
            "vat": round(round((g_xd_total_truoc_thue + g_tb_truoc_thue) * 0.0045, 0) * vat_rate, 0),
            "after_tax": round((g_xd_total_truoc_thue + g_tb_truoc_thue) * 0.0045, 0)
            + round(round((g_xd_total_truoc_thue + g_tb_truoc_thue) * 0.0045, 0) * vat_rate, 0),
        },
    ]

    g_k_truoc_thue = sum(item["before_tax"] for item in other_cost_items)
    g_k_gtgt = sum(item["vat"] for item in other_cost_items)
    g_k_sau_thue = sum(item["after_tax"] for item in other_cost_items)

    sub_truoc_dp_before_tax = g_xd_total_truoc_thue + g_tb_truoc_thue + g_qlda_truoc_thue + g_tv_truoc_thue + g_k_truoc_thue
    sub_truoc_dp_vat = g_xd_total_gtgt + g_tb_gtgt + g_qlda_gtgt + g_tv_gtgt + g_k_gtgt
    sub_truoc_dp_after_tax = g_xd_total_sau_thue + g_tb_sau_thue + g_qlda_sau_thue + g_tv_sau_thue + g_k_sau_thue

    dp1_rate = float(project_info.get("contingency_volume_rate", 5.0)) / 100.0
    dp2_rate = float(project_info.get("contingency_escalation_rate", 2.5)) / 100.0

    g_dp1_before_tax = round(sub_truoc_dp_before_tax * dp1_rate, 0)
    g_dp1_vat = round(sub_truoc_dp_vat * dp1_rate, 0)
    g_dp1_after_tax = g_dp1_before_tax + g_dp1_vat

    g_dp2_before_tax = round(sub_truoc_dp_before_tax * dp2_rate, 0)
    g_dp2_vat = round(sub_truoc_dp_vat * dp2_rate, 0)
    g_dp2_after_tax = g_dp2_before_tax + g_dp2_vat

    g_dp_before_tax = g_dp1_before_tax + g_dp2_before_tax
    g_dp_vat = g_dp1_vat + g_dp2_vat
    g_dp_after_tax = g_dp1_after_tax + g_dp2_after_tax

    total_dtxd_before_tax = sub_truoc_dp_before_tax + g_dp_before_tax
    total_dtxd_vat = sub_truoc_dp_vat + g_dp_vat
    total_dtxd_after_tax = sub_truoc_dp_after_tax + g_dp_after_tax

    return {
        "project_info": project_info,
        "detailed_boq": detailed_boq,
        "material_analysis_rows": material_analysis_rows,
        "summary_resources": summary_resources,
        "bang_3_8_summary": bang_3_8_summary,
        "detailed_equipment": detailed_equipment,
        "qlda_summary": {
            "rate_pct": rate_qlda,
            "interpolation": qlda_interp,
            "before_tax": g_qlda_truoc_thue,
            "vat": g_qlda_gtgt,
            "after_tax": g_qlda_sau_thue,
            "include_lt_in_qlda_tv": include_lt_in_qlda_tv,
        },
        "consulting_items": consulting_items,
        "other_cost_items": other_cost_items,
        "total_summary": {
            "G_XD": {"before_tax": g_xd_total_truoc_thue, "vat": g_xd_total_gtgt, "after_tax": g_xd_total_sau_thue},
            "G_TB": {"before_tax": g_tb_truoc_thue, "vat": g_tb_gtgt, "after_tax": g_tb_sau_thue},
            "G_QLDA": {"before_tax": g_qlda_truoc_thue, "vat": g_qlda_gtgt, "after_tax": g_qlda_sau_thue},
            "G_TV": {"before_tax": g_tv_truoc_thue, "vat": g_tv_gtgt, "after_tax": g_tv_sau_thue},
            "G_K": {"before_tax": g_k_truoc_thue, "vat": g_k_gtgt, "after_tax": g_k_sau_thue},
            "SUB_BEFORE_DP": {"before_tax": sub_truoc_dp_before_tax, "vat": sub_truoc_dp_vat, "after_tax": sub_truoc_dp_after_tax},
            "G_DP1": {"rate_pct": dp1_rate * 100.0, "before_tax": g_dp1_before_tax, "vat": g_dp1_vat, "after_tax": g_dp1_after_tax},
            "G_DP2": {"rate_pct": dp2_rate * 100.0, "before_tax": g_dp2_before_tax, "vat": g_dp2_vat, "after_tax": g_dp2_after_tax},
            "G_DP": {"before_tax": g_dp_before_tax, "vat": g_dp_vat, "after_tax": g_dp_after_tax},
            "TOTAL_DTXD": {"before_tax": total_dtxd_before_tax, "vat": total_dtxd_vat, "after_tax": total_dtxd_after_tax},
        },
    }


if __name__ == "__main__":
    data = load_all_data()
    for preset_key, preset in data["presets"]["presets"].items():
        res = calculate_project_estimate(
            preset["project_info"],
            preset["boq_items"],
            preset["equipment_items"],
            data["prices"],
            data["norms"],
            data["regulations"],
        )
        b38 = res["bang_3_8_summary"]
        tot = res["total_summary"]
        print(f"=== G8 2026 PRESET: {preset_key} ({preset['project_info']['project_name']}) ===")
        print(f"  Chi phí trực tiếp (T = VL + NC + M): {b38['T']:,.0f} đ")
        print(f"  Chi phí xây dựng sau thuế (G_XD):    {tot['G_XD']['after_tax']:,.0f} đ")
        print(f"  TỔNG DỰ TOÁN CÔNG TRÌNH (SAU THUẾ):  {tot['TOTAL_DTXD']['after_tax']:,.0f} đ\n")
