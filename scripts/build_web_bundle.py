#!/usr/bin/env python3
"""
Script đóng gói dữ liệu JSON vào app.js và tạo đồng thời file HTML tự chứa (Artifact)
cho Hệ thống Tính Dự toán Xây dựng Công trình Nguồn vốn Nhà nước 2026.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
ARTIFACT_HTML = Path("/home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p/bafbf20d-b972-4df0-aaa8-ba48a718e711/phan_mem_du_toan_2026.html")

regulations = json.loads((DATA_DIR / "regulations_2026.json").read_text(encoding="utf-8"))
prices = json.loads((DATA_DIR / "bang_gia_co_so.json").read_text(encoding="utf-8"))
norms = json.loads((DATA_DIR / "dinh_muc_tt38_2026.json").read_text(encoding="utf-8"))
presets = json.loads((DATA_DIR / "du_an_mau_dan_dung.json").read_text(encoding="utf-8"))

JS_LOGIC = r"""
// ============================================================================
// BỘ MÁY TÍNH DỰ TOÁN XÂY DỰNG CÔNG TRÌNH NGUỒN VỐN NHÀ NƯỚC 2026 (FRONTEND)
// ============================================================================

let state = {
  project_info: {},
  boq_items: [],
  equipment_items: [],
  prices: JSON.parse(JSON.stringify(EMBEDDED_PRICES)),
  norms: JSON.parse(JSON.stringify(EMBEDDED_NORMS)),
  regulations: EMBEDDED_REGULATIONS,
  computed: null
};

function fmtNum(val, decimals = 0) {
  if (val === null || val === undefined || isNaN(val)) return "0";
  return Number(val).toLocaleString("vi-VN", {
    minimumFractionDigits: decimals,
    maximumFractionDigits: decimals
  });
}

function fmtVND(val) {
  return fmtNum(Math.round(val || 0), 0) + " đ";
}

function stepLookupLe(valTy, thresholds, rates, labels) {
  for (let i = 0; i < thresholds.length; i++) {
    if (valTy <= thresholds[i]) {
      return {
        rate: Number(rates[i]),
        matched_index: i,
        matched_label: labels && labels[i] ? labels[i] : ("≤ " + thresholds[i])
      };
    }
  }
  const last = rates.length - 1;
  return {
    rate: Number(rates[last]),
    matched_index: last,
    matched_label: labels && labels[last] ? labels[last] : ("> " + thresholds[last - 1])
  };
}

function interpolateRateTT38(gtTy, thresholds, rates) {
  if (gtTy <= thresholds[0]) {
    return {
      rate: Number(rates[0].toFixed(4)),
      gt: gtTy,
      gb: thresholds[0],
      ga: thresholds[0],
      nb: rates[0],
      na: rates[0],
      formula: `G_t = ${gtTy.toFixed(3)} tỷ ≤ ${thresholds[0]} tỷ ⇒ N_t = ${rates[0].toFixed(3)}%`
    };
  }
  for (let i = 0; i < thresholds.length - 1; i++) {
    const gb = thresholds[i];
    const ga = thresholds[i + 1];
    const nb = rates[i];
    const na = rates[i + 1];
    if (gtTy >= gb && gtTy <= ga) {
      const nt = ga === gb ? nb : nb - ((nb - na) / (ga - gb)) * (gtTy - gb);
      return {
        rate: Number(nt.toFixed(4)),
        gt: gtTy,
        gb,
        ga,
        nb,
        na,
        formula: `N_t = ${nb} - [(${nb} - ${na}) / (${ga} - ${gb})] × (${gtTy.toFixed(3)} - ${gb}) = ${nt.toFixed(4)}%`
      };
    }
  }
  const last = thresholds.length - 1;
  return {
    rate: Number(rates[last].toFixed(4)),
    gt: gtTy,
    gb: thresholds[last],
    ga: thresholds[last],
    nb: rates[last],
    na: rates[last],
    formula: `G_t = ${gtTy.toFixed(3)} tỷ ≥ ${thresholds[last]} tỷ ⇒ N_t = ${rates[last].toFixed(3)}%`
  };
}

function calculateAll() {
  const pi = state.project_info;
  const k_nc = Number(pi.k_nc || 1.0);
  const k_m = Number(pi.k_m || 1.0);
  const vat_rate = Number(pi.vat_rate || 8.0) / 100.0;
  const building_type = pi.building_type || "dan_dung";
  const building_grade = pi.building_grade || "cap_3";
  const design_step = pi.design_step || "tkbvtc_2_buoc";
  const is_bcktkt = Boolean(pi.is_bcktkt);
  const is_mountain_island = Boolean(pi.is_mountain_island);
  const is_linear_project = Boolean(pi.is_linear_project);

  const resMap = {};
  state.prices.vat_lieu.forEach(r => resMap[r.id] = { ...r, type: "VL" });
  state.prices.nhan_cong.forEach(r => resMap[r.id] = { ...r, type: "NC" });
  state.prices.may_thi_cong.forEach(r => resMap[r.id] = { ...r, type: "M" });

  const normMap = {};
  state.norms.forEach(n => normMap[n.code] = n);

  const detailed_boq = [];
  const aggResources = {};
  let total_vl = 0;
  let total_nc = 0;
  let total_m = 0;

  state.boq_items.forEach((item, index) => {
    const stt = index + 1;
    const norm = normMap[item.norm_code] || state.norms[0];
    const qty = Number(item.quantity || 0);

    let unit_vl = 0;
    let unit_nc = 0;
    let unit_m = 0;
    const components = [];

    const groups = [
      ["VL", norm.vl || []],
      ["NC", norm.nc || []],
      ["M", norm.m || []]
    ];

    groups.forEach(([cType, cList]) => {
      cList.forEach(comp => {
        const rInfo = resMap[comp.id] || { id: comp.id, name: comp.id, unit: "", price: 0, source: "" };
        const factorK = cType === "NC" ? k_nc : (cType === "M" ? k_m : 1.0);
        const effPrice = Number(rInfo.price || 0) * factorK;
        const normQty = Number(comp.qty || 0);
        const uCost = normQty * effPrice;
        const totQty = normQty * qty;
        const totCost = totQty * effPrice;

        if (cType === "VL") unit_vl += uCost;
        if (cType === "NC") unit_nc += uCost;
        if (cType === "M") unit_m += uCost;

        components.push({
          type: cType,
          id: comp.id,
          name: rInfo.name,
          unit: rInfo.unit,
          norm_qty: normQty,
          total_qty: totQty,
          unit_price: effPrice,
          unit_cost: uCost,
          total_cost: Math.round(totCost)
        });

        if (!aggResources[comp.id]) {
          aggResources[comp.id] = {
            id: comp.id,
            type: cType,
            name: rInfo.name,
            unit: rInfo.unit,
            base_price: rInfo.price,
            factor_k: factorK,
            total_qty: 0,
            total_cost: 0,
            source: rInfo.source
          };
        }
        aggResources[comp.id].total_qty += totQty;
        aggResources[comp.id].total_cost += totCost;
      });
    });

    const line_vl = Math.round(unit_vl * qty);
    const line_nc = Math.round(unit_nc * qty);
    const line_m = Math.round(unit_m * qty);
    const line_direct = line_vl + line_nc + line_m;

    total_vl += line_vl;
    total_nc += line_nc;
    total_m += line_m;

    detailed_boq.push({
      ...item,
      stt,
      unit: norm.unit,
      name: item.custom_name || norm.name,
      unit_vl: Math.round(unit_vl),
      unit_nc: Math.round(unit_nc),
      unit_m: Math.round(unit_m),
      unit_direct: Math.round(unit_vl + unit_nc + unit_m),
      total_vl: line_vl,
      total_nc: line_nc,
      total_m: line_m,
      total_direct: line_direct,
      components
    });
  });

  // Bảng 3.8 Phụ lục III TT 36/2026/TT-BXD (Đính chính bởi QĐ 1538/QĐ-BXD)
  const T = total_vl + total_nc + total_m;
  const tt36 = state.regulations.tt36_phu_luc_3;
  const b33 = tt36.bang_3_3_cpc_du_toan;
  const cpcArr = b33.rates[building_type] || b33.rates.dan_dung;
  const lookupScaleTy = Number(pi.tmdt_gxdtt_approved_ty || ((T * 1.16) / 1e9));

  let cpcLookup;
  if (is_bcktkt) {
    cpcLookup = {
      rate: Number(cpcArr[0]),
      matched_label: "≤ 40 tỷ (Dự án lập Báo cáo KT-KT theo khoản 2 Mục II.1 PL III TT 36/2026)"
    };
  } else {
    cpcLookup = stepLookupLe(lookupScaleTy, b33.thresholds_ty_dong, cpcArr, b33.labels);
  }

  const rate_cpc = cpcLookup.rate;
  const C = Math.round(T * (rate_cpc / 100.0));

  const rate_tl = Number(tt36.bang_3_6_thu_nhap_chiu_thue.rates[building_type] || 5.5);
  const TL = Math.round((T + C) * (rate_tl / 100.0));

  const rate_tt = Number(tt36.bang_3_5_chi_phi_tt.rates[building_type] || 2.5);
  const TT = Math.round(T * (rate_tt / 100.0));

  const G_XDTT = T + C + TL + TT;
  const GTGT_XD = Math.round(G_XDTT * vat_rate);
  const G_XD_SAU_THUE_CHUA_LT = G_XDTT + GTGT_XD;

  const b37 = tt36.bang_3_7_nha_tam;
  const ltArr = is_linear_project ? b37.rates.cong_trinh_theo_tuyen : b37.rates.cong_trinh_con_lai;
  const ltLookup = stepLookupLe(lookupScaleTy, b37.thresholds_ty_dong, ltArr, b37.labels);
  const rate_lt = ltLookup.rate;

  const LT_TRUOC_THUE = Math.round(G_XDTT * (rate_lt / 100.0));
  const LT_GTGT = Math.round(LT_TRUOC_THUE * vat_rate);
  const LT_SAU_THUE = LT_TRUOC_THUE + LT_GTGT;

  const G_XD_TOTAL_BEFORE = G_XDTT + LT_TRUOC_THUE;
  const G_XD_TOTAL_VAT = GTGT_XD + LT_GTGT;
  const G_XD_TOTAL_AFTER = G_XD_SAU_THUE_CHUA_LT + LT_SAU_THUE;

  // Thiết bị (G_TB)
  let G_TB_BEFORE = 0;
  const detailed_eq = state.equipment_items.map((eq, idx) => {
    const q = Number(eq.quantity || 0);
    const p = Number(eq.unit_price || 0);
    const b = Math.round(q * p);
    const v = Math.round(b * vat_rate);
    G_TB_BEFORE += b;
    return {
      ...eq,
      stt: idx + 1,
      before_tax: b,
      vat: v,
      after_tax: b + v
    };
  });
  const G_TB_VAT = Math.round(G_TB_BEFORE * vat_rate);
  const G_TB_AFTER = G_TB_BEFORE + G_TB_VAT;

  // Phụ lục VIII Thông tư 38/2026/TT-BXD
  const pl8 = state.regulations.tt38_phu_luc_8;
  const g_xd_ty = G_XD_TOTAL_BEFORE / 1e9;
  const g_tb_ty = G_TB_BEFORE / 1e9;
  const g_xd_tb_before = G_XD_TOTAL_BEFORE + G_TB_BEFORE;
  const g_xd_tb_ty = g_xd_tb_before / 1e9;
  const baseTypeKey = building_type.startsWith("cong_nghiep") ? "cong_nghiep" :
                      (building_type.startsWith("dan_dung") ? "dan_dung" : building_type);

  // QLDA (Bảng 1.1)
  const b11 = pl8.bang_1_1_qlda;
  const qldaInterp = interpolateRateTT38(g_xd_tb_ty, b11.thresholds_ty_dong, b11.rates[baseTypeKey] || b11.rates.dan_dung);
  const k_qlda = is_mountain_island ? 1.25 : 1.0;
  const rate_qlda = Number((qldaInterp.rate * k_qlda).toFixed(4));
  const G_QLDA_BEFORE = Math.round(g_xd_tb_before * (rate_qlda / 100.0));
  const G_QLDA_VAT = Math.round(G_QLDA_BEFORE * vat_rate);
  const G_QLDA_AFTER = G_QLDA_BEFORE + G_QLDA_VAT;

  // Tư vấn ĐTXD (G_TV)
  const consulting = [];
  if (is_bcktkt) {
    const b24 = pl8.bang_2_4_bc_ktkt;
    const interp = interpolateRateTT38(g_xd_tb_ty, b24.thresholds_ty_dong, b24.rates[baseTypeKey] || b24.rates.dan_dung);
    const bf = Math.round(g_xd_tb_before * (interp.rate / 100.0));
    const vt = Math.round(bf * vat_rate);
    consulting.push({
      code: "TV.01",
      name: "Chi phí lập Báo cáo kinh tế - kỹ thuật (Bảng 2.4 PL VIII TT 38/2026)",
      basis: "(G_XD + G_TB) trước thuế",
      rate_pct: interp.rate,
      formula: interp.formula,
      before_tax: bf,
      vat: vt,
      after_tax: bf + vt
    });
  } else {
    const b23 = pl8.bang_2_3_bc_nckt;
    const interp1 = interpolateRateTT38(g_xd_tb_ty, b23.thresholds_ty_dong, b23.rates[baseTypeKey] || b23.rates.dan_dung);
    const bf1 = Math.round(g_xd_tb_before * (interp1.rate / 100.0));
    const vt1 = Math.round(bf1 * vat_rate);
    consulting.push({
      code: "TV.01",
      name: "Chi phí lập Báo cáo nghiên cứu khả thi ĐTXD (Bảng 2.3 PL VIII TT 38/2026)",
      basis: "(G_XD + G_TB) trước thuế",
      rate_pct: interp1.rate,
      formula: interp1.formula,
      before_tax: bf1,
      vat: vt1,
      after_tax: bf1 + vt1
    });

    const tkKey = baseTypeKey === "cong_nghiep"
      ? (design_step === "tkkt_3_buoc" ? "bang_2_9_tkkt_cong_nghiep" : "bang_2_10_tkbvtc_cong_nghiep")
      : (design_step === "tkkt_3_buoc" ? "bang_2_7_tkkt_dan_dung" : "bang_2_8_tkbvtc_dan_dung");
    const tkTbl = pl8[tkKey];
    const interp2 = interpolateRateTT38(g_xd_ty, tkTbl.thresholds_ty_dong, tkTbl.rates_by_grade[building_grade] || tkTbl.rates_by_grade.cap_3);
    const bf2 = Math.round(G_XD_TOTAL_BEFORE * (interp2.rate / 100.0));
    const vt2 = Math.round(bf2 * vat_rate);
    consulting.push({
      code: "TV.02",
      name: `Chi phí thiết kế xây dựng (${tkTbl.title})`,
      basis: "G_XD trước thuế",
      rate_pct: interp2.rate,
      formula: interp2.formula,
      before_tax: bf2,
      vat: vt2,
      after_tax: bf2 + vt2
    });
  }

  // Thẩm tra TK (Bảng 2.19)
  const b219 = pl8.bang_2_19_tham_tra_thiet_ke;
  const i219 = interpolateRateTT38(g_xd_ty, b219.thresholds_ty_dong, b219.rates[baseTypeKey] || b219.rates.dan_dung);
  const bf219 = Math.round(G_XD_TOTAL_BEFORE * (i219.rate / 100.0));
  const vt219 = Math.round(bf219 * vat_rate);
  consulting.push({
    code: "TV.03",
    name: "Chi phí thẩm tra thiết kế xây dựng (Bảng 2.19 PL VIII TT 38/2026)",
    basis: "G_XD trước thuế",
    rate_pct: i219.rate,
    formula: i219.formula,
    before_tax: bf219,
    vat: vt219,
    after_tax: bf219 + vt219
  });

  // Thẩm tra Dự toán (Bảng 2.20)
  const b220 = pl8.bang_2_20_tham_tra_du_toan;
  const i220 = interpolateRateTT38(g_xd_ty, b220.thresholds_ty_dong, b220.rates[baseTypeKey] || b220.rates.dan_dung);
  const bf220 = Math.round(G_XD_TOTAL_BEFORE * (i220.rate / 100.0));
  const vt220 = Math.round(bf220 * vat_rate);
  consulting.push({
    code: "TV.04",
    name: "Chi phí thẩm tra dự toán xây dựng (Bảng 2.20 PL VIII TT 38/2026)",
    basis: "G_XD trước thuế",
    rate_pct: i220.rate,
    formula: i220.formula,
    before_tax: bf220,
    vat: vt220,
    after_tax: bf220 + vt220
  });

  // HSMT XD (Bảng 2.22)
  const b222 = pl8.bang_2_22_hsmt_xay_dung;
  const i222 = interpolateRateTT38(g_xd_ty, b222.thresholds_ty_dong, b222.rates[baseTypeKey] || b222.rates.dan_dung);
  const bf222 = Math.round(G_XD_TOTAL_BEFORE * (i222.rate / 100.0));
  const vt222 = Math.round(bf222 * vat_rate);
  consulting.push({
    code: "TV.05",
    name: "Chi phí lập HSMT, đánh giá HSDT thi công xây dựng (Bảng 2.22 PL VIII TT 38/2026)",
    basis: "G_XD trước thuế",
    rate_pct: i222.rate,
    formula: i222.formula,
    before_tax: bf222,
    vat: vt222,
    after_tax: bf222 + vt222
  });

  // HSMT TB (Bảng 2.23)
  if (G_TB_BEFORE > 0) {
    const b223 = pl8.bang_2_23_hsmt_thiet_bi;
    const i223 = interpolateRateTT38(g_tb_ty, b223.thresholds_ty_dong, b223.rates[baseTypeKey] || b223.rates.dan_dung);
    const bf223 = Math.round(G_TB_BEFORE * (i223.rate / 100.0));
    const vt223 = Math.round(bf223 * vat_rate);
    consulting.push({
      code: "TV.06",
      name: "Chi phí lập HSMT, đánh giá HSDT mua sắm thiết bị (Bảng 2.23 PL VIII TT 38/2026)",
      basis: "G_TB trước thuế",
      rate_pct: i223.rate,
      formula: i223.formula,
      before_tax: bf223,
      vat: vt223,
      after_tax: bf223 + vt223
    });
  }

  // Giám sát TCXD (Bảng 2.24)
  const b224 = pl8.bang_2_24_giam_sat_tcxd;
  const i224 = interpolateRateTT38(g_xd_ty, b224.thresholds_ty_dong, b224.rates[baseTypeKey] || b224.rates.dan_dung);
  const bf224 = Math.round(G_XD_TOTAL_BEFORE * (i224.rate / 100.0));
  const vt224 = Math.round(bf224 * vat_rate);
  consulting.push({
    code: "TV.07",
    name: "Chi phí giám sát thi công xây dựng (Bảng 2.24 PL VIII TT 38/2026)",
    basis: "G_XD trước thuế",
    rate_pct: i224.rate,
    formula: i224.formula,
    before_tax: bf224,
    vat: vt224,
    after_tax: bf224 + vt224
  });

  // Giám sát LĐTB (Bảng 2.25)
  if (G_TB_BEFORE > 0) {
    const b225 = pl8.bang_2_25_giam_sat_ldtb;
    const i225 = interpolateRateTT38(g_tb_ty, b225.thresholds_ty_dong, b225.rates[baseTypeKey] || b225.rates.dan_dung);
    const bf225 = Math.round(G_TB_BEFORE * (i225.rate / 100.0));
    const vt225 = Math.round(bf225 * vat_rate);
    consulting.push({
      code: "TV.08",
      name: "Chi phí giám sát lắp đặt thiết bị (Bảng 2.25 PL VIII TT 38/2026)",
      basis: "G_TB trước thuế",
      rate_pct: i225.rate,
      formula: i225.formula,
      before_tax: bf225,
      vat: vt225,
      after_tax: bf225 + vt225
    });
  }

  const G_TV_BEFORE = consulting.reduce((s, x) => s + x.before_tax, 0);
  const G_TV_VAT = consulting.reduce((s, x) => s + x.vat, 0);
  const G_TV_AFTER = consulting.reduce((s, x) => s + x.after_tax, 0);

  // Chi phí khác (G_K)
  const ck1_bf = Math.round(G_XD_TOTAL_BEFORE * 0.0012);
  const ck2_bf = Math.round(g_xd_tb_before * 0.0015);
  const ck2_vt = Math.round(ck2_bf * vat_rate);
  const ck3_bf = Math.round(g_xd_tb_before * 0.0045);
  const ck3_vt = Math.round(ck3_bf * vat_rate);

  const other_costs = [
    {
      code: "CK.01",
      name: "Phí thẩm định Báo cáo KT-KT / Thiết kế triển khai sau TKCS",
      basis: "0,12% × G_XD trước thuế (Lệ phí không chịu thuế GTGT)",
      rate_pct: 0.12,
      before_tax: ck1_bf,
      vat: 0,
      after_tax: ck1_bf
    },
    {
      code: "CK.02",
      name: "Chi phí bảo hiểm công trình trong thời gian xây dựng",
      basis: "0,15% × (G_XD + G_TB) trước thuế",
      rate_pct: 0.15,
      before_tax: ck2_bf,
      vat: ck2_vt,
      after_tax: ck2_bf + ck2_vt
    },
    {
      code: "CK.03",
      name: "Chi phí kiểm toán độc lập & thẩm tra phê duyệt quyết toán",
      basis: "0,45% × (G_XD + G_TB) trước thuế",
      rate_pct: 0.45,
      before_tax: ck3_bf,
      vat: ck3_vt,
      after_tax: ck3_bf + ck3_vt
    }
  ];

  const G_K_BEFORE = other_costs.reduce((s, x) => s + x.before_tax, 0);
  const G_K_VAT = other_costs.reduce((s, x) => s + x.vat, 0);
  const G_K_AFTER = other_costs.reduce((s, x) => s + x.after_tax, 0);

  const SUB_BEFORE = G_XD_TOTAL_BEFORE + G_TB_BEFORE + G_QLDA_BEFORE + G_TV_BEFORE + G_K_BEFORE;
  const SUB_VAT = G_XD_TOTAL_VAT + G_TB_VAT + G_QLDA_VAT + G_TV_VAT + G_K_VAT;
  const SUB_AFTER = G_XD_TOTAL_AFTER + G_TB_AFTER + G_QLDA_AFTER + G_TV_AFTER + G_K_AFTER;

  // Dự phòng phí (G_DP = G_DP1 + G_DP2)
  const dp1_rate = Number(pi.contingency_volume_rate || 5.0) / 100.0;
  const dp2_rate = Number(pi.contingency_escalation_rate || 2.5) / 100.0;

  const G_DP1_BEFORE = Math.round(SUB_BEFORE * dp1_rate);
  const G_DP1_VAT = Math.round(SUB_VAT * dp1_rate);
  const G_DP1_AFTER = G_DP1_BEFORE + G_DP1_VAT;

  const G_DP2_BEFORE = Math.round(SUB_BEFORE * dp2_rate);
  const G_DP2_VAT = Math.round(SUB_VAT * dp2_rate);
  const G_DP2_AFTER = G_DP2_BEFORE + G_DP2_VAT;

  const G_DP_BEFORE = G_DP1_BEFORE + G_DP2_BEFORE;
  const G_DP_VAT = G_DP1_VAT + G_DP2_VAT;
  const G_DP_AFTER = G_DP1_AFTER + G_DP2_AFTER;

  const TOTAL_BEFORE = SUB_BEFORE + G_DP_BEFORE;
  const TOTAL_VAT = SUB_VAT + G_DP_VAT;
  const TOTAL_AFTER = SUB_AFTER + G_DP_AFTER;

  state.computed = {
    detailed_boq,
    aggResources,
    detailed_eq,
    b38: {
      VL: total_vl,
      NC: total_nc,
      M: total_m,
      T,
      rate_cpc,
      cpcLookup,
      C,
      rate_tl,
      TL,
      rate_tt,
      TT,
      G_XDTT,
      vat_pct: vat_rate * 100,
      GTGT_XD,
      G_XD_SAU_THUE_CHUA_LT,
      rate_lt,
      ltLookup,
      LT_TRUOC_THUE,
      LT_GTGT,
      LT_SAU_THUE,
      G_XD_TOTAL_BEFORE,
      G_XD_TOTAL_VAT,
      G_XD_TOTAL_AFTER
    },
    qlda: {
      rate_pct: rate_qlda,
      interp: qldaInterp,
      before_tax: G_QLDA_BEFORE,
      vat: G_QLDA_VAT,
      after_tax: G_QLDA_AFTER
    },
    consulting,
    other_costs,
    totals: {
      G_XD: { before: G_XD_TOTAL_BEFORE, vat: G_XD_TOTAL_VAT, after: G_XD_TOTAL_AFTER },
      G_TB: { before: G_TB_BEFORE, vat: G_TB_VAT, after: G_TB_AFTER },
      G_QLDA: { before: G_QLDA_BEFORE, vat: G_QLDA_VAT, after: G_QLDA_AFTER },
      G_TV: { before: G_TV_BEFORE, vat: G_TV_VAT, after: G_TV_AFTER },
      G_K: { before: G_K_BEFORE, vat: G_K_VAT, after: G_K_AFTER },
      SUB: { before: SUB_BEFORE, vat: SUB_VAT, after: SUB_AFTER },
      G_DP1: { rate_pct: dp1_rate * 100, before: G_DP1_BEFORE, vat: G_DP1_VAT, after: G_DP1_AFTER },
      G_DP2: { rate_pct: dp2_rate * 100, before: G_DP2_BEFORE, vat: G_DP2_VAT, after: G_DP2_AFTER },
      G_DP: { before: G_DP_BEFORE, vat: G_DP_VAT, after: G_DP_AFTER },
      TOTAL: { before: TOTAL_BEFORE, vat: TOTAL_VAT, after: TOTAL_AFTER }
    }
  };

  renderAll();
}

function renderAll() {
  const c = state.computed;
  if (!c) return;

  // 1. Update KPI Strip
  document.getElementById("kpiTotalAfterTax").textContent = fmtVND(c.totals.TOTAL.after);
  document.getElementById("kpiTotalBeforeTax").textContent = "Trước thuế: " + fmtVND(c.totals.TOTAL.before);

  document.getElementById("kpiGxdAfterTax").textContent = fmtVND(c.totals.G_XD.after);
  document.getElementById("kpiGxdBeforeTax").textContent = "Chi phí trực tiếp T: " + fmtVND(c.b38.T);
  document.getElementById("kpiCpcBadge").textContent = `CPC ${c.b38.rate_cpc}%`;

  document.getElementById("kpiGtbAfterTax").textContent = fmtVND(c.totals.G_TB.after);
  document.getElementById("kpiGtbBeforeTax").textContent = "Trước thuế: " + fmtVND(c.totals.G_TB.before);

  document.getElementById("kpiGqldaAfterTax").textContent = fmtVND(c.totals.G_QLDA.after);
  document.getElementById("kpiGqldaBeforeTax").textContent = `ĐM nội suy: ${c.qlda.rate_pct}%`;

  document.getElementById("kpiGtvGkAfterTax").textContent = fmtVND(c.totals.G_TV.after + c.totals.G_K.after);
  document.getElementById("kpiGtvGkSub").textContent = `TV: ${fmtNum(c.totals.G_TV.after)} | K: ${fmtNum(c.totals.G_K.after)}`;

  document.getElementById("kpiGdpAfterTax").textContent = fmtVND(c.totals.G_DP.after);
  document.getElementById("kpiGdpBeforeTax").textContent = `DP1 (${c.totals.G_DP1.rate_pct}%) + DP2 (${c.totals.G_DP2.rate_pct}%)`;

  document.getElementById("badgeBoqCount").textContent = c.detailed_boq.length;
  const totalRes = state.prices.vat_lieu.length + state.prices.nhan_cong.length + state.prices.may_thi_cong.length;
  document.getElementById("badgeResCount").textContent = totalRes;

  renderActiveRatesTable();
  renderBoqTable();
  renderEquipmentTable();
  renderResourcesTable();
  renderUnitPriceAnalysis();
  renderBang38Table();
  renderTotalEstimateTable();
  renderBang33Reference();
  renderNormDatabase();
  runInteractiveInterpolation();
}

function renderActiveRatesTable() {
  const c = state.computed;
  const tbody = document.getElementById("activeRatesTbody");
  const rows = [
    {
      stt: 1,
      name: "Định mức Chi phí chung (C) tính trên chi phí trực tiếp",
      basis: "Bảng 3.3 Phụ lục III Thông tư 36/2026/TT-BXD",
      method: c.b38.cpcLookup.matched_label,
      rate: c.b38.rate_cpc.toFixed(2) + "%"
    },
    {
      stt: 2,
      name: "Định mức Chi phí một số công việc không xác định được khối lượng từ thiết kế (TT)",
      basis: "Bảng 3.5 Phụ lục III Thông tư 36/2026/TT-BXD",
      method: "Tra trực tiếp theo loại công trình",
      rate: c.b38.rate_tt.toFixed(2) + "%"
    },
    {
      stt: 3,
      name: "Định mức Thu nhập chịu thuế tính trước (TL) tính trên (T + C)",
      basis: "Bảng 3.6 Phụ lục III Thông tư 36/2026/TT-BXD",
      method: "Tra trực tiếp theo loại công trình",
      rate: c.b38.rate_tl.toFixed(2) + "%"
    },
    {
      stt: 4,
      name: "Định mức Chi phí nhà tạm để ở và điều hành thi công (LT)",
      basis: "Bảng 3.7, 3.8 PL III TT 36/2026 (Đã đính chính bởi QĐ 1538/QĐ-BXD)",
      method: `Tra cận trên (${c.b38.ltLookup.matched_label}): LT = G_XDTT × ${c.b38.rate_lt}% × (1 + T_GTGT)`,
      rate: c.b38.rate_lt.toFixed(2) + "%"
    },
    {
      stt: 5,
      name: "Định mức Chi phí Quản lý dự án (G_QLDA)",
      basis: "Bảng 1.1 Phụ lục VIII Thông tư 38/2026/TT-BXD",
      method: c.qlda.interp.formula,
      rate: c.qlda.rate_pct.toFixed(4) + "%"
    }
  ];

  c.consulting.forEach((tv, i) => {
    rows.push({
      stt: 6 + i,
      name: tv.name,
      basis: `Phụ lục VIII Thông tư 38/2026/TT-BXD (Tính trên ${tv.basis})`,
      method: tv.formula,
      rate: tv.rate_pct.toFixed(4) + "%"
    });
  });

  tbody.innerHTML = rows.map(r => `
    <tr>
      <td class="center">${r.stt}</td>
      <td><strong>${r.name}</strong></td>
      <td>${r.basis}</td>
      <td><code>${r.method}</code></td>
      <td class="num"><strong>${r.rate}</strong></td>
    </tr>
  `).join("");
}

function renderBoqTable() {
  const c = state.computed;
  const tbody = document.getElementById("boqTbody");
  let html = "";
  let currentSection = "";

  c.detailed_boq.forEach((row, idx) => {
    if (row.section !== currentSection) {
      currentSection = row.section;
      html += `
        <tr class="section-row">
          <td colspan="12">${currentSection}</td>
        </tr>
      `;
    }
    html += `
      <tr>
        <td class="center">${row.stt}</td>
        <td><span class="code-pill">${row.norm_code}</span></td>
        <td>
          <input type="text" class="inline-input" value="${row.name}" onchange="updateBoqField(${idx}, 'custom_name', this.value)" />
        </td>
        <td class="center">${row.unit}</td>
        <td class="num">
          <input type="number" step="any" class="inline-input num-input" style="width:66px" value="${row.count}" onchange="updateBoqDimension(${idx}, 'count', this.value)" />
        </td>
        <td class="num">
          <input type="number" step="any" class="inline-input num-input" style="width:72px" value="${row.length}" onchange="updateBoqDimension(${idx}, 'length', this.value)" />
        </td>
        <td class="num">
          <input type="number" step="any" class="inline-input num-input" style="width:66px" value="${row.width}" onchange="updateBoqDimension(${idx}, 'width', this.value)" />
        </td>
        <td class="num">
          <input type="number" step="any" class="inline-input num-input" style="width:66px" value="${row.height}" onchange="updateBoqDimension(${idx}, 'height', this.value)" />
        </td>
        <td class="num">
          <input type="number" step="any" class="inline-input num-input" style="width:88px; font-weight:700;" value="${row.quantity}" onchange="updateBoqQuantityDirect(${idx}, this.value)" />
        </td>
        <td class="num">${fmtNum(row.unit_direct)}</td>
        <td class="num"><strong>${fmtNum(row.total_direct)}</strong></td>
        <td class="center no-print">
          <button class="btn btn-danger btn-sm" onclick="removeBoqItem(${idx})" title="Xóa công tác">✕</button>
        </td>
      </tr>
    `;
  });

  html += `
    <tr class="total-row">
      <td colspan="9" class="num">TỔNG CHI PHÍ TRỰC TIẾP (T = VL + NC + M):</td>
      <td class="num">—</td>
      <td class="num">${fmtVND(c.b38.T)}</td>
      <td class="no-print"></td>
    </tr>
  `;
  tbody.innerHTML = html;
}

function updateBoqField(idx, field, val) {
  state.boq_items[idx][field] = val;
  calculateAll();
}

function updateBoqDimension(idx, field, val) {
  const item = state.boq_items[idx];
  item[field] = Number(val || 0);
  const q = Number(item.count || 1) * Number(item.length || 1) * Number(item.width || 1) * Number(item.height || 1) * Number(item.factor || 1);
  item.quantity = Number(q.toFixed(3));
  calculateAll();
}

function updateBoqQuantityDirect(idx, val) {
  const q = Number(val || 0);
  state.boq_items[idx].quantity = q;
  state.boq_items[idx].count = 1;
  state.boq_items[idx].length = q;
  state.boq_items[idx].width = 1;
  state.boq_items[idx].height = 1;
  calculateAll();
}

function addBoqItem() {
  const normCode = document.getElementById("addNormSelect").value;
  const section = document.getElementById("addSectionInput").value || "I. HẠNG MỤC BỔ SUNG";
  const norm = state.norms.find(n => n.code === normCode) || state.norms[0];
  state.boq_items.push({
    id: Date.now(),
    section,
    norm_code: norm.code,
    custom_name: norm.name,
    formula: "10.0",
    count: 1,
    length: 10.0,
    width: 1.0,
    height: 1.0,
    factor: 1.0,
    quantity: 10.0
  });
  calculateAll();
}

function removeBoqItem(idx) {
  state.boq_items.splice(idx, 1);
  calculateAll();
}

function renderEquipmentTable() {
  const c = state.computed;
  const tbody = document.getElementById("equipmentTbody");
  let html = c.detailed_eq.map((eq, idx) => `
    <tr>
      <td class="center">${eq.stt}</td>
      <td><input type="text" class="inline-input" value="${eq.name}" onchange="updateEqField(${idx}, 'name', this.value)" /></td>
      <td class="center"><input type="text" class="inline-input center" style="width:75px" value="${eq.unit}" onchange="updateEqField(${idx}, 'unit', this.value)" /></td>
      <td class="num"><input type="number" step="any" class="inline-input num-input" value="${eq.quantity}" onchange="updateEqField(${idx}, 'quantity', this.value)" /></td>
      <td class="num"><input type="number" step="1000" class="inline-input num-input" style="width:135px" value="${eq.unit_price}" onchange="updateEqField(${idx}, 'unit_price', this.value)" /></td>
      <td class="num">${fmtNum(eq.before_tax)}</td>
      <td class="num">${fmtNum(eq.vat)}</td>
      <td class="num"><strong>${fmtNum(eq.after_tax)}</strong></td>
      <td class="center no-print"><button class="btn btn-danger btn-sm" onclick="removeEquipmentItem(${idx})">✕</button></td>
    </tr>
  `).join("");

  html += `
    <tr class="total-row">
      <td colspan="5" class="num">TỔNG CHI PHÍ THIẾT BỊ (G_TB):</td>
      <td class="num">${fmtVND(c.totals.G_TB.before)}</td>
      <td class="num">${fmtVND(c.totals.G_TB.vat)}</td>
      <td class="num">${fmtVND(c.totals.G_TB.after)}</td>
      <td class="no-print"></td>
    </tr>
  `;
  tbody.innerHTML = html;
}

function updateEqField(idx, field, val) {
  state.equipment_items[idx][field] = (field === "quantity" || field === "unit_price") ? Number(val || 0) : val;
  calculateAll();
}

function addEquipmentItem() {
  state.equipment_items.push({
    id: Date.now(),
    name: "Thiết bị công trình bổ sung đồng bộ",
    unit: "hệ thống",
    quantity: 1,
    unit_price: 150000000
  });
  calculateAll();
}

function removeEquipmentItem(idx) {
  state.equipment_items.splice(idx, 1);
  calculateAll();
}

function renderResourcesTable() {
  const c = state.computed;
  const q = (document.getElementById("resourceSearchInput")?.value || "").toLowerCase();
  const fType = document.getElementById("resourceFilterType")?.value || "ALL";

  const allRes = [
    ...state.prices.vat_lieu.map((r, i) => ({ ...r, type: "VL", arrKey: "vat_lieu", idx: i })),
    ...state.prices.nhan_cong.map((r, i) => ({ ...r, type: "NC", arrKey: "nhan_cong", idx: i })),
    ...state.prices.may_thi_cong.map((r, i) => ({ ...r, type: "M", arrKey: "may_thi_cong", idx: i }))
  ];

  const filtered = allRes.filter(r => {
    if (fType !== "ALL" && r.type !== fType) return false;
    if (q && !(r.id.toLowerCase().includes(q) || r.name.toLowerCase().includes(q))) return false;
    return true;
  });

  const tbody = document.getElementById("resourcesTbody");
  tbody.innerHTML = filtered.map((r, idx) => {
    const agg = c.aggResources[r.id] || { total_qty: 0, total_cost: 0 };
    const k = r.type === "NC" ? state.project_info.k_nc : (r.type === "M" ? state.project_info.k_m : 1.0);
    const badgeClass = r.type === "VL" ? "badge-info" : (r.type === "NC" ? "badge-success" : "badge-warn");
    return `
      <tr>
        <td class="center">${idx + 1}</td>
        <td><span class="code-pill">${r.id}</span></td>
        <td class="center"><span class="badge ${badgeClass}">${r.type}</span></td>
        <td>${r.name}</td>
        <td class="center">${r.unit}</td>
        <td class="num">
          <input type="number" step="100" class="inline-input num-input" style="width:120px" value="${r.price}" onchange="updateResourcePrice('${r.arrKey}', ${r.idx}, this.value)" />
        </td>
        <td class="num">${Number(k).toFixed(2)}</td>
        <td class="num">${fmtNum(agg.total_qty, 3)}</td>
        <td class="num"><strong>${fmtNum(agg.total_cost, 0)}</strong></td>
        <td><span style="font-size:12px; color:var(--text-muted)">${r.source || ""}</span></td>
      </tr>
    `;
  }).join("");
}

function updateResourcePrice(arrKey, idx, val) {
  state.prices[arrKey][idx].price = Number(val || 0);
  calculateAll();
}

function renderUnitPriceAnalysis() {
  const c = state.computed;
  const showComp = document.getElementById("toggleShowComponents")?.checked !== false;
  const tbody = document.getElementById("unitPriceAnalysisTbody");
  let html = "";

  c.detailed_boq.forEach(row => {
    html += `
      <tr class="section-row">
        <td class="center">${row.stt}</td>
        <td><span class="code-pill">${row.norm_code}</span></td>
        <td>${row.name} <span style="font-weight:400; color:var(--text-muted)">(VL: ${fmtNum(row.unit_vl)} | NC: ${fmtNum(row.unit_nc)} | M: ${fmtNum(row.unit_m)})</span></td>
        <td class="center">${row.unit}</td>
        <td class="num">1,000</td>
        <td class="num">${fmtNum(row.quantity, 3)}</td>
        <td class="num">—</td>
        <td class="num"><strong>${fmtNum(row.unit_direct)}</strong></td>
        <td class="num"><strong>${fmtNum(row.total_direct)}</strong></td>
      </tr>
    `;
    if (showComp) {
      row.components.forEach(comp => {
        html += `
          <tr>
            <td class="center" style="color:var(--text-muted)">•</td>
            <td><code>${comp.id}</code> <span class="badge badge-info" style="font-size:10px">${comp.type}</span></td>
            <td style="padding-left:22px;">${comp.name}</td>
            <td class="center">${comp.unit}</td>
            <td class="num">${fmtNum(comp.norm_qty, 4)}</td>
            <td class="num">${fmtNum(comp.total_qty, 3)}</td>
            <td class="num">${fmtNum(comp.unit_price, 0)}</td>
            <td class="num">${fmtNum(comp.unit_cost, 0)}</td>
            <td class="num">${fmtNum(comp.total_cost, 0)}</td>
          </tr>
        `;
      });
    }
  });
  tbody.innerHTML = html;
}

function renderBang38Table() {
  const b = state.computed.b38;
  document.getElementById("bang38Subtitle").textContent =
    `${state.project_info.project_name} — ${state.project_info.building_name}`;

  const rows = [
    { stt: "I", name: "CHI PHÍ TRỰC TIẾP", formula: "T = VL + NC + M", sym: "T", val: b.T, note: "Tổng hợp từ Bảng Tiên lượng & Đơn giá chi tiết", bold: true },
    { stt: "1", name: "Chi phí vật liệu", formula: "∑ (KL_i × ĐG_VL_i)", sym: "VL", val: b.VL, note: "Theo công bố giá VLXD địa phương & TT 38/2026" },
    { stt: "2", name: "Chi phí nhân công", formula: `∑ (KL_i × ĐG_NC_i) × K_NC (${state.project_info.k_nc})`, sym: "NC", val: b.NC, note: "Đơn giá nhân công theo Thông tư 37/2026/TT-BXD" },
    { stt: "3", name: "Chi phí máy và thiết bị thi công", formula: `∑ (KL_i × ĐG_M_i) × K_M (${state.project_info.k_m})`, sym: "M", val: b.M, note: "Bảng giá ca máy theo Thông tư 37/2026/TT-BXD" },
    { stt: "II", name: "CHI PHÍ GIÁN TIẾP", formula: "GT = C + LT + TT", sym: "GT", val: b.C + b.TT + b.LT_TRUOC_THUE, note: "Theo Điều 13 Nghị định 206/2026/NĐ-CP & TT 36/2026", bold: true },
    { stt: "1", name: "Chi phí chung", formula: `T × ${b.rate_cpc}%`, sym: "C", val: b.C, note: `Bảng 3.3 PL III TT 36/2026 (${b.cpcLookup.matched_label})` },
    { stt: "2", name: "Chi phí một số công việc không xác định được khối lượng từ thiết kế", formula: `T × ${b.rate_tt}%`, sym: "TT", val: b.TT, note: "Bảng 3.5 Phụ lục III Thông tư 36/2026/TT-BXD" },
    { stt: "III", name: "THU NHẬP CHỊU THUẾ TÍNH TRƯỚC", formula: `(T + C) × ${b.rate_tl}%`, sym: "TL", val: b.TL, note: "Bảng 3.6 Phụ lục III Thông tư 36/2026/TT-BXD", bold: true },
    { stt: "IV", name: "CHI PHÍ XÂY DỰNG TRƯỚC THUẾ (Chưa gồm nhà tạm)", formula: "G = T + C + TL + TT", sym: "G_XDTT", val: b.G_XDTT, note: "Bảng 3.8 Phụ lục III Thông tư 36/2026/TT-BXD", bold: true },
    { stt: "V", name: "THUẾ GIÁ TRỊ GIA TĂNG XÂY DỰNG", formula: `G_XDTT × ${b.vat_pct}%`, sym: "GTGT", val: b.GTGT_XD, note: "Thuế suất GTGT hiện hành", bold: true },
    { stt: "VI", name: "CHI PHÍ XÂY DỰNG SAU THUẾ (Chưa gồm nhà tạm)", formula: "G_XDTT + GTGT", sym: "G_XDST", val: b.G_XD_SAU_THUE_CHUA_LT, note: "Bảng 3.8 Phụ lục III Thông tư 36/2026/TT-BXD", bold: true },
    { stt: "VII", name: "CHI PHÍ NHÀ TẠM ĐỂ Ở VÀ ĐIỀU HÀNH THI CÔNG (Sau thuế)", formula: `G_XDTT × ${b.rate_lt}% × (1 + ${b.vat_pct}%)`, sym: "LT", val: b.LT_SAU_THUE, note: `Đính chính theo QĐ 1538/QĐ-BXD (Trước thuế: ${fmtNum(b.LT_TRUOC_THUE)} đ; GTGT: ${fmtNum(b.LT_GTGT)} đ)`, bold: true },
    { stt: "TỔNG", name: "TỔNG CỘNG CHI PHÍ XÂY DỰNG HẠNG MỤC (SAU THUẾ, GỒM NHÀ TẠM)", formula: "G_XDST + LT", sym: "G_XD", val: b.G_XD_TOTAL_AFTER, note: `Trước thuế (gồm LT): ${fmtNum(b.G_XD_TOTAL_BEFORE)} đ`, grand: true }
  ];

  document.getElementById("bang38Tbody").innerHTML = rows.map(r => `
    <tr class="${r.grand ? 'grand-total-row' : (r.bold ? 'section-row' : '')}">
      <td class="center">${r.stt}</td>
      <td>${r.name}</td>
      <td><code>${r.formula}</code></td>
      <td class="center"><strong>${r.sym}</strong></td>
      <td class="num">${fmtNum(r.val)}</td>
      <td>${r.note}</td>
    </tr>
  `).join("");
}

function renderTotalEstimateTable() {
  const c = state.computed;
  const t = c.totals;
  const totalAfter = t.TOTAL.after || 1;

  // Render visual cost breakdown bar
  const segments = [
    { label: "Chi phí xây dựng (G_XD)", val: t.G_XD.after, color: "#0b4f6c" },
    { label: "Chi phí thiết bị (G_TB)", val: t.G_TB.after, color: "#0284c7" },
    { label: "Quản lý dự án (G_QLDA)", val: t.G_QLDA.after, color: "#15803d" },
    { label: "Tư vấn ĐTXD (G_TV)", val: t.G_TV.after, color: "#b45309" },
    { label: "Chi phí khác (G_K)", val: t.G_K.after, color: "#6366f1" },
    { label: "Chi phí dự phòng (G_DP)", val: t.G_DP.after, color: "#dc2626" }
  ];

  document.getElementById("costStructureBar").innerHTML = segments.map(s => {
    const pct = ((s.val / totalAfter) * 100).toFixed(2);
    return `<div class="cost-bar-segment" style="width:${pct}%; background:${s.color};" title="${s.label}: ${fmtVND(s.val)} (${pct}%)"></div>`;
  }).join("");

  document.getElementById("costStructureLegend").innerHTML = segments.map(s => {
    const pct = ((s.val / totalAfter) * 100).toFixed(1);
    return `
      <div class="legend-item">
        <span class="legend-dot" style="background:${s.color}"></span>
        <span><strong>${s.label}:</strong> ${pct}% (${fmtVND(s.val)})</span>
      </div>
    `;
  }).join("");

  let html = "";
  const mainRows = [
    {
      stt: "I",
      name: "CHI PHÍ XÂY DỰNG (G_XD)",
      basis: "Bảng 3.8 Phụ lục III TT 36/2026 & QĐ 1538/QĐ-BXD",
      rate: "—",
      before: t.G_XD.before,
      vat: t.G_XD.vat,
      after: t.G_XD.after,
      section: true
    },
    {
      stt: "II",
      name: "CHI PHÍ THIẾT BỊ (G_TB)",
      basis: "Chương II Thông tư 36/2026/TT-BXD",
      rate: "—",
      before: t.G_TB.before,
      vat: t.G_TB.vat,
      after: t.G_TB.after,
      section: true
    },
    {
      stt: "III",
      name: "CHI PHÍ QUẢN LÝ DỰ ÁN (G_QLDA)",
      basis: "Bảng 1.1 Phụ lục VIII Thông tư 38/2026/TT-BXD",
      rate: c.qlda.rate_pct.toFixed(4) + "%",
      before: t.G_QLDA.before,
      vat: t.G_QLDA.vat,
      after: t.G_QLDA.after,
      section: true
    },
    {
      stt: "IV",
      name: "CHI PHÍ TƯ VẤN ĐẦU TƯ XÂY DỰNG (G_TV)",
      basis: "Phần II Phụ lục VIII Thông tư 38/2026/TT-BXD",
      rate: "Tổng hợp",
      before: t.G_TV.before,
      vat: t.G_TV.vat,
      after: t.G_TV.after,
      section: true,
      children: c.consulting
    },
    {
      stt: "V",
      name: "CHI PHÍ KHÁC (G_K)",
      basis: "Điều 11 Nghị định 206/2026/NĐ-CP & TT 36/2026",
      rate: "Tổng hợp",
      before: t.G_K.before,
      vat: t.G_K.vat,
      after: t.G_K.after,
      section: true,
      children: c.other_costs
    },
    {
      stt: "VI",
      name: "CHI PHÍ DỰ PHÒNG (G_DP = G_DP1 + G_DP2)",
      basis: "Điều 12 Nghị định 206/2026/NĐ-CP",
      rate: (t.G_DP1.rate_pct + t.G_DP2.rate_pct).toFixed(2) + "%",
      before: t.G_DP.before,
      vat: t.G_DP.vat,
      after: t.G_DP.after,
      section: true,
      children: [
        {
          code: "DP.01",
          name: "Dự phòng chi phí cho yếu tố khối lượng công việc phát sinh (G_DP1)",
          basis: `${t.G_DP1.rate_pct}% × (G_XD + G_TB + G_QLDA + G_TV + G_K)`,
          rate_pct: t.G_DP1.rate_pct,
          before_tax: t.G_DP1.before,
          vat: t.G_DP1.vat,
          after_tax: t.G_DP1.after
        },
        {
          code: "DP.02",
          name: "Dự phòng chi phí cho yếu tố trượt giá trong thời gian thực hiện (G_DP2)",
          basis: `${t.G_DP2.rate_pct}% × (G_XD + G_TB + G_QLDA + G_TV + G_K)`,
          rate_pct: t.G_DP2.rate_pct,
          before_tax: t.G_DP2.before,
          vat: t.G_DP2.vat,
          after_tax: t.G_DP2.after
        }
      ]
    }
  ];

  mainRows.forEach(r => {
    const pct = ((r.after / totalAfter) * 100).toFixed(2) + "%";
    html += `
      <tr class="section-row">
        <td class="center">${r.stt}</td>
        <td>${r.name}</td>
        <td>${r.basis}</td>
        <td class="num">${r.rate}</td>
        <td class="num">${fmtNum(r.before)}</td>
        <td class="num">${fmtNum(r.vat)}</td>
        <td class="num">${fmtNum(r.after)}</td>
        <td class="num">${pct}</td>
      </tr>
    `;
    if (r.children) {
      r.children.forEach((ch, idx) => {
        const chPct = ((ch.after_tax / totalAfter) * 100).toFixed(2) + "%";
        html += `
          <tr>
            <td class="center">${idx + 1}</td>
            <td style="padding-left:20px;">${ch.name}</td>
            <td><span style="font-size:12px; color:var(--text-muted)">${ch.basis}</span></td>
            <td class="num">${Number(ch.rate_pct).toFixed(3)}%</td>
            <td class="num">${fmtNum(ch.before_tax)}</td>
            <td class="num">${fmtNum(ch.vat)}</td>
            <td class="num">${fmtNum(ch.after_tax)}</td>
            <td class="num">${chPct}</td>
          </tr>
        `;
      });
    }
  });

  html += `
    <tr class="grand-total-row">
      <td class="center">TỔNG</td>
      <td>TỔNG DỰ TOÁN XÂY DỰNG CÔNG TRÌNH (G_DTXD = I + II + III + IV + V + VI)</td>
      <td>Nghị định 206/2026/NĐ-CP & TT 36/2026/TT-BXD</td>
      <td class="num">100%</td>
      <td class="num">${fmtNum(t.TOTAL.before)}</td>
      <td class="num">${fmtNum(t.TOTAL.vat)}</td>
      <td class="num">${fmtNum(t.TOTAL.after)}</td>
      <td class="num">100,00%</td>
    </tr>
  `;
  document.getElementById("totalEstimateTbody").innerHTML = html;
}

function renderBang33Reference() {
  const b33 = state.regulations.tt36_phu_luc_3.bang_3_3_cpc_du_toan.rates;
  const labels = {
    dan_dung: "1. Công trình Dân dụng",
    dan_dung_di_tich: "— Tu bổ, phục hồi di tích lịch sử - văn hóa",
    cong_nghiep: "2. Công trình Công nghiệp",
    cong_nghiep_ham: "— Công trình hầm thủy điện, hầm lò",
    giao_thong: "3. Công trình Giao thông",
    nong_nghiep: "4. Công trình Nông nghiệp & PTNT",
    ha_tang_ky_thuat: "5. Công trình Hạ tầng kỹ thuật"
  };

  document.getElementById("bang33RefTbody").innerHTML = Object.entries(labels).map(([k, title]) => {
    const arr = b33[k] || [];
    return `
      <tr>
        <td><strong>${title}</strong></td>
        ${arr.map(v => `<td class="num">${v.toFixed(1)}%</td>`).join("")}
      </tr>
    `;
  }).join("");
}

function renderNormDatabase() {
  const q = (document.getElementById("normSearchInput")?.value || "").toLowerCase();
  const resMap = {};
  state.prices.vat_lieu.forEach(r => resMap[r.id] = r.name);
  state.prices.nhan_cong.forEach(r => resMap[r.id] = r.name);
  state.prices.may_thi_cong.forEach(r => resMap[r.id] = r.name);

  const filtered = state.norms.filter(n => {
    if (!q) return true;
    return n.code.toLowerCase().includes(q) || n.name.toLowerCase().includes(q) || n.category.toLowerCase().includes(q);
  });

  document.getElementById("normDatabaseTbody").innerHTML = filtered.map(n => {
    const parts = [
      ...(n.vl || []).map(x => `VL ${x.id}: ${x.qty}`),
      ...(n.nc || []).map(x => `NC ${x.id}: ${x.qty}`),
      ...(n.m || []).map(x => `M ${x.id}: ${x.qty}`)
    ].join(" | ");
    return `
      <tr>
        <td><span class="code-pill">${n.code}</span></td>
        <td><span style="font-size:12px; color:var(--text-secondary)">${n.category}</span></td>
        <td><strong>${n.name}</strong></td>
        <td class="center">${n.unit}</td>
        <td><code style="font-size:11.5px;">${parts}</code></td>
        <td class="center no-print">
          <button class="btn btn-primary btn-sm" onclick="quickAddNormToBoq('${n.code}')">+ Đưa vào BOQ</button>
        </td>
      </tr>
    `;
  }).join("");
}

function quickAddNormToBoq(code) {
  const norm = state.norms.find(n => n.code === code);
  if (!norm) return;
  state.boq_items.push({
    id: Date.now(),
    section: "I. CÔNG TÁC BỔ SUNG TỪ THƯ VIỆN TT38",
    norm_code: norm.code,
    custom_name: norm.name,
    formula: "10.0",
    count: 1,
    length: 10,
    width: 1,
    height: 1,
    factor: 1,
    quantity: 10
  });
  calculateAll();
  switchTab("tab-2");
}

function runInteractiveInterpolation() {
  const tblKey = document.getElementById("calcTableSelect").value;
  const typeOrGrade = document.getElementById("calcTypeOrGradeSelect").value;
  const gt = Number(document.getElementById("calcGtInput").value || 10.0);

  const tbl = state.regulations.tt38_phu_luc_8[tblKey];
  if (!tbl) return;

  let rates;
  if (tbl.rates_by_grade) {
    const gKey = typeOrGrade.startsWith("cap_") || typeOrGrade === "dac_biet" ? typeOrGrade : "cap_3";
    rates = tbl.rates_by_grade[gKey] || tbl.rates_by_grade.cap_3;
  } else {
    const tKey = (typeOrGrade === "cong_nghiep" || typeOrGrade === "cap_2") ? "cong_nghiep" : "dan_dung";
    rates = tbl.rates[tKey] || tbl.rates.dan_dung;
  }

  const res = interpolateRateTT38(gt, tbl.thresholds_ty_dong, rates);
  const valMoney = Math.round(gt * 1e9 * (res.rate / 100.0));

  document.getElementById("interpResultBox").innerHTML = `
    <div><strong>Bảng tra:</strong> ${tbl.title} (${tbl.unit})</div>
    <div style="margin-top:4px;"><strong>Cận dưới (G_b):</strong> ${res.gb} tỷ (${res.nb}%) &nbsp;|&nbsp; <strong>Cận trên (G_a):</strong> ${res.ga} tỷ (${res.na}%)</div>
    <div style="margin-top:4px;"><strong>Công thức nội suy:</strong> <code>${res.formula}</code></div>
    <div style="margin-top:6px; font-size:15px;">
      ⇒ <strong>Định mức nội suy N_t = <span style="color:var(--accent-primary)">${res.rate.toFixed(4)}%</span></strong>
      &nbsp; (Thành tiền trước thuế tương ứng: <strong>${fmtVND(valMoney)}</strong>)
    </div>
  `;
}

function syncProjectInfoToUI() {
  const pi = state.project_info;
  document.getElementById("inpProjectName").value = pi.project_name || "";
  document.getElementById("inpBuildingName").value = pi.building_name || "";
  document.getElementById("inpInvestor").value = pi.investor || "";
  document.getElementById("inpLocation").value = pi.location || "";
  document.getElementById("inpBuildingType").value = pi.building_type || "dan_dung";
  document.getElementById("inpBuildingGrade").value = pi.building_grade || "cap_3";

  if (pi.is_bcktkt) {
    document.getElementById("inpReportType").value = "bcktkt_1_buoc";
  } else if (pi.design_step === "tkkt_3_buoc") {
    document.getElementById("inpReportType").value = "bcnckt_3_buoc";
  } else {
    document.getElementById("inpReportType").value = "bcnckt_2_buoc";
  }

  document.getElementById("inpTmdtGxdTy").value = pi.tmdt_gxdtt_approved_ty || 15.0;
  document.getElementById("inpVatRate").value = pi.vat_rate ?? 8.0;
  document.getElementById("inpKnc").value = pi.k_nc ?? 1.0;
  document.getElementById("inpKm").value = pi.k_m ?? 1.0;
  document.getElementById("inpDp1Rate").value = pi.contingency_volume_rate ?? 5.0;
  document.getElementById("inpDp2Rate").value = pi.contingency_escalation_rate ?? 2.5;

  if (pi.is_linear_project) {
    document.getElementById("inpSpecialZone").value = "linear";
  } else if (pi.is_mountain_island) {
    document.getElementById("inpSpecialZone").value = "mountain";
  } else {
    document.getElementById("inpSpecialZone").value = "normal";
  }
}

function updateProjectInfoFromUI() {
  const pi = state.project_info;
  pi.project_name = document.getElementById("inpProjectName").value;
  pi.building_name = document.getElementById("inpBuildingName").value;
  pi.investor = document.getElementById("inpInvestor").value;
  pi.location = document.getElementById("inpLocation").value;
  pi.building_type = document.getElementById("inpBuildingType").value;
  pi.building_grade = document.getElementById("inpBuildingGrade").value;

  const rep = document.getElementById("inpReportType").value;
  pi.is_bcktkt = (rep === "bcktkt_1_buoc");
  pi.design_step = (rep === "bcnckt_3_buoc") ? "tkkt_3_buoc" : "tkbvtc_2_buoc";

  pi.tmdt_gxdtt_approved_ty = Number(document.getElementById("inpTmdtGxdTy").value || 15.0);
  pi.vat_rate = Number(document.getElementById("inpVatRate").value || 8.0);
  pi.k_nc = Number(document.getElementById("inpKnc").value || 1.0);
  pi.k_m = Number(document.getElementById("inpKm").value || 1.0);
  pi.contingency_volume_rate = Number(document.getElementById("inpDp1Rate").value || 5.0);
  pi.contingency_escalation_rate = Number(document.getElementById("inpDp2Rate").value || 2.5);

  const sz = document.getElementById("inpSpecialZone").value;
  pi.is_linear_project = (sz === "linear");
  pi.is_mountain_island = (sz === "mountain");

  calculateAll();
}

function loadPreset(presetKey) {
  const p = EMBEDDED_PRESETS.presets[presetKey] || EMBEDDED_PRESETS.presets.dan_dung_tru_so;
  state.project_info = JSON.parse(JSON.stringify(p.project_info));
  state.boq_items = JSON.parse(JSON.stringify(p.boq_items));
  state.equipment_items = JSON.parse(JSON.stringify(p.equipment_items));
  syncProjectInfoToUI();
  calculateAll();
}

function switchTab(tabId) {
  document.querySelectorAll(".nav-tab").forEach(btn => {
    btn.classList.toggle("active", btn.getAttribute("data-tab") === tabId);
  });
  document.querySelectorAll(".tab-panel").forEach(panel => {
    panel.classList.toggle("active", panel.id === tabId);
  });
}

function toggleTheme() {
  const html = document.documentElement;
  const next = html.getAttribute("data-theme") === "dark" ? "light" : "dark";
  html.setAttribute("data-theme", next);
  document.getElementById("themeToggleBtn").textContent = next === "dark" ? "☀️ Giao diện Sáng" : "🌙 Giao diện Tối";
}

function exportProjectJSON() {
  const payload = {
    exported_at: new Date().toISOString(),
    legal_version: "ND206_TT36_TT37_TT38_2026",
    project_info: state.project_info,
    boq_items: state.boq_items,
    equipment_items: state.equipment_items,
    prices: state.prices
  };
  const blob = new Blob([JSON.stringify(payload, null, 2)], { type: "application/json" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "Ho_So_Du_Toan_2026.json";
  a.click();
}

function importProjectJSON(event) {
  const file = event.target.files?.[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = e => {
    try {
      const data = JSON.parse(e.target.result);
      if (data.project_info) state.project_info = data.project_info;
      if (data.boq_items) state.boq_items = data.boq_items;
      if (data.equipment_items) state.equipment_items = data.equipment_items;
      if (data.prices) state.prices = data.prices;
      syncProjectInfoToUI();
      calculateAll();
    } catch (err) {
      alert("File JSON không hợp lệ: " + err.message);
    }
  };
  reader.readAsText(file);
}

function exportExcelWorkbook() {
  const c = state.computed;
  const pi = state.project_info;

  const esc = s => String(s ?? "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

  // Build XML Spreadsheet 2003 with multiple worksheets
  let xml = `<?xml version="1.0" encoding="UTF-8"?>
<?mso-application progid="Excel.Sheet"?>
<Workbook xmlns="urn:schemas-microsoft-com:office:spreadsheet"
 xmlns:ss="urn:schemas-microsoft-com:office:spreadsheet">
 <Styles>
  <Style ss:ID="Header"><Font ss:Bold="1" ss:Color="#FFFFFF"/><Interior ss:Color="#0F172A" ss:Pattern="Solid"/></Style>
  <Style ss:ID="Bold"><Font ss:Bold="1"/></Style>
  <Style ss:ID="Num"><NumberFormat ss:Format="#,##0"/></Style>
 </Styles>
 <Worksheet ss:Name="01_TH_DU_TOAN_CT">
  <Table>
   <Row><Cell ss:StyleID="Bold"><Data ss:Type="String">${esc(pi.project_name)}</Data></Cell></Row>
   <Row><Cell><Data ss:Type="String">${esc(pi.building_name)}</Data></Cell></Row>
   <Row><Cell ss:StyleID="Header"><Data ss:Type="String">Khoản mục chi phí</Data></Cell><Cell ss:StyleID="Header"><Data ss:Type="String">Trước thuế (VNĐ)</Data></Cell><Cell ss:StyleID="Header"><Data ss:Type="String">Thuế GTGT (VNĐ)</Data></Cell><Cell ss:StyleID="Header"><Data ss:Type="String">Sau thuế (VNĐ)</Data></Cell></Row>
   <Row><Cell><Data ss:Type="String">I. Chi phí xây dựng (G_XD)</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.totals.G_XD.before}</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.totals.G_XD.vat}</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.totals.G_XD.after}</Data></Cell></Row>
   <Row><Cell><Data ss:Type="String">II. Chi phí thiết bị (G_TB)</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.totals.G_TB.before}</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.totals.G_TB.vat}</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.totals.G_TB.after}</Data></Cell></Row>
   <Row><Cell><Data ss:Type="String">III. Chi phí quản lý dự án (G_QLDA)</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.totals.G_QLDA.before}</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.totals.G_QLDA.vat}</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.totals.G_QLDA.after}</Data></Cell></Row>
   <Row><Cell><Data ss:Type="String">IV. Chi phí tư vấn đầu tư xây dựng (G_TV)</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.totals.G_TV.before}</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.totals.G_TV.vat}</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.totals.G_TV.after}</Data></Cell></Row>
   <Row><Cell><Data ss:Type="String">V. Chi phí khác (G_K)</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.totals.G_K.before}</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.totals.G_K.vat}</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.totals.G_K.after}</Data></Cell></Row>
   <Row><Cell><Data ss:Type="String">VI. Chi phí dự phòng (G_DP)</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.totals.G_DP.before}</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.totals.G_DP.vat}</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.totals.G_DP.after}</Data></Cell></Row>
   <Row><Cell ss:StyleID="Bold"><Data ss:Type="String">TỔNG DỰ TOÁN XÂY DỰNG CÔNG TRÌNH</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.totals.TOTAL.before}</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.totals.TOTAL.vat}</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.totals.TOTAL.after}</Data></Cell></Row>
  </Table>
 </Worksheet>
 <Worksheet ss:Name="02_BANG_3_8_CHI_PHI_XD">
  <Table>
   <Row><Cell ss:StyleID="Header"><Data ss:Type="String">Ký hiệu</Data></Cell><Cell ss:StyleID="Header"><Data ss:Type="String">Khoản mục chi phí xây dựng</Data></Cell><Cell ss:StyleID="Header"><Data ss:Type="String">Giá trị (VNĐ)</Data></Cell></Row>
   <Row><Cell><Data ss:Type="String">VL</Data></Cell><Cell><Data ss:Type="String">Chi phí vật liệu</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.b38.VL}</Data></Cell></Row>
   <Row><Cell><Data ss:Type="String">NC</Data></Cell><Cell><Data ss:Type="String">Chi phí nhân công</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.b38.NC}</Data></Cell></Row>
   <Row><Cell><Data ss:Type="String">M</Data></Cell><Cell><Data ss:Type="String">Chi phí máy thi công</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.b38.M}</Data></Cell></Row>
   <Row><Cell ss:StyleID="Bold"><Data ss:Type="String">T</Data></Cell><Cell ss:StyleID="Bold"><Data ss:Type="String">Chi phí trực tiếp (T = VL + NC + M)</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.b38.T}</Data></Cell></Row>
   <Row><Cell><Data ss:Type="String">C</Data></Cell><Cell><Data ss:Type="String">Chi phí chung (${c.b38.rate_cpc}%)</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.b38.C}</Data></Cell></Row>
   <Row><Cell><Data ss:Type="String">TL</Data></Cell><Cell><Data ss:Type="String">Thu nhập chịu thuế tính trước (${c.b38.rate_tl}%)</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.b38.TL}</Data></Cell></Row>
   <Row><Cell><Data ss:Type="String">TT</Data></Cell><Cell><Data ss:Type="String">Chi phí CV không xác định khối lượng từ TK (${c.b38.rate_tt}%)</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.b38.TT}</Data></Cell></Row>
   <Row><Cell ss:StyleID="Bold"><Data ss:Type="String">G_XDTT</Data></Cell><Cell ss:StyleID="Bold"><Data ss:Type="String">Chi phí xây dựng trước thuế (chưa gồm nhà tạm)</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.b38.G_XDTT}</Data></Cell></Row>
   <Row><Cell><Data ss:Type="String">GTGT</Data></Cell><Cell><Data ss:Type="String">Thuế GTGT xây dựng (${c.b38.vat_pct}%)</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.b38.GTGT_XD}</Data></Cell></Row>
   <Row><Cell><Data ss:Type="String">LT</Data></Cell><Cell><Data ss:Type="String">Chi phí nhà tạm sau thuế theo QĐ 1538/QĐ-BXD (${c.b38.rate_lt}%)</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.b38.LT_SAU_THUE}</Data></Cell></Row>
   <Row><Cell ss:StyleID="Bold"><Data ss:Type="String">G_XD</Data></Cell><Cell ss:StyleID="Bold"><Data ss:Type="String">TỔNG CHI PHÍ XÂY DỰNG SAU THUẾ</Data></Cell><Cell ss:StyleID="Num"><Data ss:Type="Number">${c.b38.G_XD_TOTAL_AFTER}</Data></Cell></Row>
  </Table>
 </Worksheet>
 <Worksheet ss:Name="03_TIEN_LUONG_BOQ">
  <Table>
   <Row>
    <Cell ss:StyleID="Header"><Data ss:Type="String">STT</Data></Cell>
    <Cell ss:StyleID="Header"><Data ss:Type="String">Mã ĐM TT38</Data></Cell>
    <Cell ss:StyleID="Header"><Data ss:Type="String">Tên công tác xây dựng</Data></Cell>
    <Cell ss:StyleID="Header"><Data ss:Type="String">ĐVT</Data></Cell>
    <Cell ss:StyleID="Header"><Data ss:Type="String">Khối lượng</Data></Cell>
    <Cell ss:StyleID="Header"><Data ss:Type="String">ĐG Vật liệu</Data></Cell>
    <Cell ss:StyleID="Header"><Data ss:Type="String">ĐG Nhân công</Data></Cell>
    <Cell ss:StyleID="Header"><Data ss:Type="String">ĐG Máy</Data></Cell>
    <Cell ss:StyleID="Header"><Data ss:Type="String">Thành tiền TT (VNĐ)</Data></Cell>
   </Row>
   ${c.detailed_boq.map(r => `<Row>
    <Cell><Data ss:Type="Number">${r.stt}</Data></Cell>
    <Cell><Data ss:Type="String">${esc(r.norm_code)}</Data></Cell>
    <Cell><Data ss:Type="String">${esc(r.name)}</Data></Cell>
    <Cell><Data ss:Type="String">${esc(r.unit)}</Data></Cell>
    <Cell><Data ss:Type="Number">${r.quantity}</Data></Cell>
    <Cell ss:StyleID="Num"><Data ss:Type="Number">${r.unit_vl}</Data></Cell>
    <Cell ss:StyleID="Num"><Data ss:Type="Number">${r.unit_nc}</Data></Cell>
    <Cell ss:StyleID="Num"><Data ss:Type="Number">${r.unit_m}</Data></Cell>
    <Cell ss:StyleID="Num"><Data ss:Type="Number">${r.total_direct}</Data></Cell>
   </Row>`).join("")}
  </Table>
 </Worksheet>
</Workbook>`;

  const blob = new Blob([xml], { type: "application/vnd.ms-excel" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "Du_Toan_Xay_Dung_2026.xls";
  a.click();
}

window.addEventListener("DOMContentLoaded", () => {
  const sel = document.getElementById("addNormSelect");
  if (sel) {
    sel.innerHTML = state.norms.map(n => `<option value="${n.code}">${n.code} — ${n.name} (${n.unit})</option>`).join("");
  }
  loadPreset("dan_dung_tru_so");
});
"""

app_js_content = (
    "// TỰ ĐỘNG SINH BỞI build_web_bundle.py - DỮ LIỆU PHÁP LÝ 2026\n"
    f"const EMBEDDED_REGULATIONS = {json.dumps(regulations, ensure_ascii=False)};\n"
    f"const EMBEDDED_PRICES = {json.dumps(prices, ensure_ascii=False)};\n"
    f"const EMBEDDED_NORMS = {json.dumps(norms, ensure_ascii=False)};\n"
    f"const EMBEDDED_PRESETS = {json.dumps(presets, ensure_ascii=False)};\n"
    + JS_LOGIC
)

(ROOT / "app.js").write_text(app_js_content, encoding="utf-8")
print("Wrote", ROOT / "app.js")

# Build self-contained HTML artifact
index_html = (ROOT / "index.html").read_text(encoding="utf-8")
styles_css = (ROOT / "styles.css").read_text(encoding="utf-8")

self_contained = index_html.replace(
    '<link rel="stylesheet" href="styles.css" />',
    f"<style>\n{styles_css}\n</style>"
).replace(
    '<script src="app.js"></script>',
    f"<script>\n{app_js_content}\n</script>"
)

ARTIFACT_HTML.write_text(self_contained, encoding="utf-8")
print("Wrote self-contained HTML artifact:", ARTIFACT_HTML)
