// TỰ ĐỘNG SINH BỞI build_web_bundle.py - DỮ LIỆU PHÁP LÝ 2026
const EMBEDDED_REGULATIONS = {"metadata": {"legal_basis": [{"code": "135/2025/QH15", "name": "Luật Xây dựng năm 2025", "issued_date": "10/12/2025", "effective_date": "01/01/2026", "role": "Quy định khung về tổng mức đầu tư, dự toán xây dựng, thẩm định, phê duyệt và quản lý chi phí đầu tư xây dựng."}, {"code": "206/2026/NĐ-CP", "name": "Nghị định 206/2026/NĐ-CP của Chính phủ", "issued_date": "15/06/2026", "effective_date": "01/07/2026", "role": "Quy định chi tiết về quản lý chi phí đầu tư xây dựng (thay thế Nghị định 10/2021/NĐ-CP)."}, {"code": "36/2026/TT-BXD", "name": "Thông tư 36/2026/TT-BXD của Bộ Xây dựng (hợp nhất tại 89/2026/VBHN-TT-BXD)", "issued_date": "26/06/2026", "effective_date": "01/07/2026", "role": "Hướng dẫn một số nội dung, phương pháp xác định và quản lý chi phí đầu tư xây dựng (thay thế Thông tư 11/2021/TT-BXD)."}, {"code": "1538/QĐ-BXD", "name": "Quyết định 1538/QĐ-BXD của Bộ Xây dựng", "issued_date": "28/08/2026", "effective_date": "28/08/2026", "role": "Đính chính Thông tư 36/2026/TT-BXD (đặc biệt đính chính công thức chi phí nhà tạm LT = G_XDTT × Tỷ lệ × (1 + T_GTGT) tại Bảng 3.8, 3.9 Phụ lục III và STT 1 Bảng 3.4 từ Bảo dưỡng thành Sửa chữa)."}, {"code": "37/2026/TT-BXD", "name": "Thông tư 37/2026/TT-BXD của Bộ Xây dựng", "issued_date": "26/06/2026", "effective_date": "01/07/2026", "role": "Hướng dẫn phương pháp xác định định mức dự toán và các chỉ tiêu kinh tế - kỹ thuật (giá nhân công, giá ca máy, chỉ số giá xây dựng)."}, {"code": "38/2026/TT-BXD", "name": "Thông tư 38/2026/TT-BXD của Bộ Xây dựng", "issued_date": "26/06/2026", "effective_date": "01/07/2026", "role": "Ban hành Định mức xây dựng (Phụ lục I-VII: Định mức dự toán; Phụ lục VIII: Định mức chi phí quản lý dự án và tư vấn đầu tư xây dựng)."}]}, "tt36_phu_luc_3": {"bang_3_2_cpc_tmdt": {"title": "Bảng 3.2: Định mức chi phí chung trong giai đoạn lập Tổng mức đầu tư (%)", "rates": {"dan_dung": 7.3, "dan_dung_di_tich": 11.6, "cong_nghiep": 6.2, "cong_nghiep_ham": 7.3, "giao_thong": 6.2, "giao_thong_ham": 7.3, "nong_nghiep": 6.1, "nong_nghiep_ham": 7.3, "ha_tang_ky_thuat": 5.5}}, "bang_3_3_cpc_du_toan": {"title": "Bảng 3.3: Định mức chi phí chung tính trên chi phí trực tiếp trong giai đoạn lập dự toán xây dựng (%)", "note": "Tra theo Chi phí xây dựng trước thuế trong TMĐT được duyệt (tỷ đồng). Các mốc có dấu ≤ nên tra theo cận trên (không nội suy). Riêng dự án lập Báo cáo KT-KT lấy tại cột mốc ≤ 40 tỷ đồng.", "thresholds_ty_dong": [40, 60, 100, 300, 500, 750, 1000, 999999], "labels": ["≤ 40", "≤ 60", "≤ 100", "≤ 300", "≤ 500", "≤ 750", "≤ 1.000", "> 1.000"], "rates": {"dan_dung": [7.3, 7.1, 6.7, 6.5, 6.2, 6.1, 6.0, 5.8], "dan_dung_di_tich": [11.6, 11.1, 10.3, 10.1, 9.9, 9.8, 9.6, 9.4], "cong_nghiep": [6.2, 6.0, 5.6, 5.3, 5.1, 5.0, 4.9, 4.6], "cong_nghiep_ham": [7.3, 7.2, 7.1, 6.9, 6.7, 6.6, 6.5, 6.4], "giao_thong": [6.2, 6.0, 5.6, 5.3, 5.1, 5.0, 4.9, 4.6], "giao_thong_ham": [7.3, 7.2, 7.1, 6.9, 6.7, 6.6, 6.5, 6.4], "nong_nghiep": [6.1, 5.9, 5.5, 5.3, 5.1, 5.0, 4.8, 4.6], "nong_nghiep_ham": [7.3, 7.2, 7.1, 6.9, 6.7, 6.6, 6.5, 6.4], "ha_tang_ky_thuat": [5.5, 5.3, 5.0, 4.8, 4.5, 4.4, 4.3, 4.0]}}, "bang_3_4_cpc_nhan_cong": {"title": "Bảng 3.4: Định mức chi phí chung tính trên chi phí nhân công (%) - Đã đính chính theo QĐ 1538/QĐ-BXD", "rates": {"sua_chua_nho_duoi_500tr": 66.0, "lap_dat_thiet_bi_cong_nghe": 65.0, "thi_nghiem_hieu_chinh_dien": 65.0, "xay_lap_duong_day_tram_bien_ap": 65.0}}, "bang_3_5_chi_phi_tt": {"title": "Bảng 3.5: Định mức chi phí một số công việc không xác định được khối lượng từ thiết kế (%)", "rates": {"dan_dung": 2.5, "dan_dung_di_tich": 2.5, "cong_nghiep": 2.0, "cong_nghiep_ham": 6.5, "giao_thong": 2.0, "giao_thong_ham": 6.5, "nong_nghiep": 2.0, "nong_nghiep_ham": 6.5, "ha_tang_ky_thuat": 2.0}}, "bang_3_6_thu_nhap_chiu_thue": {"title": "Bảng 3.6: Định mức thu nhập chịu thuế tính trước (%)", "rates": {"dan_dung": 5.5, "dan_dung_di_tich": 5.5, "cong_nghiep": 6.0, "cong_nghiep_ham": 6.0, "giao_thong": 6.0, "giao_thong_ham": 6.0, "nong_nghiep": 5.5, "nong_nghiep_ham": 5.5, "ha_tang_ky_thuat": 5.5, "lap_dat_thiet_bi_cong_nghe": 6.0}}, "bang_3_7_nha_tam": {"title": "Bảng 3.7: Định mức chi phí nhà tạm để ở và điều hành thi công (%)", "note": "Công thức đính chính theo QĐ 1538/QĐ-BXD: LT = G_XDTT × Tỷ lệ × (1 + T_GTGT). Các mốc có dấu ≤.", "thresholds_ty_dong": [15, 100, 500, 1000, 999999], "labels": ["≤ 15", "≤ 100", "≤ 500", "≤ 1.000", "> 1.000"], "rates": {"cong_trinh_con_lai": [1.1, 1.0, 0.95, 0.9, 0.85], "cong_trinh_theo_tuyen": [2.2, 2.0, 1.9, 1.8, 1.7]}}}, "tt38_phu_luc_8": {"bang_1_1_qlda": {"title": "Bảng 1.1: Định mức chi phí quản lý dự án (Phụ lục VIII - TT 38/2026/TT-BXD)", "unit": "% trên (G_XD + G_TB) trước thuế GTGT", "thresholds_ty_dong": [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 30000], "rates": {"dan_dung": [3.446, 2.923, 2.61, 2.017, 1.886, 1.514, 1.239, 0.958, 0.711, 0.51, 0.381, 0.305], "cong_nghiep": [3.557, 3.018, 2.694, 2.082, 1.947, 1.564, 1.279, 1.103, 0.734, 0.527, 0.393, 0.314], "giao_thong": [3.024, 2.566, 2.292, 1.771, 1.655, 1.329, 1.088, 0.937, 0.624, 0.448, 0.335, 0.268], "nong_nghiep": [3.263, 2.769, 2.473, 1.91, 1.786, 1.434, 1.174, 1.012, 0.674, 0.484, 0.361, 0.289], "ha_tang_ky_thuat": [2.901, 2.461, 2.198, 1.593, 1.56, 1.275, 1.071, 0.899, 0.599, 0.429, 0.321, 0.257]}}, "bang_2_3_bc_nckt": {"title": "Bảng 2.3: Định mức chi phí lập Báo cáo nghiên cứu khả thi (Phụ lục VIII - TT 38/2026/TT-BXD)", "unit": "% trên (G_XD + G_TB) trước thuế GTGT", "thresholds_ty_dong": [15, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 30000], "rates": {"dan_dung": [1.114, 0.914, 0.751, 0.534, 0.402, 0.287, 0.246, 0.209, 0.167, 0.134, 0.102, 0.086], "cong_nghiep": [1.261, 1.112, 0.882, 0.654, 0.515, 0.466, 0.404, 0.315, 0.248, 0.189, 0.135, 0.107], "giao_thong": [0.689, 0.628, 0.501, 0.393, 0.271, 0.203, 0.177, 0.151, 0.12, 0.097, 0.075, 0.063], "nong_nghiep": [0.943, 0.858, 0.685, 0.48, 0.361, 0.273, 0.234, 0.201, 0.161, 0.129, 0.1, 0.084], "ha_tang_ky_thuat": [0.719, 0.654, 0.524, 0.407, 0.28, 0.211, 0.185, 0.158, 0.127, 0.101, 0.078, 0.065]}}, "bang_2_4_bc_ktkt": {"title": "Bảng 2.4: Định mức chi phí lập Báo cáo kinh tế - kỹ thuật (Phụ lục VIII - TT 38/2026/TT-BXD)", "unit": "% trên (G_XD + G_TB) trước thuế GTGT", "thresholds_ty_dong": [1, 3, 7, 15, 20, 40], "rates": {"dan_dung": [6.5, 4.7, 4.2, 3.6, 2.9, 2.4], "cong_nghiep": [6.7, 4.8, 4.3, 3.8, 3.2, 2.5], "giao_thong": [5.4, 3.6, 3.0, 2.9, 2.7, 2.1], "nong_nghiep": [6.2, 4.4, 3.9, 3.6, 3.1, 2.4], "ha_tang_ky_thuat": [5.8, 4.2, 3.4, 3.0, 2.8, 2.2]}}, "bang_2_7_tkkt_dan_dung": {"title": "Bảng 2.7: Định mức chi phí Thiết kế kỹ thuật công trình Dân dụng (có yêu cầu TKKT & TKBVTC)", "unit": "% trên G_XD trước thuế GTGT", "thresholds_ty_dong": [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 8000, 10000], "rates_by_grade": {"dac_biet": [3.22, 2.81, 2.36, 2.15, 1.96, 1.65, 1.36, 1.16, 0.89, 0.68, 0.61], "cap_1": [2.93, 2.55, 2.14, 1.94, 1.78, 1.5, 1.22, 1.05, 0.8, 0.61, 0.55], "cap_2": [2.67, 2.33, 1.96, 1.77, 1.62, 1.37, 1.11, 0.94, 0.73, 0.55, 0.5], "cap_3": [2.36, 2.07, 1.74, 1.57, 1.43, 1.21, 0.98, 0.83, 0.64, 0.48, 0.44], "cap_4": [2.07, 1.81, 1.48, 1.3, 1.06, 0.89, 0.89, 0.89, 0.89, 0.89, 0.89]}}, "bang_2_8_tkbvtc_dan_dung": {"title": "Bảng 2.8: Định mức chi phí Thiết kế bản vẽ thi công công trình Dân dụng (không yêu cầu TKKT)", "unit": "% trên G_XD trước thuế GTGT", "thresholds_ty_dong": [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 8000, 10000], "rates_by_grade": {"dac_biet": [4.66, 4.05, 3.41, 3.1, 2.83, 2.39, 1.93, 1.65, 1.28, 0.99, 0.91], "cap_1": [4.22, 3.66, 3.1, 2.82, 2.57, 2.17, 1.76, 1.51, 1.16, 0.9, 0.8], "cap_2": [3.85, 3.33, 2.8, 2.54, 2.34, 1.98, 1.61, 1.36, 1.06, 0.82, 0.72], "cap_3": [3.41, 2.95, 2.48, 2.25, 2.07, 1.75, 1.43, 1.2, 0.94, 0.72, 0.63], "cap_4": [2.92, 2.55, 2.12, 1.86, 1.51, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3]}}, "bang_2_9_tkkt_cong_nghiep": {"title": "Bảng 2.9: Định mức chi phí Thiết kế kỹ thuật công trình Công nghiệp (có yêu cầu TKKT & TKBVTC)", "unit": "% trên G_XD trước thuế GTGT", "thresholds_ty_dong": [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 8000, 10000], "rates_by_grade": {"dac_biet": [2.96, 2.73, 2.34, 2.13, 1.92, 1.76, 1.54, 1.3, 0.97, 0.79, 0.7], "cap_1": [2.47, 2.27, 1.93, 1.77, 1.6, 1.46, 1.28, 1.09, 0.8, 0.65, 0.58], "cap_2": [2.03, 1.86, 1.59, 1.46, 1.32, 1.2, 1.05, 0.9, 0.66, 0.53, 0.48], "cap_3": [1.78, 1.65, 1.4, 1.27, 1.17, 1.06, 0.93, 0.79, 0.58, 0.47, 0.42], "cap_4": [1.59, 1.47, 1.24, 1.14, 0.98, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83]}}, "bang_2_10_tkbvtc_cong_nghiep": {"title": "Bảng 2.10: Định mức chi phí Thiết kế bản vẽ thi công công trình Công nghiệp (không yêu cầu TKKT)", "unit": "% trên G_XD trước thuế GTGT", "thresholds_ty_dong": [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 8000, 10000], "rates_by_grade": {"dac_biet": [4.7, 4.27, 3.66, 3.32, 3.01, 2.75, 2.4, 2.03, 1.52, 1.21, 1.04], "cap_1": [3.87, 3.57, 3.02, 2.77, 2.5, 2.28, 2.01, 1.7, 1.26, 1.02, 0.88], "cap_2": [3.13, 2.9, 2.43, 2.24, 2.03, 1.9, 1.66, 1.42, 1.04, 0.82, 0.72], "cap_3": [2.78, 2.57, 2.16, 1.99, 1.79, 1.68, 1.47, 1.25, 0.91, 0.72, 0.64], "cap_4": [2.46, 2.25, 1.89, 1.72, 1.47, 1.22, 1.22, 1.22, 1.22, 1.22, 1.22]}}, "bang_2_18_tham_tra_bcnckt": {"title": "Bảng 2.18: Định mức chi phí thẩm tra Báo cáo nghiên cứu khả thi", "unit": "% trên (G_XD + G_TB) trước thuế GTGT", "thresholds_ty_dong": [15, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 30000], "rates": {"dan_dung": [0.204, 0.168, 0.138, 0.097, 0.07, 0.046, 0.041, 0.034, 0.026, 0.019, 0.015, 0.012], "cong_nghiep": [0.281, 0.238, 0.19, 0.141, 0.107, 0.08, 0.07, 0.056, 0.044, 0.029, 0.02, 0.015], "giao_thong": [0.153, 0.139, 0.112, 0.087, 0.058, 0.036, 0.032, 0.026, 0.02, 0.014, 0.01, 0.009], "nong_nghiep": [0.182, 0.167, 0.133, 0.094, 0.068, 0.044, 0.037, 0.032, 0.026, 0.017, 0.014, 0.01], "ha_tang_ky_thuat": [0.16, 0.145, 0.116, 0.092, 0.06, 0.037, 0.034, 0.029, 0.022, 0.015, 0.01, 0.009]}}, "bang_2_19_tham_tra_thiet_ke": {"title": "Bảng 2.19: Định mức chi phí thẩm tra thiết kế xây dựng", "unit": "% trên G_XD trước thuế GTGT", "thresholds_ty_dong": [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 8000, 10000], "rates": {"dan_dung": [0.258, 0.223, 0.172, 0.143, 0.108, 0.083, 0.068, 0.044, 0.033, 0.028, 0.026], "cong_nghiep": [0.29, 0.252, 0.192, 0.146, 0.113, 0.087, 0.066, 0.053, 0.038, 0.031, 0.028], "giao_thong": [0.17, 0.147, 0.113, 0.084, 0.073, 0.055, 0.042, 0.035, 0.024, 0.02, 0.017], "nong_nghiep": [0.189, 0.163, 0.125, 0.093, 0.073, 0.056, 0.043, 0.035, 0.026, 0.022, 0.019], "ha_tang_ky_thuat": [0.197, 0.172, 0.133, 0.099, 0.076, 0.059, 0.046, 0.04, 0.029, 0.024, 0.021]}}, "bang_2_20_tham_tra_du_toan": {"title": "Bảng 2.20: Định mức chi phí thẩm tra dự toán xây dựng", "unit": "% trên G_XD trước thuế GTGT", "thresholds_ty_dong": [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 8000, 10000], "rates": {"dan_dung": [0.25, 0.219, 0.166, 0.14, 0.105, 0.077, 0.064, 0.043, 0.032, 0.027, 0.025], "cong_nghiep": [0.282, 0.244, 0.185, 0.141, 0.108, 0.083, 0.062, 0.05, 0.034, 0.03, 0.027], "giao_thong": [0.166, 0.142, 0.106, 0.082, 0.069, 0.052, 0.041, 0.034, 0.021, 0.018, 0.016], "nong_nghiep": [0.183, 0.158, 0.119, 0.092, 0.07, 0.053, 0.04, 0.034, 0.024, 0.021, 0.018], "ha_tang_ky_thuat": [0.191, 0.166, 0.128, 0.095, 0.072, 0.056, 0.044, 0.037, 0.026, 0.022, 0.02]}}, "bang_2_22_hsmt_xay_dung": {"title": "Bảng 2.22: Định mức chi phí lập HSMT, đánh giá HSDT thi công xây dựng", "unit": "% trên G_XD trước thuế GTGT", "thresholds_ty_dong": [10, 20, 50, 100, 200, 500, 1000, 2000], "rates": {"dan_dung": [0.432, 0.346, 0.195, 0.127, 0.078, 0.057, 0.04, 0.032], "cong_nghiep": [0.549, 0.379, 0.211, 0.144, 0.096, 0.067, 0.052, 0.041], "giao_thong": [0.346, 0.237, 0.151, 0.09, 0.057, 0.043, 0.029, 0.023], "nong_nghiep": [0.361, 0.302, 0.166, 0.094, 0.066, 0.046, 0.031, 0.026], "ha_tang_ky_thuat": [0.388, 0.325, 0.172, 0.106, 0.069, 0.052, 0.038, 0.028]}}, "bang_2_23_hsmt_thiet_bi": {"title": "Bảng 2.23: Định mức chi phí lập HSMT, đánh giá HSDT mua sắm vật tư, thiết bị", "unit": "% trên G_TB trước thuế GTGT", "thresholds_ty_dong": [10, 20, 50, 100, 200, 500, 1000, 2000], "rates": {"dan_dung": [0.367, 0.346, 0.181, 0.113, 0.102, 0.081, 0.055, 0.043], "cong_nghiep": [0.549, 0.494, 0.28, 0.177, 0.152, 0.123, 0.084, 0.066], "giao_thong": [0.261, 0.23, 0.131, 0.084, 0.074, 0.056, 0.04, 0.032], "nong_nghiep": [0.281, 0.245, 0.14, 0.09, 0.078, 0.061, 0.05, 0.037], "ha_tang_ky_thuat": [0.302, 0.26, 0.156, 0.102, 0.087, 0.069, 0.054, 0.041]}}, "bang_2_24_giam_sat_tcxd": {"title": "Bảng 2.24: Định mức chi phí giám sát thi công xây dựng", "unit": "% trên G_XD trước thuế GTGT", "thresholds_ty_dong": [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 8000, 10000], "rates": {"dan_dung": [3.285, 2.853, 2.435, 1.845, 1.546, 1.188, 0.797, 0.694, 0.62, 0.53, 0.478], "cong_nghiep": [3.508, 3.137, 2.559, 2.074, 1.604, 1.301, 0.823, 0.716, 0.64, 0.55, 0.493], "giao_thong": [3.203, 2.7, 2.356, 1.714, 1.272, 1.003, 0.731, 0.636, 0.55, 0.48, 0.438], "nong_nghiep": [2.598, 2.292, 2.075, 1.545, 1.189, 0.95, 0.631, 0.55, 0.49, 0.42, 0.378], "ha_tang_ky_thuat": [2.566, 2.256, 1.984, 1.461, 1.142, 0.912, 0.584, 0.509, 0.452, 0.39, 0.35]}}, "bang_2_25_giam_sat_ldtb": {"title": "Bảng 2.25: Định mức chi phí giám sát lắp đặt thiết bị", "unit": "% trên G_TB trước thuế GTGT", "thresholds_ty_dong": [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 8000, 10000], "rates": {"dan_dung": [0.844, 0.715, 0.596, 0.394, 0.305, 0.261, 0.176, 0.153, 0.132, 0.112, 0.11], "cong_nghiep": [1.147, 1.005, 0.958, 0.811, 0.49, 0.422, 0.356, 0.309, 0.27, 0.23, 0.21], "giao_thong": [0.677, 0.58, 0.486, 0.32, 0.261, 0.217, 0.146, 0.127, 0.11, 0.092, 0.085], "nong_nghiep": [0.718, 0.585, 0.52, 0.344, 0.276, 0.232, 0.159, 0.138, 0.12, 0.098, 0.091], "ha_tang_ky_thuat": [0.803, 0.69, 0.575, 0.383, 0.3, 0.261, 0.173, 0.15, 0.126, 0.105, 0.095]}}}};
const EMBEDDED_PRICES = {"vat_lieu": [{"id": "VL001", "name": "Xi măng PCB40 (bao)", "unit": "kg", "price": 1750, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL002", "name": "Cát mịn xây trát (cát đen/cát mịn đạt TCVN)", "unit": "m3", "price": 245000, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL003", "name": "Cát vàng đổ bê tông (hạt trung - thô đạt TCVN)", "unit": "m3", "price": 395000, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL004", "name": "Đá dăm 1x2 đổ bê tông", "unit": "m3", "price": 360000, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL005", "name": "Đá dăm 4x6 lót móng", "unit": "m3", "price": 310000, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL006", "name": "Nước sạch thi công", "unit": "lít", "price": 12, "source": "Giá nước sạch địa phương 2026"}, {"id": "VL007", "name": "Gạch đặc đất sét nung hoặc gạch không nung 6x10.5x22cm", "unit": "viên", "price": 1450, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL008", "name": "Gạch ống 4 lỗ 8x8x18cm", "unit": "viên", "price": 1320, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL009", "name": "Thép tròn cuộn D<=10mm (CB240-T)", "unit": "kg", "price": 16200, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL010", "name": "Thép thanh vằn D12-D18mm (CB300-V / CB400-V)", "unit": "kg", "price": 16500, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL011", "name": "Thép thanh vằn D>18mm (CB400-V)", "unit": "kg", "price": 16650, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL012", "name": "Thép hình (U, I, V, L) kết cấu nhà xưởng", "unit": "kg", "price": 19800, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL013", "name": "Dây thép buộc 1mm", "unit": "kg", "price": 23000, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL014", "name": "Que hàn điện 4mm", "unit": "kg", "price": 32000, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL015", "name": "Ván khuôn thép định hình + cây chống thép", "unit": "kg", "price": 22500, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL016", "name": "Gỗ ván khuôn nhóm IV", "unit": "m3", "price": 5400000, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL017", "name": "Đinh các loại", "unit": "kg", "price": 25000, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL018", "name": "Bê tông thương phẩm M250 (C20/25) độ sụt 10-12cm", "unit": "m3", "price": 1280000, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL019", "name": "Bê tông thương phẩm M300 (C25/30) độ sụt 10-12cm", "unit": "m3", "price": 1365000, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL020", "name": "Gạch Ceramic / Granite lát nền 600x600mm chống trượt", "unit": "m2", "price": 235000, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL021", "name": "Gạch Ceramic ốp tường 300x600mm", "unit": "m2", "price": 195000, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL022", "name": "Xi măng trắng chà mạch", "unit": "kg", "price": 4500, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL023", "name": "Bột bả tường nội/ngoại thất cao cấp", "unit": "kg", "price": 11500, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL024", "name": "Sơn lót kháng kiềm", "unit": "kg", "price": 68000, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL025", "name": "Sơn phủ hoàn thiện 2 lớp", "unit": "kg", "price": 85000, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL026", "name": "Tôn lợp mái mạ màu sóng vuông dày 0.45mm", "unit": "m2", "price": 158000, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL027", "name": "Cửa nhôm hệ Xingfa kính an toàn 8.38mm đồng bộ phụ kiện", "unit": "m2", "price": 1850000, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL028", "name": "Tấm thạch cao khung xương chìm Vĩnh Tường tiêu chuẩn", "unit": "m2", "price": 165000, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL029", "name": "Ống nhựa uPVC D90 thoát nước (C2)", "unit": "m", "price": 64000, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL030", "name": "Ống nhựa PPR D32 cấp nước chịu nhiệt PN10", "unit": "m", "price": 42000, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL031", "name": "Dây cáp điện đồng CV 2x4.0mm2 luồn ống", "unit": "m", "price": 29500, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL032", "name": "Bộ đèn LED Panel 600x600mm 40W âm trần", "unit": "bộ", "price": 420000, "source": "CBG VLXD Sở XD Quý III/2026"}, {"id": "VL033", "name": "Cọc bê tông cốt thép预 ứng lực / vuông 250x250mm M300", "unit": "m", "price": 345000, "source": "CBG VLXD Sở XD Quý III/2026"}], "nhan_cong": [{"id": "NC001", "name": "Nhân công bậc 3,0/7 - Nhóm nhân công xây dựng (TT 37/2026/TT-BXD)", "unit": "công", "price": 295000, "source": "QĐ Công bố đơn giá NC 2026"}, {"id": "NC002", "name": "Nhân công bậc 3,5/7 - Nhóm nhân công xây dựng (TT 37/2026/TT-BXD)", "unit": "công", "price": 322000, "source": "QĐ Công bố đơn giá NC 2026"}, {"id": "NC003", "name": "Nhân công bậc 4,0/7 - Nhóm nhân công xây dựng & lắp đặt (TT 37/2026/TT-BXD)", "unit": "công", "price": 352000, "source": "QĐ Công bố đơn giá NC 2026"}], "may_thi_cong": [{"id": "M001", "name": "Máy đào một gầu bánh xích dung tích gầu 0,80 m3", "unit": "ca", "price": 3450000, "source": "Bảng giá ca máy TT 37/2026/TT-BXD"}, {"id": "M002", "name": "Máy ủi bánh xích công suất 110 CV", "unit": "ca", "price": 2890000, "source": "Bảng giá ca máy TT 37/2026/TT-BXD"}, {"id": "M003", "name": "Máy đầm đất cầm tay (đầm cóc) 70kg", "unit": "ca", "price": 465000, "source": "Bảng giá ca máy TT 37/2026/TT-BXD"}, {"id": "M004", "name": "Máy trộn bê tông 250 lít", "unit": "ca", "price": 430000, "source": "Bảng giá ca máy TT 37/2026/TT-BXD"}, {"id": "M005", "name": "Máy trộn vữa 150 lít", "unit": "ca", "price": 360000, "source": "Bảng giá ca máy TT 37/2026/TT-BXD"}, {"id": "M006", "name": "Máy đầm bê tông dùi 1,5 kW", "unit": "ca", "price": 325000, "source": "Bảng giá ca máy TT 37/2026/TT-BXD"}, {"id": "M007", "name": "Máy đầm bàn 1,0 kW", "unit": "ca", "price": 315000, "source": "Bảng giá ca máy TT 37/2026/TT-BXD"}, {"id": "M008", "name": "Máy bơm bê tông 50 m3/h", "unit": "ca", "price": 4250000, "source": "Bảng giá ca máy TT 37/2026/TT-BXD"}, {"id": "M009", "name": "Máy cắt uốn cốt thép 5 kW", "unit": "ca", "price": 440000, "source": "Bảng giá ca máy TT 37/2026/TT-BXD"}, {"id": "M010", "name": "Máy hàn điện 23 kW", "unit": "ca", "price": 620000, "source": "Bảng giá ca máy TT 37/2026/TT-BXD"}, {"id": "M011", "name": "Vận thăng lồng / Tời điện 0,8 tấn", "unit": "ca", "price": 690000, "source": "Bảng giá ca máy TT 37/2026/TT-BXD"}, {"id": "M012", "name": "Cần trục tháp sức nâng 25 tấn / Cần trục bánh lốp 16 tấn", "unit": "ca", "price": 4850000, "source": "Bảng giá ca máy TT 37/2026/TT-BXD"}, {"id": "M013", "name": "Máy ép cọc thủy lực 120 - 150 tấn", "unit": "ca", "price": 4600000, "source": "Bảng giá ca máy TT 37/2026/TT-BXD"}, {"id": "M014", "name": "Ô tô tự đổ 10 tấn vận chuyển đất/phế thải", "unit": "ca", "price": 2750000, "source": "Bảng giá ca máy TT 37/2026/TT-BXD"}]};
const EMBEDDED_NORMS = [{"code": "AB.11442", "category": "Công tác đất & chuẩn bị mặt bằng (Chương AB - PL II TT 38/2026)", "name": "Đào móng bằng thủ công, chiều rộng móng <= 3m, sâu <= 1m, đất cấp II", "unit": "m3", "vl": [], "nc": [{"id": "NC001", "qty": 0.61}], "m": []}, {"code": "AB.25112", "category": "Công tác đất & chuẩn bị mặt bằng (Chương AB - PL II TT 38/2026)", "name": "Đào móng công trình bằng máy đào 0,80m3, đất cấp II", "unit": "m3", "vl": [], "nc": [{"id": "NC001", "qty": 0.058}], "m": [{"id": "M001", "qty": 0.0041}, {"id": "M002", "qty": 0.0005}]}, {"code": "AB.41312", "category": "Công tác đất & chuẩn bị mặt bằng (Chương AB - PL II TT 38/2026)", "name": "Vận chuyển đất bằng ô tô tự đổ 10 tấn trong phạm vi <= 1000m, đất cấp II", "unit": "m3", "vl": [], "nc": [], "m": [{"id": "M014", "qty": 0.0112}]}, {"code": "AB.13113", "category": "Công tác đất & chuẩn bị mặt bằng (Chương AB - PL II TT 38/2026)", "name": "Đắp đất nền móng công trình bằng đầm cóc, độ chặt yêu cầu K=0,95", "unit": "m3", "vl": [], "nc": [{"id": "NC001", "qty": 0.21}], "m": [{"id": "M003", "qty": 0.038}]}, {"code": "AC.26111", "category": "Công tác đóng/ép cọc & gia cố nền móng (Chương AC - PL II TT 38/2026)", "name": "Ép trước cọc BTCT vuông 250x250mm chiều dài cọc > 4m bằng máy ép thủy lực, đất cấp II", "unit": "m", "vl": [{"id": "VL033", "qty": 1.01}, {"id": "VL014", "qty": 0.08}], "nc": [{"id": "NC002", "qty": 0.075}], "m": [{"id": "M013", "qty": 0.0085}, {"id": "M012", "qty": 0.0085}, {"id": "M010", "qty": 0.004}]}, {"code": "AF.11111", "category": "Công tác bê tông (Chương AF - PL II TT 38/2026)", "name": "Bê tông lót móng sản xuất qua máy trộn tại hiện trường, chiều rộng <= 250cm, đá 4x6, vữa BT M100", "unit": "m3", "vl": [{"id": "VL001", "qty": 225.0}, {"id": "VL003", "qty": 0.525}, {"id": "VL005", "qty": 0.893}, {"id": "VL006", "qty": 185.0}], "nc": [{"id": "NC001", "qty": 1.25}], "m": [{"id": "M004", "qty": 0.095}, {"id": "M007", "qty": 0.089}]}, {"code": "AF.31123", "category": "Công tác bê tông (Chương AF - PL II TT 38/2026)", "name": "Bê tông móng đổ bằng máy bơm bê tông, bê tông thương phẩm M250 (C20/25), chiều rộng móng <= 250cm", "unit": "m3", "vl": [{"id": "VL018", "qty": 1.015}, {"id": "VL006", "qty": 30.0}], "nc": [{"id": "NC002", "qty": 0.56}], "m": [{"id": "M008", "qty": 0.033}, {"id": "M006", "qty": 0.089}]}, {"code": "AF.32224", "category": "Công tác bê tông (Chương AF - PL II TT 38/2026)", "name": "Bê tông cột, tiết diện cột > 0,1m2, cao <= 28m, đổ bằng bơm BT thương phẩm M300 (C25/30)", "unit": "m3", "vl": [{"id": "VL019", "qty": 1.015}, {"id": "VL006", "qty": 45.0}], "nc": [{"id": "NC002", "qty": 1.38}], "m": [{"id": "M008", "qty": 0.042}, {"id": "M006", "qty": 0.18}]}, {"code": "AF.32314", "category": "Công tác bê tông (Chương AF - PL II TT 38/2026)", "name": "Bê tông xà dầm, giằng, sàn mái cao <= 28m, đổ bằng bơm BT thương phẩm M300 (C25/30)", "unit": "m3", "vl": [{"id": "VL019", "qty": 1.015}, {"id": "VL006", "qty": 45.0}], "nc": [{"id": "NC002", "qty": 1.12}], "m": [{"id": "M008", "qty": 0.038}, {"id": "M006", "qty": 0.14}, {"id": "M007", "qty": 0.07}]}, {"code": "AF.15113", "category": "Công tác bê tông (Chương AF - PL II TT 38/2026)", "name": "Bê tông nền nhà xưởng / nền tầng trệt sản xuất tại chỗ, đá 1x2, M250", "unit": "m3", "vl": [{"id": "VL001", "qty": 348.0}, {"id": "VL003", "qty": 0.468}, {"id": "VL004", "qty": 0.871}, {"id": "VL006", "qty": 185.0}], "nc": [{"id": "NC001", "qty": 1.32}], "m": [{"id": "M004", "qty": 0.095}, {"id": "M007", "qty": 0.089}]}, {"code": "AF.61110", "category": "Công tác cốt thép & ván khuôn (Chương AF - PL II TT 38/2026)", "name": "Gia công lắp dựng cốt thép móng, đường kính cốt thép <= 10mm", "unit": "tấn", "vl": [{"id": "VL009", "qty": 1005.0}, {"id": "VL013", "qty": 16.5}], "nc": [{"id": "NC002", "qty": 9.85}], "m": [{"id": "M009", "qty": 0.4}]}, {"code": "AF.61120", "category": "Công tác cốt thép & ván khuôn (Chương AF - PL II TT 38/2026)", "name": "Gia công lắp dựng cốt thép móng, đường kính cốt thép <= 18mm", "unit": "tấn", "vl": [{"id": "VL010", "qty": 1020.0}, {"id": "VL013", "qty": 14.2}], "nc": [{"id": "NC002", "qty": 7.12}], "m": [{"id": "M009", "qty": 0.32}, {"id": "M010", "qty": 0.55}]}, {"code": "AF.61422", "category": "Công tác cốt thép & ván khuôn (Chương AF - PL II TT 38/2026)", "name": "Gia công lắp dựng cốt thép cột, trụ, đường kính cốt thép <= 18mm, cao <= 28m", "unit": "tấn", "vl": [{"id": "VL010", "qty": 1020.0}, {"id": "VL013", "qty": 14.5}, {"id": "VL014", "qty": 2.3}], "nc": [{"id": "NC002", "qty": 9.2}], "m": [{"id": "M009", "qty": 0.32}, {"id": "M010", "qty": 1.15}, {"id": "M011", "qty": 0.28}]}, {"code": "AF.61432", "category": "Công tác cốt thép & ván khuôn (Chương AF - PL II TT 38/2026)", "name": "Gia công lắp dựng cốt thép cột, dầm, đường kính > 18mm, cao <= 28m", "unit": "tấn", "vl": [{"id": "VL011", "qty": 1020.0}, {"id": "VL013", "qty": 9.8}, {"id": "VL014", "qty": 4.6}], "nc": [{"id": "NC002", "qty": 6.85}], "m": [{"id": "M009", "qty": 0.25}, {"id": "M010", "qty": 1.5}, {"id": "M011", "qty": 0.28}]}, {"code": "AF.61522", "category": "Công tác cốt thép & ván khuôn (Chương AF - PL II TT 38/2026)", "name": "Gia công lắp dựng cốt thép xà dầm, giằng, sàn, đường kính <= 18mm, cao <= 28m", "unit": "tấn", "vl": [{"id": "VL010", "qty": 1020.0}, {"id": "VL013", "qty": 15.6}], "nc": [{"id": "NC002", "qty": 8.95}], "m": [{"id": "M009", "qty": 0.32}, {"id": "M010", "qty": 0.85}, {"id": "M011", "qty": 0.28}]}, {"code": "AF.81122", "category": "Công tác cốt thép & ván khuôn (Chương AF - PL II TT 38/2026)", "name": "Ván khuôn gỗ cho móng dài, bệ máy (tính cho 100m2 ván khuôn quy đổi về 1m2)", "unit": "m2", "vl": [{"id": "VL016", "qty": 0.0079}, {"id": "VL017", "qty": 0.15}], "nc": [{"id": "NC002", "qty": 0.245}], "m": []}, {"code": "AF.86312", "category": "Công tác cốt thép & ván khuôn (Chương AF - PL II TT 38/2026)", "name": "Ván khuôn thép định hình + hệ giáo chống cho cột, dầm, sàn chiều cao <= 28m", "unit": "m2", "vl": [{"id": "VL015", "qty": 1.35}, {"id": "VL014", "qty": 0.05}], "nc": [{"id": "NC002", "qty": 0.365}], "m": [{"id": "M011", "qty": 0.015}, {"id": "M010", "qty": 0.012}]}, {"code": "AE.22113", "category": "Công tác xây gạch đá (Chương AE - PL II TT 38/2026)", "name": "Xây tường thẳng bằng gạch đặc 6x10,5x22cm chiều dày <= 11cm, cao <= 28m, vữa XM M75", "unit": "m3", "vl": [{"id": "VL007", "qty": 643.0}, {"id": "VL001", "qty": 77.5}, {"id": "VL002", "qty": 0.28}, {"id": "VL006", "qty": 72.0}], "nc": [{"id": "NC002", "qty": 1.92}], "m": [{"id": "M005", "qty": 0.045}, {"id": "M011", "qty": 0.032}]}, {"code": "AE.22223", "category": "Công tác xây gạch đá (Chương AE - PL II TT 38/2026)", "name": "Xây tường thẳng bằng gạch đặc 6x10,5x22cm chiều dày <= 33cm (tường 220), cao <= 28m, vữa XM M75", "unit": "m3", "vl": [{"id": "VL007", "qty": 550.0}, {"id": "VL001", "qty": 90.3}, {"id": "VL002", "qty": 0.326}, {"id": "VL006", "qty": 84.0}], "nc": [{"id": "NC002", "qty": 1.68}], "m": [{"id": "M005", "qty": 0.052}, {"id": "M011", "qty": 0.032}]}, {"code": "AE.52213", "category": "Công tác xây gạch đá (Chương AE - PL II TT 38/2026)", "name": "Xây tường thẳng bằng gạch ống 8x8x18cm chiều dày <= 30cm, cao <= 28m, vữa XM M75", "unit": "m3", "vl": [{"id": "VL008", "qty": 475.0}, {"id": "VL001", "qty": 82.0}, {"id": "VL002", "qty": 0.295}, {"id": "VL006", "qty": 76.0}], "nc": [{"id": "NC002", "qty": 1.54}], "m": [{"id": "M005", "qty": 0.048}, {"id": "M011", "qty": 0.032}]}, {"code": "AI.11221", "category": "Công tác kết cấu thép nhà công nghiệp (Chương AI - PL II TT 38/2026)", "name": "Gia công và lắp dựng cột, vì kèo, xà gồ thép hình nhà xưởng công nghiệp", "unit": "tấn", "vl": [{"id": "VL012", "qty": 1030.0}, {"id": "VL014", "qty": 18.5}], "nc": [{"id": "NC003", "qty": 14.5}], "m": [{"id": "M012", "qty": 0.65}, {"id": "M010", "qty": 3.2}]}, {"code": "AK.21123", "category": "Công tác hoàn thiện: Trát, Láng, Ốp, Lát (Chương AK - PL II TT 38/2026)", "name": "Trát tường ngoài dày 1,5cm, vữa xi măng M75", "unit": "m2", "vl": [{"id": "VL001", "qty": 4.92}, {"id": "VL002", "qty": 0.018}, {"id": "VL006", "qty": 4.5}], "nc": [{"id": "NC002", "qty": 0.22}], "m": [{"id": "M005", "qty": 0.0032}]}, {"code": "AK.21223", "category": "Công tác hoàn thiện: Trát, Láng, Ốp, Lát (Chương AK - PL II TT 38/2026)", "name": "Trát tường trong dày 1,5cm, vữa xi măng M75", "unit": "m2", "vl": [{"id": "VL001", "qty": 4.65}, {"id": "VL002", "qty": 0.017}, {"id": "VL006", "qty": 4.2}], "nc": [{"id": "NC002", "qty": 0.18}], "m": [{"id": "M005", "qty": 0.003}]}, {"code": "AK.23113", "category": "Công tác hoàn thiện: Trát, Láng, Ốp, Lát (Chương AK - PL II TT 38/2026)", "name": "Trát trần, dầm dày 1,0cm - 1,5cm, vữa xi măng M75", "unit": "m2", "vl": [{"id": "VL001", "qty": 4.15}, {"id": "VL002", "qty": 0.015}, {"id": "VL006", "qty": 4.0}], "nc": [{"id": "NC002", "qty": 0.25}], "m": [{"id": "M005", "qty": 0.0028}]}, {"code": "AK.51240", "category": "Công tác hoàn thiện: Trát, Láng, Ốp, Lát (Chương AK - PL II TT 38/2026)", "name": "Lát nền, sàn bằng gạch Ceramic / Granite 600x600mm, vữa lót XM M75", "unit": "m2", "vl": [{"id": "VL020", "qty": 1.02}, {"id": "VL001", "qty": 6.15}, {"id": "VL002", "qty": 0.025}, {"id": "VL022", "qty": 0.15}], "nc": [{"id": "NC002", "qty": 0.21}], "m": [{"id": "M005", "qty": 0.004}]}, {"code": "AK.31130", "category": "Công tác hoàn thiện: Trát, Láng, Ốp, Lát (Chương AK - PL II TT 38/2026)", "name": "Ốp tường khu vệ sinh bằng gạch Ceramic 300x600mm", "unit": "m2", "vl": [{"id": "VL021", "qty": 1.03}, {"id": "VL001", "qty": 5.2}, {"id": "VL002", "qty": 0.018}, {"id": "VL022", "qty": 0.18}], "nc": [{"id": "NC002", "qty": 0.34}], "m": [{"id": "M005", "qty": 0.003}]}, {"code": "AK.82410", "category": "Công tác Sơn bả, Trần, Cửa, Mái (Chương AK, AL - PL II TT 38/2026)", "name": "Bả bằng bột bả vào tường, cột, dầm trần", "unit": "m2", "vl": [{"id": "VL023", "qty": 1.15}], "nc": [{"id": "NC002", "qty": 0.085}], "m": []}, {"code": "AK.84113", "category": "Công tác Sơn bả, Trần, Cửa, Mái (Chương AK, AL - PL II TT 38/2026)", "name": "Sơn dầm, trần, tường trong và ngoài nhà đã bả: 1 nước lót + 2 nước phủ", "unit": "m2", "vl": [{"id": "VL024", "qty": 0.11}, {"id": "VL025", "qty": 0.18}], "nc": [{"id": "NC002", "qty": 0.092}], "m": []}, {"code": "AK.62120", "category": "Công tác Sơn bả, Trần, Cửa, Mái (Chương AK, AL - PL II TT 38/2026)", "name": "Làm trần thạch cao khung xương chìm phẳng hoàn chỉnh", "unit": "m2", "vl": [{"id": "VL028", "qty": 1.03}], "nc": [{"id": "NC002", "qty": 0.24}], "m": []}, {"code": "AL.16111", "category": "Công tác Sơn bả, Trần, Cửa, Mái (Chương AK, AL - PL II TT 38/2026)", "name": "Lợp mái tôn múi mạ màu dày 0,45mm trên hệ xà gồ", "unit": "m2", "vl": [{"id": "VL026", "qty": 1.08}], "nc": [{"id": "NC002", "qty": 0.11}], "m": []}, {"code": "AL.63110", "category": "Công tác Sơn bả, Trần, Cửa, Mái (Chương AK, AL - PL II TT 38/2026)", "name": "Lắp dựng cửa đi, cửa sổ khung nhôm hệ Xingfa kính an toàn 8,38mm đồng bộ phụ kiện", "unit": "m2", "vl": [{"id": "VL027", "qty": 1.0}], "nc": [{"id": "NC003", "qty": 0.28}], "m": []}, {"code": "BB.19214", "category": "Công tác Lắp đặt Điện & Cấp thoát nước MEP (PL III TT 38/2026)", "name": "Lắp đặt ống nhựa uPVC D90 thoát nước nối bằng phương pháp dán keo", "unit": "m", "vl": [{"id": "VL029", "qty": 1.02}], "nc": [{"id": "NC003", "qty": 0.085}], "m": []}, {"code": "BB.19305", "category": "Công tác Lắp đặt Điện & Cấp thoát nước MEP (PL III TT 38/2026)", "name": "Lắp đặt ống nhựa PPR D32 cấp nước nối bằng phương pháp hàn nhiệt", "unit": "m", "vl": [{"id": "VL030", "qty": 1.02}], "nc": [{"id": "NC003", "qty": 0.072}], "m": []}, {"code": "BA.16204", "category": "Công tác Lắp đặt Điện & Cấp thoát nước MEP (PL III TT 38/2026)", "name": "Kéo rải dây điện đôi CV 2x4,0mm2 luồn trong ống bảo vệ", "unit": "m", "vl": [{"id": "VL031", "qty": 1.02}], "nc": [{"id": "NC003", "qty": 0.038}], "m": []}, {"code": "BA.12302", "category": "Công tác Lắp đặt Điện & Cấp thoát nước MEP (PL III TT 38/2026)", "name": "Lắp đặt bộ đèn LED Panel 600x600mm âm trần", "unit": "bộ", "vl": [{"id": "VL032", "qty": 1.0}], "nc": [{"id": "NC003", "qty": 0.22}], "m": []}];
const EMBEDDED_PRESETS = {"presets": {"dan_dung_tru_so": {"project_info": {"project_name": "Dự án Đầu tư Xây dựng Trụ sở Làm việc & Trung tâm Hành chính Công", "building_name": "Khối nhà làm việc chính 3 tầng + 1 tum (Diện tích sàn 1.850 m2)", "investor": "Ban Quản lý Dự án Đầu tư Xây dựng Công trình Dân dụng & Công nghiệp", "location": "Khu trung tâm hành chính - Vùng II", "funding_source": "Vốn đầu tư công (Ngân sách Nhà nước)", "building_type": "dan_dung", "building_grade": "cap_3", "design_step": "tkbvtc_2_buoc", "is_bcktkt": true, "is_mountain_island": false, "vat_rate": 8.0, "k_nc": 1.0, "k_m": 1.0, "contingency_volume_rate": 5.0, "contingency_escalation_rate": 2.5, "tmdt_gxdtt_approved_ty": 15.0}, "boq_items": [{"id": 1, "section": "I. PHẦN MÓNG & CÔNG TÁC NGẦM", "norm_code": "AB.25112", "custom_name": "Đào móng công trình bằng máy đào 0,80m3, đất cấp II", "formula": "12 * 4.2 * 3.8 * 1.8", "count": 12, "length": 4.2, "width": 3.8, "height": 1.8, "factor": 1.0, "quantity": 344.736}, {"id": 2, "section": "I. PHẦN MÓNG & CÔNG TÁC NGẦM", "norm_code": "AB.11442", "custom_name": "Đào sửa hố móng bằng thủ công, đất cấp II", "formula": "12 * 4.2 * 3.8 * 0.2", "count": 12, "length": 4.2, "width": 3.8, "height": 0.2, "factor": 1.0, "quantity": 38.304}, {"id": 3, "section": "I. PHẦN MÓNG & CÔNG TÁC NGẦM", "norm_code": "AC.26111", "custom_name": "Ép cọc BTCT vuông 250x250mm M300 bằng máy ép thủy lực", "formula": "48 * 15.0", "count": 48, "length": 15.0, "width": 1.0, "height": 1.0, "factor": 1.0, "quantity": 720.0}, {"id": 4, "section": "I. PHẦN MÓNG & CÔNG TÁC NGẦM", "norm_code": "AF.11111", "custom_name": "Bê tông lót móng đá 4x6 M100 dày 10cm", "formula": "12 * 2.6 * 2.4 * 0.1 + 65 * 0.6 * 0.1", "count": 1, "length": 11.388, "width": 1.0, "height": 1.0, "factor": 1.0, "quantity": 11.388}, {"id": 5, "section": "I. PHẦN MÓNG & CÔNG TÁC NGẦM", "norm_code": "AF.31123", "custom_name": "Bê tông đài móng & giằng móng thương phẩm M250 đổ bằng máy bơm", "formula": "12 * 2.4 * 2.2 * 0.9 + 65 * 0.4 * 0.7", "count": 1, "length": 75.224, "width": 1.0, "height": 1.0, "factor": 1.0, "quantity": 75.224}, {"id": 6, "section": "I. PHẦN MÓNG & CÔNG TÁC NGẦM", "norm_code": "AF.61120", "custom_name": "Cốt thép đài móng, giằng móng đường kính <= 18mm", "formula": "75.224 * 0.115", "count": 1, "length": 8.65, "width": 1.0, "height": 1.0, "factor": 1.0, "quantity": 8.65}, {"id": 7, "section": "I. PHẦN MÓNG & CÔNG TÁC NGẦM", "norm_code": "AF.81122", "custom_name": "Ván khuôn móng và giằng móng", "formula": "12 * (2.4+2.2)*2 * 0.9 + 65 * 2 * 0.7", "count": 1, "length": 190.36, "width": 1.0, "height": 1.0, "factor": 1.0, "quantity": 190.36}, {"id": 8, "section": "I. PHẦN MÓNG & CÔNG TÁC NGẦM", "norm_code": "AB.13113", "custom_name": "Đắp đất hố móng và tôn nền bằng đầm cóc K=0,95", "formula": "285.0", "count": 1, "length": 285.0, "width": 1.0, "height": 1.0, "factor": 1.0, "quantity": 285.0}, {"id": 9, "section": "II. PHẦN THÂN & KẾT CẤU BTCT", "norm_code": "AF.32224", "custom_name": "Bê tông cột tầng 1 - tầng 3 thương phẩm M300 đổ bằng bơm", "formula": "36 * 0.4 * 0.4 * 11.4", "count": 36, "length": 0.4, "width": 0.4, "height": 11.4, "factor": 1.0, "quantity": 65.664}, {"id": 10, "section": "II. PHẦN THÂN & KẾT CẤU BTCT", "norm_code": "AF.32314", "custom_name": "Bê tông dầm, sàn các tầng và sàn mái thương phẩm M300 đổ bằng bơm", "formula": "3 * 615 * 0.14", "count": 3, "length": 615.0, "width": 1.0, "height": 0.14, "factor": 1.0, "quantity": 258.3}, {"id": 11, "section": "II. PHẦN THÂN & KẾT CẤU BTCT", "norm_code": "AF.61432", "custom_name": "Cốt thép chủ cột, dầm chính đường kính > 18mm", "formula": "28.5", "count": 1, "length": 28.5, "width": 1.0, "height": 1.0, "factor": 1.0, "quantity": 28.5}, {"id": 12, "section": "II. PHẦN THÂN & KẾT CẤU BTCT", "norm_code": "AF.61522", "custom_name": "Cốt thép dầm phụ, bản sàn các tầng đường kính <= 18mm", "formula": "26.4", "count": 1, "length": 26.4, "width": 1.0, "height": 1.0, "factor": 1.0, "quantity": 26.4}, {"id": 13, "section": "II. PHẦN THÂN & KẾT CẤU BTCT", "norm_code": "AF.86312", "custom_name": "Ván khuôn thép định hình + giáo chống cột, dầm, sàn các tầng", "formula": "2480.0", "count": 1, "length": 2480.0, "width": 1.0, "height": 1.0, "factor": 1.0, "quantity": 2480.0}, {"id": 14, "section": "II. PHẦN THÂN & KẾT CẤU BTCT", "norm_code": "AE.22223", "custom_name": "Xây tường bao che dày 220mm gạch đặc vữa XM M75", "formula": "215.0", "count": 1, "length": 215.0, "width": 1.0, "height": 1.0, "factor": 1.0, "quantity": 215.0}, {"id": 15, "section": "II. PHẦN THÂN & KẾT CẤU BTCT", "norm_code": "AE.22113", "custom_name": "Xây tường ngăn phòng dày 110mm gạch đặc vữa XM M75", "formula": "118.0", "count": 1, "length": 118.0, "width": 1.0, "height": 1.0, "factor": 1.0, "quantity": 118.0}, {"id": 16, "section": "III. PHẦN HOÀN THIỆN KIẾN TRÚC", "norm_code": "AK.21123", "custom_name": "Trát tường ngoài nhà dày 1,5cm vữa XM M75", "formula": "1650.0", "count": 1, "length": 1650.0, "width": 1.0, "height": 1.0, "factor": 1.0, "quantity": 1650.0}, {"id": 17, "section": "III. PHẦN HOÀN THIỆN KIẾN TRÚC", "norm_code": "AK.21223", "custom_name": "Trát tường trong nhà dày 1,5cm vữa XM M75", "formula": "3420.0", "count": 1, "length": 3420.0, "width": 1.0, "height": 1.0, "factor": 1.0, "quantity": 3420.0}, {"id": 18, "section": "III. PHẦN HOÀN THIỆN KIẾN TRÚC", "norm_code": "AK.51240", "custom_name": "Lát nền gạch Granite 600x600mm các tầng làm việc & sảnh", "formula": "1720.0", "count": 1, "length": 1720.0, "width": 1.0, "height": 1.0, "factor": 1.0, "quantity": 1720.0}, {"id": 19, "section": "III. PHẦN HOÀN THIỆN KIẾN TRÚC", "norm_code": "AK.31130", "custom_name": "Ốp tường khu vệ sinh gạch Ceramic 300x600mm", "formula": "280.0", "count": 1, "length": 280.0, "width": 1.0, "height": 1.0, "factor": 1.0, "quantity": 280.0}, {"id": 20, "section": "III. PHẦN HOÀN THIỆN KIẾN TRÚC", "norm_code": "AK.62120", "custom_name": "Trần thạch cao khung xương chìm phẳng các phòng làm việc", "formula": "1560.0", "count": 1, "length": 1560.0, "width": 1.0, "height": 1.0, "factor": 1.0, "quantity": 1560.0}, {"id": 21, "section": "III. PHẦN HOÀN THIỆN KIẾN TRÚC", "norm_code": "AK.82410", "custom_name": "Bả bột bả vào tường, cột trong và ngoài nhà", "formula": "5070.0", "count": 1, "length": 5070.0, "width": 1.0, "height": 1.0, "factor": 1.0, "quantity": 5070.0}, {"id": 22, "section": "III. PHẦN HOÀN THIỆN KIẾN TRÚC", "norm_code": "AK.84113", "custom_name": "Sơn tường, trần 1 lớp lót + 2 lớp phủ hoàn thiện", "formula": "6630.0", "count": 1, "length": 6630.0, "width": 1.0, "height": 1.0, "factor": 1.0, "quantity": 6630.0}, {"id": 23, "section": "III. PHẦN HOÀN THIỆN KIẾN TRÚC", "norm_code": "AL.63110", "custom_name": "Cửa đi, cửa sổ nhôm hệ Xingfa kính an toàn 8,38mm đồng bộ", "formula": "345.0", "count": 1, "length": 345.0, "width": 1.0, "height": 1.0, "factor": 1.0, "quantity": 345.0}, {"id": 24, "section": "IV. HỆ THỐNG ĐIỆN & CẤP THOÁT NƯỚC (MEP)", "norm_code": "BB.19214", "custom_name": "Lắp đặt ống nhựa uPVC D90 thoát nước trục đứng & nhánh", "formula": "260.0", "count": 1, "length": 260.0, "width": 1.0, "height": 1.0, "factor": 1.0, "quantity": 260.0}, {"id": 25, "section": "IV. HỆ THỐNG ĐIỆN & CẤP THOÁT NƯỚC (MEP)", "norm_code": "BB.19305", "custom_name": "Lắp đặt ống nhựa PPR D32 cấp nước chịu nhiệt", "formula": "320.0", "count": 1, "length": 320.0, "width": 1.0, "height": 1.0, "factor": 1.0, "quantity": 320.0}, {"id": 26, "section": "IV. HỆ THỐNG ĐIỆN & CẤP THOÁT NƯỚC (MEP)", "norm_code": "BA.16204", "custom_name": "Kéo rải dây cáp điện đồng CV 2x4,0mm2 luồn ống", "formula": "2400.0", "count": 1, "length": 2400.0, "width": 1.0, "height": 1.0, "factor": 1.0, "quantity": 2400.0}, {"id": 27, "section": "IV. HỆ THỐNG ĐIỆN & CẤP THOÁT NƯỚC (MEP)", "norm_code": "BA.12302", "custom_name": "Lắp đặt bộ đèn LED Panel 600x600mm 40W âm trần", "formula": "180.0", "count": 180, "length": 1.0, "width": 1.0, "height": 1.0, "factor": 1.0, "quantity": 180.0}], "equipment_items": [{"id": 1, "name": "Hệ thống điều hòa không khí trung tâm VRV/VRF đồng bộ dàn nóng & dàn lạnh âm trần", "unit": "hệ thống", "quantity": 1, "unit_price": 680000000}, {"id": 2, "name": "Thang máy tải khách 750kg (10 người) - 4 điểm dừng đồng bộ", "unit": "bộ", "quantity": 1, "unit_price": 590000000}, {"id": 3, "name": "Tủ điện tổng MSB, tủ phân phối tầng DB & hệ thống báo cháy tự động trung tâm", "unit": "hệ thống", "quantity": 1, "unit_price": 245000000}]}, "cong_nghiep_nha_xuong": {"project_info": {"project_name": "Dự án Đầu tư Xây dựng Nhà xưởng Sản xuất & Kho vận Công nghiệp", "building_name": "Nhà xưởng sản xuất chính khung thép tiền chế khẩu độ 36m (Diện tích 3.600 m2)", "investor": "Ban Quản lý Khu Công nghiệp & Đầu tư Xây dựng", "location": "Khu Công nghiệp Tập trung - Vùng II", "funding_source": "Vốn đầu tư công / Vốn nhà nước ngoài ngân sách", "building_type": "cong_nghiep", "building_grade": "cap_3", "design_step": "tkbvtc_2_buoc", "is_bcktkt": false, "is_mountain_island": false, "vat_rate": 8.0, "k_nc": 1.0, "k_m": 1.0, "contingency_volume_rate": 5.0, "contingency_escalation_rate": 3.0, "tmdt_gxdtt_approved_ty": 25.0}, "boq_items": [{"id": 1, "section": "I. PHẦN NỀN MÓNG NHÀ XƯỞNG", "norm_code": "AB.25112", "custom_name": "Đào móng trụ khung thép & đà kiềng bằng máy đào 0,80m3", "formula": "24 * 3.2 * 3.2 * 2.0", "count": 24, "length": 3.2, "width": 3.2, "height": 2.0, "factor": 1.0, "quantity": 491.52}, {"id": 2, "section": "I. PHẦN NỀN MÓNG NHÀ XƯỞNG", "norm_code": "AF.11111", "custom_name": "Bê tông lót móng đá 4x6 M100", "formula": "24 * 2.6 * 2.6 * 0.1", "count": 24, "length": 2.6, "width": 2.6, "height": 0.1, "factor": 1.0, "quantity": 16.224}, {"id": 3, "section": "I. PHẦN NỀN MÓNG NHÀ XƯỞNG", "norm_code": "AF.31123", "custom_name": "Bê tông móng trụ, cổ cột & giằng móng thương phẩm M250", "formula": "24 * 2.4 * 2.4 * 0.8 + 45.0", "count": 1, "length": 155.592, "width": 1.0, "height": 1.0, "factor": 1.0, "quantity": 155.592}, {"id": 4, "section": "I. PHẦN NỀN MÓNG NHÀ XƯỞNG", "norm_code": "AF.61120", "custom_name": "Cốt thép móng & cổ cột đường kính <= 18mm", "formula": "18.5", "count": 1, "length": 18.5, "width": 1.0, "height": 1.0, "factor": 1.0, "quantity": 18.5}, {"id": 5, "section": "I. PHẦN NỀN MÓNG NHÀ XƯỞNG", "norm_code": "AF.15113", "custom_name": "Bê tông nền nhà xưởng chịu tải nặng dày 20cm đá 1x2 M250", "formula": "3600 * 0.2", "count": 1, "length": 3600.0, "width": 1.0, "height": 0.2, "factor": 1.0, "quantity": 720.0}, {"id": 6, "section": "I. PHẦN NỀN MÓNG NHÀ XƯỞNG", "norm_code": "AF.61110", "custom_name": "Thép lưới nền nhà xưởng 2 lớp D10a200", "formula": "44.5", "count": 1, "length": 44.5, "width": 1.0, "height": 1.0, "factor": 1.0, "quantity": 44.5}, {"id": 7, "section": "II. KẾT CẤU KHUNG THÉP & BAO CHE NHÀ XƯỞNG", "norm_code": "AI.11221", "custom_name": "Gia công và lắp dựng cột, kèo, xà gồ thép tổ hợp nhà xưởng công nghiệp", "formula": "142.0", "count": 1, "length": 142.0, "width": 1.0, "height": 1.0, "factor": 1.0, "quantity": 142.0}, {"id": 8, "section": "II. KẾT CẤU KHUNG THÉP & BAO CHE NHÀ XƯỞNG", "norm_code": "AL.16111", "custom_name": "Lợp mái tôn & vách tôn mạ màu dày 0,45mm", "formula": "4850.0", "count": 1, "length": 4850.0, "width": 1.0, "height": 1.0, "factor": 1.0, "quantity": 4850.0}, {"id": 9, "section": "II. KẾT CẤU KHUNG THÉP & BAO CHE NHÀ XƯỞNG", "norm_code": "AE.52213", "custom_name": "Xây tường bao chân vách nhà xưởng cao 2,2m bằng gạch ống vữa XM M75", "formula": "148.0", "count": 1, "length": 148.0, "width": 1.0, "height": 1.0, "factor": 1.0, "quantity": 148.0}, {"id": 10, "section": "II. KẾT CẤU KHUNG THÉP & BAO CHE NHÀ XƯỞNG", "norm_code": "AK.21123", "custom_name": "Trát tường bao nhà xưởng ngoài và trong dày 1,5cm vữa XM M75", "formula": "1350.0", "count": 1, "length": 1350.0, "width": 1.0, "height": 1.0, "factor": 1.0, "quantity": 1350.0}], "equipment_items": [{"id": 1, "name": "Cầu trục dầm đôi nhà xưởng sức nâng 10 tấn khẩu độ 34m đồng bộ đường ray", "unit": "bộ", "quantity": 2, "unit_price": 820000000}, {"id": 2, "name": "Trạm biến áp 1000kVA - 22/0,4kV và tủ điện phân phối công nghiệp", "unit": "hệ thống", "quantity": 1, "unit_price": 980000000}, {"id": 3, "name": "Hệ thống thông gió làm mát áp suất âm và PCCC vách tường tự động", "unit": "hệ thống", "quantity": 1, "unit_price": 540000000}]}}};

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
