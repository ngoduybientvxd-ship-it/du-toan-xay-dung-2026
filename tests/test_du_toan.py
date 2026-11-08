#!/usr/bin/env python3
"""
Bộ kiểm thử tự động (Unit Tests) cho Hệ thống Dự toán Xây dựng Công trình Nguồn vốn Nhà nước 2026
Kiểm tra:
1. Tra cứu cận trên (≤) theo Bảng 3.3 và Bảng 3.7 Phụ lục III Thông tư 36/2026/TT-BXD
2. Công thức đính chính chi phí nhà tạm theo Quyết định 1538/QĐ-BXD ngày 28/08/2026
3. Nội suy tuyến tính định mức tỷ lệ % theo Phụ lục VIII Thông tư 38/2026/TT-BXD
4. Toàn bộ chuỗi tính toán Dự toán công trình Dân dụng và Công nghiệp
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from du_toan_engine import (
    calculate_machine_shift_price_tt37,
    calculate_material_transport_cost,
    calculate_project_estimate,
    interpolate_rate_tt38,
    load_all_data,
    step_lookup_le,
)


class TestDuToan2026Engine(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = load_all_data()

    def test_step_lookup_bang_3_3_tt36(self):
        """Kiểm tra tra cứu Chi phí chung Bảng 3.3 (cột có dấu ≤ không nội suy)."""
        b33 = self.data["regulations"]["tt36_phu_luc_3"]["bang_3_3_cpc_du_toan"]
        thresholds = b33["thresholds_ty_dong"]
        dan_dung_rates = b33["rates"]["dan_dung"]

        # Công trình <= 40 tỷ -> 7.3%
        res_15 = step_lookup_le(15.0, thresholds, dan_dung_rates, b33["labels"])
        self.assertAlmostEqual(res_15["rate"], 7.3)
        self.assertEqual(res_15["matched_label"], "≤ 40")

        # Công trình 45 tỷ (nằm giữa 40 và 60 tỷ) -> lấy tại cột ≤ 60 tỷ là 7.1%
        res_45 = step_lookup_le(45.0, thresholds, dan_dung_rates, b33["labels"])
        self.assertAlmostEqual(res_45["rate"], 7.1)
        self.assertEqual(res_45["matched_label"], "≤ 60")

        # Công trình 1200 tỷ (> 1000 tỷ) -> 5.8%
        res_1200 = step_lookup_le(1200.0, thresholds, dan_dung_rates, b33["labels"])
        self.assertAlmostEqual(res_1200["rate"], 5.8)

    def test_linear_interpolation_tt38_pl8(self):
        """Kiểm tra công thức nội suy tuyến tính N_t = N_b - ((N_b - N_a)/(G_a - G_b))*(G_t - G_b)."""
        b11 = self.data["regulations"]["tt38_phu_luc_8"]["bang_1_1_qlda"]
        thresholds = b11["thresholds_ty_dong"]
        rates = b11["rates"]["dan_dung"]

        # Tại đúng mốc 10 tỷ -> 3.446%
        r10 = interpolate_rate_tt38(10.0, thresholds, rates)
        self.assertAlmostEqual(r10["rate"], 3.446, places=4)

        # Tại điểm giữa 15 tỷ (giữa 10 tỷ = 3.446% và 20 tỷ = 2.923%) -> trung bình cộng = 3.1845%
        r15 = interpolate_rate_tt38(15.0, thresholds, rates)
        self.assertAlmostEqual(r15["rate"], 3.1845, places=4)

    def test_preset_dan_dung_tru_so(self):
        """Kiểm tra dự toán mẫu Công trình Dân dụng (Trụ sở làm việc 3 tầng)."""
        preset = self.data["presets"]["presets"]["dan_dung_tru_so"]
        result = calculate_project_estimate(
            preset["project_info"],
            preset["boq_items"],
            preset["equipment_items"],
            self.data["prices"],
            self.data["norms"],
            self.data["regulations"],
        )
        b38 = result["bang_3_8_summary"]
        tot = result["total_summary"]

        # Kiểm tra 27 công tác tiên lượng
        self.assertEqual(len(result["detailed_boq"]), 27)
        self.assertGreater(b38["VL"], 0)
        self.assertGreater(b38["NC"], 0)
        self.assertGreater(b38["M"], 0)
        self.assertEqual(b38["T"], b38["VL"] + b38["NC"] + b38["M"])

        # Tỷ lệ CPC Dân dụng BCKTKT = 7.3%, TL = 5.5%, TT = 2.5%, Nhà tạm = 1.1%
        self.assertAlmostEqual(b38["rate_cpc"], 7.3)
        self.assertAlmostEqual(b38["rate_tl"], 5.5)
        self.assertAlmostEqual(b38["rate_tt_other"], 2.5)
        self.assertAlmostEqual(b38["rate_lt"], 1.1)

        # Kiểm tra công thức nhà tạm theo QĐ 1538/QĐ-BXD: LT_sau_thue = LT_truoc_thue + LT_GTGT
        self.assertEqual(b38["LT_truoc_thue"], round(b38["G_XDTT"] * 0.011, 0))
        self.assertEqual(b38["LT_sau_thue"], b38["LT_truoc_thue"] + b38["LT_GTGT"])

        # Kiểm tra tổng dự toán công trình > G_XD + G_TB
        self.assertGreater(tot["TOTAL_DTXD"]["after_tax"], tot["G_XD"]["after_tax"] + tot["G_TB"]["after_tax"])

    def test_preset_cong_nghiep_nha_xuong(self):
        """Kiểm tra dự toán mẫu Công trình Công nghiệp (Nhà xưởng sản xuất khung thép tiền chế)."""
        preset = self.data["presets"]["presets"]["cong_nghiep_nha_xuong"]
        result = calculate_project_estimate(
            preset["project_info"],
            preset["boq_items"],
            preset["equipment_items"],
            self.data["prices"],
            self.data["norms"],
            self.data["regulations"],
        )
        b38 = result["bang_3_8_summary"]
        # Công trình công nghiệp quy mô <= 40 tỷ -> CPC = 6.2%, TL = 6.0%, TT = 2.0%
        self.assertAlmostEqual(b38["rate_cpc"], 6.2)
        self.assertAlmostEqual(b38["rate_tl"], 6.0)
        self.assertAlmostEqual(b38["rate_tt_other"], 2.0)

    def test_g8_machine_shift_tt37_and_transport(self):
        """Kiểm tra tính Giá ca máy (TT 37/2026/TT-BXD) và Cước vận chuyển (Cước VC) theo chuẩn Dự toán G8."""
        m001 = next(m for m in self.data["prices"]["may_thi_cong"] if m["id"] == "M001")
        nc_map = {n["id"]: n["price"] for n in self.data["prices"]["nhan_cong"]}
        fuel_prices = {
            "diesel_price_vnd_liter": 18500,
            "electricity_price_vnd_kwh": 2160,
            "gasoline_price_vnd_liter": 19800,
        }
        m_calc = calculate_machine_shift_price_tt37(m001, fuel_prices, nc_map)
        self.assertGreater(m_calc["c_kh"], 0)
        self.assertGreater(m_calc["c_nl"], 0)
        self.assertGreater(m_calc["c_nc"], 0)
        self.assertEqual(
            m_calc["calculated_shift_price"],
            m_calc["c_kh"] + m_calc["c_sc"] + m_calc["c_k"] + m_calc["c_nl"] + m_calc["c_nc"],
        )

        # Kiểm tra cước vận chuyển cát xây dựng VL004
        vl004 = next(v for v in self.data["prices"]["vat_lieu"] if v["id"] == "VL004")
        road_rates = {"loai_1": 2400, "loai_2": 3200, "loai_3": 4200}
        t_calc = calculate_material_transport_cost(vl004, road_rates)
        self.assertGreater(t_calc["transport_cost"], 0)
        self.assertEqual(t_calc["site_price"], t_calc["base_price"] + t_calc["transport_cost"])

    def test_g8_cv12637_toggle(self):
        """Kiểm tra tùy chọn 'Có nhà tạm' khi tính G_QLDA và G_TV theo Công văn 12637/BXD-KTQLXD (G8 20/08/2026)."""
        preset = self.data["presets"]["presets"]["dan_dung_tru_so"]
        info_with_lt = dict(preset["project_info"], include_lt_in_qlda_tv=True)
        info_no_lt = dict(preset["project_info"], include_lt_in_qlda_tv=False)

        res_with_lt = calculate_project_estimate(
            info_with_lt,
            preset["boq_items"],
            preset["equipment_items"],
            self.data["prices"],
            self.data["norms"],
            self.data["regulations"],
        )
        res_no_lt = calculate_project_estimate(
            info_no_lt,
            preset["boq_items"],
            preset["equipment_items"],
            self.data["prices"],
            self.data["norms"],
            self.data["regulations"],
        )
        self.assertGreater(
            res_with_lt["total_summary"]["G_QLDA"]["before_tax"],
            res_no_lt["total_summary"]["G_QLDA"]["before_tax"],
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)

