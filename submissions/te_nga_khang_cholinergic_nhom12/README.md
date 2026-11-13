# N12 — Phân loại báo cáo FAERS có ghi nhận FALL ở người cao tuổi

- **Mã đề tài:** 3.3 — `te_nga_khang_cholinergic`
- **Mã nhóm:** `nhom12`
- **Nhánh nộp:** `gd5-proposed-model`
- **Fork bài nộp:** https://github.com/linhvvvvvvv/hmyt-project
- **Repo dự án:** https://github.com/linhvvvvvvv/176336_N12_fall_risk_prediction

## Thành viên và phân công

- **NNA — 20233727:** Literature Review, tổng hợp tài liệu và viết báo cáo.
- **VHL — 20233775:** Xử lý dữ liệu FAERS, huấn luyện baseline Logistic Regression, chuẩn hóa thuốc và RxNorm.

## Tài liệu, mã nguồn và kết quả

- [Báo cáo kiểm tra lần 2](report/kiem_tra_lan_2.md)
- [Datasheet FAERS](data_docs/datasheet.md)
- [Mã nguồn baseline](code/chay_baseline.py)
- [Mã nguồn tách hoạt chất](code/tach_hoat_chat_csv.py)
- [Mã nguồn RxNorm](code/xac_minh_rxnorm.py)
- [Báo cáo chỉ số baseline](results/bao_cao_baseline.txt)
- [Confusion matrix](results/confusion_matrix.png)
- [Kết quả dự đoán test](results/du_doan_test.csv)

## Tình trạng tại mốc kiểm tra

Bộ dữ liệu báo cáo FAERS 2025 Q1–Q4 gồm 342.948 báo cáo ≥65 tuổi; baseline Logistic Regression dùng tuổi, giới và số loại thuốc có ROC-AUC = 0,6291, AP = 0,0551. Nhóm đã có code tách hoạt chất và RxNorm; chưa hoàn thành đặc trưng ACB 2012, DDI hoặc mô hình kết hợp. Nhãn FALL chỉ thể hiện có ghi nhận phản ứng FALL trong báo cáo FAERS, không phải nguy cơ té ngã lâm sàng trong tương lai.

**Lưu ý:** Thư mục `code/` và `results/` cần được giữ lại từ bản bài nộp đã upload trước đây; gói chỉnh sửa này không chứa lại các tệp đó.
