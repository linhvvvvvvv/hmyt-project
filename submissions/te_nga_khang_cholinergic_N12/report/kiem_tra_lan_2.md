# Bài kiểm tra lần 2 — N12 — te_nga_khang_cholinergic

- Fork: https://github.com/linhvvvvvvv/hmyt-project · Nhánh: `gd5-proposed-model`
- Thành viên và phân công:
  - NNA - 20233727 - Literature Review, tổng hợp tài liệu và viết báo cáo.
  - VHL - 20233775 - Xử lý dữ liệu FAERS, xây dựng baseline Logistic Regression, chuẩn hóa thuốc và RxNorm.

## A. Literature Review và research gaps

### A1. Chiến lược tìm kiếm

**Mục đích:** Tìm nghiên cứu trả lời ba vấn đề: (1) mô hình ML phân biệt/dự đoán té ngã ở người cao tuổi; (2) số thuốc và gánh nặng kháng cholinergic liên quan thế nào đến té ngã; (3) có thể dùng thông tin thuốc và cảnh báo để hỗ trợ đánh giá người bệnh không.

**Nguồn và phạm vi:** Rà soát PubMed và Google Scholar trong tháng 11/2026; đối chiếu DOI/toàn văn trên trang nhà xuất bản hoặc PubMed Central. Các lượt truy vấn dùng bộ lọc 5 năm (PubMed) và phạm vi năm do người tìm chọn (Google Scholar). Đây là **lượt kiểm tra lại**, không phải nhật ký các lần tìm tài liệu trước đó.

| Nguồn | Từ khóa / truy vấn rà soát | Khoảng năm / bộ lọc | Số kết quả | Số bài giữ lại |
|---|---|---|---:|---|
| PubMed | `(falls OR fall risk) AND (older adults OR elderly) AND (machine learning OR prediction model)` | Bộ lọc **5 years** (giao diện hiển thị 2021–2026) | **1.535** | Gộp chọn cùng các truy vấn khác; không ghi riêng |
| PubMed | `(anticholinergic burden OR ACB) AND (falls OR recurrent falls)` | Bộ lọc **5 years** (giao diện hiển thị 2021–2026) | **102** | Gộp chọn cùng các truy vấn khác; không ghi riêng |
| Google Scholar | `older adults polypharmacy drug drug interactions fall risk` | Trang tìm kiếm hiển thị bộ lọc năm **2021–2026** | **Khoảng 17.700** (ước tính) | Gộp chọn cùng các truy vấn khác; không ghi riêng |
| **Tổng hợp sau khi đọc và loại trùng** | **Bộ tài liệu cuối cùng được phân tích tại A2** | **Bài xuất bản 2023–2026** | **Không cộng ba số trên vì bài có thể trùng nhau** | **10 bài khác nhau** |

**Cách đếm:** Các giá trị **1.535**, **102** và **khoảng 17.700** được đọc trực tiếp từ ảnh kết quả tìm kiếm của nhóm ngày 02/11/2026. Số 17.700 của Google Scholar là ước tính. Nhóm không lưu nhật ký đánh dấu bài được nhận từ *từng* truy vấn, nên chỉ có thể xác nhận **10 bài cuối cùng sau tổng hợp và loại trùng**, không gán tùy ý 10 bài thành 3 nhóm số lượng. Trong PubMed, bộ lọc **5 years** là bộ lọc tương đối theo ngày tìm; nếu cần phạm vi ngày cố định chính xác, phải tìm lại với Custom Range và cập nhật số kết quả.

**Cách lựa chọn 10 bài:** Đọc tiêu đề/tóm tắt để xem có liên quan đến FALL, ML hoặc đặc tính thuốc; đọc Methods/Results và đối chiếu DOI; loại bài trùng và bài không đủ nội dung để đánh giá. Bộ 10 bài ở A2 gồm các nhóm bằng chứng khác nhau: mô hình ML phân loại/dự đoán FALL (#1, #2, #3, #6, #8); mối liên hệ ACB với FALL (#1, #7); cảnh báo/gánh nặng thuốc và các biến cố liên quan (#4, #5, #9, #10). Một bài có thể thuộc nhiều nhóm, nên không cộng các nhóm này thành tổng số kết quả tìm kiếm.

**Bằng chứng nguồn công khai đã đối chiếu cho đủ 10 bài trong A2:** Bảng dưới đây ghi **nơi đọc được bài gốc/toàn văn**, không có nghĩa cả 10 bài đều xuất hiện từ cùng một truy vấn PubMed. DOI của từng bài được trình bày trong A2.

| Bài ở A2 | Tác giả (năm) | Nguồn công khai đã kiểm tra |
|---|---|---|
| #1 | Dinh (2023) | [PLOS ONE – toàn văn](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0280907) |
| #2 | Lin (2025) | [Frontiers – toàn văn](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2025.1597853/full) |
| #3 | Liu (2025) | [Frontiers – toàn văn](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2025.1628493/full) |
| #4 | Delvallée (2024) | [PubMed Central – toàn văn](https://pmc.ncbi.nlm.nih.gov/articles/PMC11587406/) |
| #5 | Kim (2026) | [PubMed Central – toàn văn](https://pmc.ncbi.nlm.nih.gov/articles/PMC13467294/) |
| #6 | Larrañaga (2026) | [Frontiers – toàn văn](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1852439/full) |
| #7 | Xu (2025) | [PubMed – bản ghi](https://pubmed.ncbi.nlm.nih.gov/40586120/) · [PubMed Central – toàn văn](https://pmc.ncbi.nlm.nih.gov/articles/PMC12207211/) |
| #8 | Yang (2026) | [JMIR Aging – toàn văn](https://aging.jmir.org/2026/1/e80602) |
| #9 | Jøsendal (2026) | [PubMed Central – toàn văn](https://pmc.ncbi.nlm.nih.gov/articles/PMC13010666/) |
| #10 | Vennard (2026) | [PubMed Central – toàn văn](https://pmc.ncbi.nlm.nih.gov/articles/PMC13266442/) |

**Phân biệt:** Bảng trên ghi **số kết quả của ba lượt tìm thực tế** và **10 bài cuối cùng sau tổng hợp**. Số bài chọn riêng từng truy vấn không thể suy ra từ bảng 10 bài nếu không lưu log truy xuất/đánh dấu trùng.

**Tiêu chí chọn:** Liên quan đến người cao tuổi, té ngã, sử dụng nhiều thuốc, ACB, DDI hoặc hỗ trợ cảnh báo thuốc; có phương pháp và kết quả đối chiếu được; ưu tiên toàn văn và các công bố gần đây. **Tiêu chí loại:** Bài trùng lặp, không phù hợp câu hỏi nhóm, hoặc thiếu thông tin cần thiết để phân tích phương pháp/kết quả.

**Giới hạn tìm kiếm:** Ba truy vấn có thể trả về những bài trùng nhau; bộ tài liệu cuối cùng được chọn có **10 bài**. Google Scholar cung cấp tổng số kết quả mang tính ước lượng; việc có bài toàn văn công khai không đồng nghĩa bài đó xuất hiện trong một truy vấn nhất định.

### A2. Ma trận y văn (10 bài)

*Dữ liệu trích từ workbook Literature Review 10 bài của nhóm. Tên bài và DOI giữ theo workbook; các số liệu cần được nhóm đối chiếu nguồn gốc trước khi xác nhận nộp.*

| # | Bài (tác giả + tên bài) | DOI / link | Dataset (n, nguồn) | Phương pháp | Kết quả chính (metric, giá trị) | Kiểm định ngoài? | Hạn chế chính |
|---|---|---|---|---|---|---|---|
| 1 | Dinh et al. (2023) — Anticholinergic burden measures, symptoms, and fall-associated risk in older adults with polypharmacy: Development and validation of a prognostic model | [DOI](https://doi.org/10.1371/journal.pone.0280907) | RIME n=1.197; PRIMUM n=502; theo dõi FALL trong 6 tháng | Dùng 5 thang gánh nặng kháng cholinergic; so sánh mô hình có và không thêm thông tin thuốc/triệu chứng. | Mô hình nền AUC 0,712; thêm thuốc và triệu chứng đạt 0,732; khi kiểm tra ở nhóm độc lập AUC 0,632. Khi mô hình đã có triệu chứng, thêm gánh nặng thuốc chỉ tăng AUC khoảng 0,002. | Có: PRIMUM độc lập | Năm thang đo không phải ACB 2012; kết quả kiểm tra ngoài thấp hơn phát triển mô hình. |
| 2 | Lin et al. (2025) — Urban–rural disparities in fall risk among older Chinese adults: Insights from machine learning-based predictive models | [DOI](https://doi.org/10.3389/fpubh.2025.1597853) | CHARLS Trung Quốc n=5.876; thành thị/nông thôn; theo dõi 2015–2018 | Thử 5 thuật toán ML cho nhóm thành thị và nông thôn; so ROC-AUC, các chỉ số khác và giải thích biến. | Theo Table 3: nông thôn Random Forest AUC 0,732; thành thị Logistic Regression AUC 0,727, nhỉnh hơn Random Forest 0,724. | Chưa thấy kiểm định ngoài độc lập | Abstract và Table 3 không thống nhất AUC thành thị; có điểm cần xem kỹ về thứ tự tiền xử lý; chưa thấy kiểm định ngoài độc lập. |
| 3 | Liu et al. (2025) — Predicting fall risk among older adults in Chinese communities with advanced machine learning techniques: A retrospective study | [DOI](https://doi.org/10.3389/fpubh.2025.1628493) | Khảo sát cộng đồng Trung Quốc n=977; train 732, test 245 | So sánh 6 thuật toán ML; dùng SHAP để xem mô hình dựa nhiều vào biến nào. | CatBoost AUC test 0,8719 khi so 6 thuật toán; cấu hình sau chọn biến đạt 0,8748. SHAP nêu bật tiền sử ngã, bệnh đi kèm và tình trạng dùng nhiều thuốc. | Không: chia train/test cùng nguồn | Hồi cứu, người tham gia tự báo ngã, một khu vực; thiếu kiểm định ngoài; không đánh giá riêng ACB/DDI. |
| 4 | Delvallée et al. (2024) — Impact of a Clinical Decision Support System on the Change over Time in the Anticholinergic Load in Geriatric Patients: The SADP-Antichol Study | [DOI](https://doi.org/10.3390/pharmacy12060162) | Bệnh nhân cao tuổi tại một bệnh viện Pháp; hai giai đoạn 6 tuần | Phần mềm phát hiện đơn có thuốc cần xem xét; dược sĩ kiểm tra và đề xuất thay đổi; so với chăm sóc thường quy. | 144 cảnh báo được tạo, 87 phù hợp; 19/36 đề xuất được bác sĩ chấp nhận. Điểm gánh nặng thuốc giảm trung bình 1,61 so với 0,67. | Không áp dụng: không phải ML dự đoán FALL | Không dự đoán FALL; không dùng ACB 2012 làm thang chính; nghiên cứu một bệnh viện, không chứng minh hiệu quả giảm ngã. |
| 5 | Kim et al. (2026) — Explainable Machine Learning for Predicting Adverse Drug Events in Older Adults with Polypharmacy: A Single-Center Retrospective Cohort Study | [DOI](https://doi.org/10.3390/jcm15155824) | Hồ sơ ngoại trú Hàn Quốc n=7.505; ADE 90 ngày | Chia theo số thuốc; dùng Logistic Regression, Random Forest, LightGBM; SHAP để giải thích mô hình. | ADE ở nhóm 0–4 thuốc: 2,4%; 5–9 thuốc: 5,1%; ≥10 thuốc: 12,5%. Số thuốc là biến quan trọng; Logistic Regression AUC 0,705. | Không thấy kiểm định ngoài độc lập | ADE không phải riêng FALL; một trung tâm, thiếu kiểm định ngoài; không kiểm chứng ACB/DDI. |
| 6 | Larrañaga et al. (2026) — Predicting first falls among older adults with chronic conditions and polypharmacy using routinely collected health records | [DOI](https://doi.org/10.3389/frai.2026.1852439) | Hồ sơ y tế Tây Ban Nha n=35.197; người ≥65 tuổi | Dùng hồ sơ y tế trước mốc ngã; so Logistic Regression, Random Forest và XGBoost; phân tích nhóm thuốc. | Nhóm có ngã dùng trung bình 10,3 thuốc, nhóm không ngã 8,8. Các mô hình ROC-AUC khoảng 0,71; số đơn thuốc và thuốc chống trầm cảm có đóng góp. | Chưa thấy kiểm định ngoài độc lập | Đối tượng có bệnh mạn tính nặng, không đại diện tất cả người già; thiếu nhiều biến vận động; không thử trực tiếp ACB/DDI. |
| 7 | Xu et al. (2025) — Changes in anticholinergic cognitive burden and risk of single and recurrent falls: Population-based cohort study | [DOI](https://doi.org/10.1093/ageing/afaf177) | EPIC-Norfolk n=10.717; không chỉ người ≥65 tuổi | Theo dõi thay đổi mức tiếp xúc thuốc kháng cholinergic, so nhóm không dùng với nhóm bắt đầu/dùng ngắt quãng/dùng liên tục. | So với nhóm không tiếp xúc: OR té ngã tái diễn 1,49 (bắt đầu muộn), 1,66 (ngắt quãng), 1,67 (liên tục). | Không áp dụng: phân tích liên hệ | Mẫu gồm cả người từ 40 tuổi, tuổi trung vị 55,6; quan sát nên không chứng minh thuốc gây ngã; không đánh giá ML. |
| 8 | Yang et al. (2026) — Development and Validation of Machine Learning Models for Predicting Falls Among Hospitalized Older Adults: Retrospective Cross-Sectional Study | [DOI](https://doi.org/10.2196/80602) | Bệnh nhân nội trú n=1.026; 342 FALL, 684 đối chứng | Dùng thông tin bệnh, thuốc và xét nghiệm, thử các thuật toán ML; chọn Gradient Boosting làm mô hình nổi bật. | Gradient Boosting đạt C-index khoảng 0,744 (95% CI 0,688–0,799) trên đánh giá được báo cáo. | Chưa xác minh kiểm định ngoài | Thiết kế hồi cứu chọn ca/đối chứng; tỉ lệ FALL 1/3 do chọn mẫu; không có kiểm định ngoài độc lập rõ ràng. |
| 9 | Jøsendal et al. (2026) — The Use of Direct Oral Anticoagulants (DOACs) in Older Adults Receiving Multidose Drug Dispensing; Interactions, Anticholinergic and Fall-Risk Increasing Drugs | [DOI](https://doi.org/10.3390/geriatrics11020030) | Người cao tuổi dùng DOAC n=13.215 | Đối chiếu danh sách thuốc với cơ sở tương tác DDI, danh mục thuốc tăng nguy cơ té ngã (FRID) và thang CRIDECO. | 26,8% có ít nhất một DDI liên quan DOAC; 0,2% có DDI nghiêm trọng; 96,7% dùng ít nhất một FRID; 46,8% có điểm kháng cholinergic ≥3. | Không áp dụng: nghiên cứu thuốc | Chỉ người dùng DOAC; dùng CRIDECO không phải ACB 2012; không dự đoán và không ghi nhận số lần té ngã. |
| 10 | Vennard et al. (2026) — Anticholinergic Medication Burden Scales: A Systematic Review | [DOI](https://doi.org/10.1111/jgs.70352) | Tổng quan các thang đánh giá kháng cholinergic | Tổng hợp cách phát triển, danh mục thuốc và điểm chấm ở các thang đo kháng cholinergic. | Tìm được 21 thang đo; cách chọn thuốc và mức điểm khác nhau giữa các thang. Không có một thang duy nhất là đáp án đúng cho mọi bối cảnh. | Không áp dụng: tổng quan | Không nghiên cứu mô hình ML hoặc chứng minh ACB làm giảm/ngăn té ngã. |

### A3. Research gaps

Các khoảng trống dưới đây rút ra từ **10 bài trong A2**, không khẳng định đây là vấn đề chưa từng được nghiên cứu trên thế giới.

| Mã | Khoảng trống (1–2 câu) | Bằng chứng (# trong A2) | Dự án nhóm giải quyết như thế nào |
|---|---|---|---|
| G1 | Bài Dinh đã kiểm tra gánh nặng kháng cholinergic nhưng không dùng ACB 2012 và mức cải thiện AUC nhỏ. Chưa rõ ACB 2012 có giúp phân biệt báo cáo FALL trong FAERS không. | #1, #7, #10 | Tính điểm ACB 2012, so mô hình nền và mô hình thêm ACB trên cùng tập test, báo cáo ROC-AUC và AP. |
| G2 | Các bài về số thuốc và nhóm thuốc cho thấy thuốc có liên quan tới biến cố, nhưng chưa chứng minh thêm ACB/DDI sẽ cải thiện mô hình chỉ dùng số thuốc. | #3, #5, #6, #9 | Chuẩn hóa tên thuốc; xây đặc trưng ACB/DDI; so với baseline tuổi, giới tính và số thuốc. |
| G3 | Phần mềm cảnh báo có thể giúp giảm điểm gánh nặng thuốc nhưng chưa chứng minh giảm té ngã; hiệu quả cảnh báo khác hiệu quả dự đoán FALL. | #4, #9 | Đánh giá riêng độ bao phủ/tính đúng đắn của ACB/DDI và hiệu quả phân loại FALL; không coi cảnh báo là chứng cứ giảm ngã. |
| G4 | Các nghiên cứu có dữ liệu, nhãn và tập bệnh nhân khác nhau; hiệu quả trên tập nội bộ chưa đảm bảo áp dụng ở nơi khác. | #1, #2, #3, #6, #8 | Công khai giới hạn FAERS, báo cáo AP/ROC-AUC, calibration và khoảng tin cậy nếu tính được; không so AUC giữa các bài như cùng một thí nghiệm. |

### A4. Thẩm định một bài trọng tâm bằng PROBAST+AI

**Bài #1 Dinh et al. (2023)** — chọn vì dự đoán FALL trong 6 tháng, có mô hình nền, so sánh gánh nặng kháng cholinergic và kiểm định ngoài thực sự. Nguồn: https://doi.org/10.1371/journal.pone.0280907

| Miền | Nguy cơ sai lệch (thấp/cao/không rõ) | Căn cứ từ nghiên cứu; cần đối chiếu checklist môn |
|---|---|---|
| Người tham gia và nguồn dữ liệu | Không rõ (đánh giá sơ bộ) | Dữ liệu RIME để phát triển (1.197) và PRIMUM để kiểm định ngoài (502); cần đánh giá tiêu chí tuyển, loại và đại diện quần thể trong phần Methods. |
| Biến dự báo | Không rõ (đánh giá sơ bộ) | Thang ACh và triệu chứng được đưa vào mô hình; cần kiểm tra thời điểm đo, cách xác định thuốc và thiếu dữ liệu. |
| Kết cục | Không rõ (đánh giá sơ bộ) | Kết cục ≥1 lần ngã trong 6 tháng theo dõi; cần đánh giá độ tin cậy của cách thu thập và tính độc lập với biến dự báo. |
| Phân tích | Không rõ (đánh giá sơ bộ) | Hồi quy logistic, chọn biến theo AIC và MFP; bootstrap; c-statistic tối đa phát triển 0,732, ngoài 0,632, calibration slope ngoài 0,716. Cần xem xử lý thiếu dữ liệu/overfitting và checklist đầy đủ. |

**Tính áp dụng:** Hữu ích để kiểm tra giá trị tăng thêm của ACB, nhưng quần thể bệnh nhân theo dõi và kết cục ngã 6 tháng khác hẳn FAERS (nhãn báo cáo chứa FALL), nên không thể chuyển kết quả hay mức nguy cơ lâm sàng sang FAERS.

## B. Kết quả và timeline

### B1. Kết quả hiện có

**Dữ liệu:** FAERS 2025 Q1–Q4, báo cáo có tuổi ≥65; giữ `caseversion` lớn nhất theo `caseid`. Nhãn `FALL=1` khi bảng REAC có phản ứng `FALL`, còn lại là báo cáo không ghi nhận FALL. Đây là **phân loại báo cáo FAERS**, không phải dự báo chắc chắn bệnh nhân sẽ ngã trong tương lai.

| Mô hình | Tập đánh giá (cách chia, n) | Metric chính (giá trị, 95% CI nếu có) | Metric phụ | Nguồn số liệu (file/notebook/W&B) |
|---|---|---|---|---|
| **Baseline 1 — Logistic Regression** (tuổi, giới tính, số loại thuốc khác nhau) | Tập dữ liệu **342.948** báo cáo; train **274.358**, test **68.590**; chia 80/20 theo `caseid` sau khi chọn phiên bản mới nhất | **ROC-AUC = 0,6291**; **95% CI chưa tính** | **AP = 0,0551**; test có **1.986 FALL** (~2,90%); precision FALL khoảng **0,04**, recall khoảng **0,52** ở ngưỡng đã sử dụng | [Code Logistic Regression](../code/chay_baseline.py); [Báo cáo baseline](../results/bao_cao_baseline.txt); [Dự đoán test](../results/du_doan_test.csv); [Ma trận nhầm lẫn](../results/confusion_matrix.png). |
| **Mô hình đề xuất — baseline + ACB + DDI** | Chưa chạy đánh giá cuối trên tập test | **Chưa có ROC-AUC / CI** | Chưa có AP/recall đã kiểm chứng | Đang chuẩn bị thông tin thuốc; **chưa có output mô hình kết hợp**. |

**Các công việc đã có code, nhưng không phải bằng chứng cho ROC-AUC baseline:**

- **Bước tách hoạt chất:** [Code tách hoạt chất](../code/tach_hoat_chat_csv.py) đọc `FAERS_2025_65plus_medications.csv`, tạo `KET_QUA_TACH_THUOC/01_MOI_DONG_THUOC_TACH_HOAT_CHAT.csv`, `02_DANH_MUC_HOAT_CHAT_CAN_XAC_MINH.csv`, `03_CHUA_RO_HOAT_CHAT.csv`, `04_MOI_HO_SO_MOI_HOAT_CHAT_KHONG_TRUNG.csv`. Code tách tên/hoạt chất sơ bộ, **chưa gán điểm ACB**.
- **Bước tra RxNorm:** [Code RxNorm](../code/xac_minh_rxnorm.py) đọc `02_DANH_MUC_HOAT_CHAT_CAN_XAC_MINH.csv`, gọi RxNorm API và xuất `RXNORM_KET_QUA/01_KET_QUA_DANH_MUC.csv`, `02_CAN_KIEM_TRA.csv`, `03_DA_KHOP_RXNORM.csv`. Các tên khớp vẫn cần kiểm tra chất lượng; các cột `ACB_2012` và `ACB_source` đang để trống trong code.
- **Chưa có bằng chứng đã hoàn thành:** Xác minh toàn bộ tên thuốc, tính ACB cho từng báo cáo, tạo biến DDI, hoặc chạy mô hình kết hợp ACB + DDI.


**Bằng chứng B1 đã được lưu trên GitHub:** Nhóm đã tải lên mã nguồn và các tệp kết quả của mô hình Logistic Regression, bao gồm:

(1) [Code Logistic Regression](../code/chay_baseline.py) — mã nguồn huấn luyện và đánh giá mô hình baseline.

(2) [Báo cáo kết quả baseline](../results/bao_cao_baseline.txt) — ghi nhận ROC-AUC = 0,6291, Average Precision = 0,0551 cùng precision, recall, F1-score và confusion matrix.

(3) [Kết quả dự đoán tập test](../results/du_doan_test.csv) — tệp lưu kết quả dự đoán trên tập kiểm tra.

(4) [Ma trận nhầm lẫn](../results/confusion_matrix.png) — hình ảnh thể hiện kết quả phân loại trên tập test.

Ngoài ra, nhóm đã bổ sung [code tách hoạt chất](../code/tach_hoat_chat_csv.py), [code ánh xạ RxNorm](../code/xac_minh_rxnorm.py) và các tệp [thuốc đã khớp RxNorm](../results/03_DA_KHOP_RXNORM.csv), [thuốc cần kiểm tra](../results/02_CAN_KIEM_TRA.csv) để minh chứng tiến độ chuẩn hóa dữ liệu thuốc. Các kết quả này chưa bao gồm điểm ACB 2012 và đặc trưng DDI, do đó chưa được sử dụng để đánh giá mô hình kết hợp ACB + DDI.

### B2. Ablation (Mốc 3)

| Cấu hình | Metric chính | Chênh lệch so với mô hình đầy đủ | Nguồn |
|---|---|---|---|
| Baseline thông tin cơ bản | ROC-AUC 0,6291; AP 0,0551 (đã đối chiếu với báo cáo baseline) | Chưa áp dụng — mô hình đầy đủ chưa được đánh giá | [Code](../code/chay_baseline.py); [Kết quả](../results/bao_cao_baseline.txt) |
| Baseline + ACB | Chưa chạy/không có bằng chứng kết quả | Chưa tính | Không áp dụng — chưa có output |
| Baseline + DDI | Chưa chạy/không có bằng chứng kết quả | Chưa tính | Không áp dụng — chưa có output |
| Baseline + ACB + DDI | Chưa chạy/không có bằng chứng kết quả | Mốc đối chiếu chưa có | Không áp dụng — chưa có output |

### B3. Đối chiếu với y văn

Baseline báo cáo ROC-AUC 0,6291 thấp hơn chỉ số công bố của Liu #3 (CatBoost 0,8719) và Larrañaga #6 (AUC ≈0,71), nhưng **không chứng minh mô hình nhóm kém hơn về mặt phương pháp**: Liu dùng 977 người từ cộng đồng, thông tin lâm sàng như tiền sử ngã và chức năng vận động; Larrañaga dùng EHR bệnh nhân, định nghĩa ngã sau khoảng 90 ngày không ghi nhận; còn nhãn FAERS của nhóm là *FALL xuất hiện trong báo cáo*. Nghiên cứu Dinh #1 có c-statistic ngoài 0,632, nhưng cũng có định nghĩa kết cục trong 6 tháng và quần thể khác, nên không so trực tiếp để tuyên bố hai mô hình tương đương.

### B4. Timeline đến khi hoàn thành

| Việc | Phụ trách (MSSV/vai trò) | Mốc | Ngày dự kiến | Trạng thái + bằng chứng |
|---|---|---|---|---|
| Rà nguồn/làm sạch FAERS, đối chiếu nhãn/caseid | VHL (20233775) | M3 tuần 10 | Đã thực hiện giai đoạn baseline; rà soát tiếp trong M4 | Đã có tổng hợp dữ liệu 342.948 báo cáo và [baseline](../results/bao_cao_baseline.txt); chưa có script lọc FAERS gốc trong repo |
| Kiểm tra tên thuốc và kết quả ánh xạ RxNorm | VHL (20233775) | M3–M4 | Tuần 12 (dự kiến) | Đã có [code RxNorm](../code/xac_minh_rxnorm.py), [kết quả khớp](../results/03_DA_KHOP_RXNORM.csv) và [danh sách cần rà](../results/02_CAN_KIEM_TRA.csv); chưa hoàn tất xác minh |
| Tính ACB 2012, đánh giá độ phủ | VHL (20233775) | M4 tuần 12 | Tuần 12 (dự kiến) | Chưa có kết quả tính ACB; cần xây bảng ánh xạ và kiểm tra tên thuốc |
| Chọn nguồn DDI, tính đặc trưng tương tác | VHL (20233775) | M4–Final | Sau bước chuẩn hóa thuốc (chưa chốt ngày) | Chưa có output DDI; cần lựa chọn nguồn tương tác và quy tắc gán nhãn |
| So sánh mô hình, ablation, calibration và 95% CI | VHL (20233775), NNA (20233727) phối hợp tổng hợp | M4–Final | Trước báo cáo cuối kỳ (chưa chốt ngày) | Đã có [baseline](../results/bao_cao_baseline.txt); chưa chạy mô hình ACB/DDI và đánh giá mở rộng |
| Hoàn thiện Literature Review, báo cáo và bằng chứng GitHub | NNA (20233727), VHL (20233775) phối hợp | M3–Final tuần 15 | Trước nộp cuối kỳ (chưa chốt ngày) | Đã có báo cáo A–D và 10 bài y văn; cần hoàn thiện checklist, cập nhật README và kiểm tra liên kết |

### B5. Rủi ro / đang vướng / câu hỏi cho GV

- Nhãn FAERS phản ánh có ghi nhận từ FALL trong báo cáo, **không phải nguy cơ ngã tương lai**; đề nghị GV xác nhận phạm vi tuyên bố phù hợp.
- Thiếu T0 rõ ràng và định danh bệnh nhân duy nhất; chia theo caseid chưa chứng minh chia theo bệnh nhân.
- Mất cân bằng nhãn (~3%) và khả năng sai lệch báo cáo tự nguyện; không suy tỷ lệ FALL thành tỷ lệ té ngã trong quần thể.
- Tên thuốc phức tạp, không khớp bảng ACB/DDI, thiếu thời gian phơi nhiễm; cần kiểm tra độ phủ và không gán điểm 0 cho thuốc chưa khớp.

## C. Tự đánh giá FAIR, TRIPOD+AI, PROBAST+AI

### C1. FAIR - dữ liệu

| Mục | Trả lời | Bằng chứng |
|---|---|---|
| Nguồn, phiên bản, ngày tải; checksum | Dữ liệu FAERS 2025 Q1–Q4 do FDA công bố. Ngày tải gốc chưa xác nhận; SHA-256 cần tính từ file đã xử lý. | [Nguồn dữ liệu FDA](https://fis.fda.gov/extensions/FPD-QDE-FAERS/FPD-QDE-FAERS.html) |
| Giấy phép / DUA | FAERS là dữ liệu báo cáo biến cố bất lợi được công khai. Trang openFDA ghi giấy phép Public Domain/CC0; cần phân biệt với điều khoản của bộ file FAERS tải trực tiếp. | [Trang openFDA](https://open.fda.gov/data/faers/) |
| Datasheet | Nhóm sử dụng báo cáo FAERS 2025 Q1–Q4, lọc tuổi ≥65, giữ phiên bản mới nhất theo caseid và xác định FALL từ REAC. Bộ dữ liệu cuối gồm 342.948 báo cáo. | [Datasheet FAERS](../data_docs/datasheet.md); code lọc FAERS gốc chưa có trong thư mục nộp |
| Không có định danh bệnh nhân | Dữ liệu được tổ chức theo mã báo cáo caseid, không phải mã định danh bệnh nhân. Nhóm cần kiểm tra các cột trong file đầu ra trước khi xác nhận không có thông tin định danh trực tiếp. | [Datasheet FAERS — mục bảo mật](../data_docs/datasheet.md); chưa có kết quả kiểm tra từng cột được công bố |

### C2. Hướng dẫn báo cáo

- **Câu hỏi nghiên cứu:** Việc bổ sung đặc trưng ACB và DDI có giúp cải thiện khả năng phân biệt các báo cáo FAERS của người ≥65 tuổi có ghi nhận FALL so với các báo cáo không ghi nhận FALL, so với mô hình nền dựa vào tuổi, giới và số thuốc?
- **Hướng dẫn báo cáo:** Ưu tiên **TRIPOD+AI**, vì nhóm phát triển/đánh giá mô hình dự đoán/phân loại; không phải STARD-AI đánh giá xét nghiệm chẩn đoán hay DECIDE-AI đánh giá triển khai can thiệp trong thực hành. Cần đối chiếu mục 3.2 phụ lục thầy.
- **Số mục checklist đáp ứng/tổng:** Chưa hoàn tất đối chiếu từng mục TRIPOD+AI, vì vậy chưa xác định số mục đáp ứng/tổng. Những điểm chưa đáp ứng hoặc cần kiểm tra gồm: T0, 95% CI, calibration, kiểm định ngoài, mô hình M3; cần rà tất cả mục theo phụ lục.
- **Kết cục, nhãn, T0, biến có sẵn tại T0:** FALL=1 khi REAC có phản ứng FALL; FALL=0 nếu không có ghi nhận FALL; không xác định được T0 tiền biến cố rõ ràng từ dữ liệu hiện tại. Các biến tuổi/giới/số thuốc là thông tin tại thời điểm được báo cáo, chưa chứng minh đã có *trước* FALL.

### C3. PROBAST+AI — tự thẩm định

| Miền | Nguy cơ sai lệch | Căn cứ trong repo | Việc sẽ làm để giảm nguy cơ |
|---|---|---|---|
| Người tham gia/nguồn | Cao hoặc không rõ — đánh giá sơ bộ | FAERS tự nguyện, thiếu đại diện cho toàn bộ người cao tuổi; [Datasheet](../data_docs/datasheet.md) | Nêu phạm vi suy luận chỉ ở mức báo cáo, mô tả chọn/loại, thiếu dữ liệu |
| Biến dự báo | Không rõ | Tuổi/giới/số thuốc; thời điểm trước kết cục chưa rõ; ACB/DDI chưa xác minh | Kiểm tra thời điểm thuốc, nguồn ánh xạ và độ bao phủ; hạn chế đặc trưng hậu biến cố |
| Kết cục | Cao cho mục tiêu nguy cơ tương lai | Nhãn FALL từ REAC trong cùng báo cáo; T0 chưa có | Định nghĩa lại bài toán phân loại report-level; không tuyên bố dự đoán lâm sàng |
| Phân tích | Không rõ | Chia 80/20 theo caseid; đã có [code baseline](../code/chay_baseline.py), [báo cáo kết quả](../results/bao_cao_baseline.txt). Chưa đánh giá đầy đủ fit preprocessing, calibration và 95% CI | Rà `chay_baseline.py`, kiểm tra thứ tự fit tiền xử lý, tập test bất biến; bootstrap CI/calibration |

**Tính áp dụng:** Chỉ trình bày như nghiên cứu khám phá liên hệ của thông tin thuốc với trạng thái có báo cáo FALL trong FAERS; chưa đủ điều kiện dùng để quyết định lâm sàng hay ước lượng nguy cơ té ngã tuyệt đối.

### C4. Bảng kiểm nhanh

| Mục | Đạt / Chưa | Bằng chứng |
|---|---|---|
| Datasheet | Đã có bản mô tả, cần bổ sung xác minh một số trường | [Datasheet](../data_docs/datasheet.md) |
| Phiên bản + checksum dữ liệu | Chưa | Q1–Q4 2025; thiếu checksum và ngày tải |
| Không định danh; căn cứ được phép dùng | Chưa hoàn tất rà soát dữ liệu đầu ra | [Nguồn FDA](https://www.fda.gov/drugs/surveillance/fda-adverse-event-reporting-system-faers); [Datasheet](../data_docs/datasheet.md); cần kiểm tra các trường dữ liệu |
| Chọn đúng hướng dẫn + checklist | Chưa | Đề xuất TRIPOD+AI; chưa đối chiếu từng mục |
| Định nghĩa kết cục, nhãn, T0 | Chưa đầy đủ | Có nhãn REAC FALL; không có T0 tiền biến cố |
| Chia theo bệnh nhân; fit tiền xử lý chỉ train | Chưa xác minh | Chia theo caseid, không chứng minh patient-level / pipeline |
| Mô hình mốc hồi quy logistic | Đã có code và output | ROC-AUC 0,6291, AP 0,0551; [code](../code/chay_baseline.py), [output](../results/bao_cao_baseline.txt) |
| AUC + calibration + Brier + 95% CI | Chưa | Chỉ có AUC/AP được báo cáo |
| Cỡ mẫu và giới hạn áp dụng | Chưa đầy đủ | 342.948 báo cáo; FALL 10.499 (3,06%); cần phân tích sự kiện/mẫu và nguồn sai lệch |

## D. Khai báo dùng AI

| Công cụ | Dùng cho phần nào | Nhóm đã kiểm chứng lại bằng cách nào |
|---|---|---|
| ChatGPT (OpenAI) | Hỗ trợ tổ chức bảng y văn, soạn bản nháp A–D, giải thích PROBAST+AI, gợi ý khoảng trống và đối chiếu bài công bố | Đối chiếu DOI và văn bản bài báo trên nhà xuất bản/PubMed; đối chiếu ROC-AUC và AP với [output baseline](../results/bao_cao_baseline.txt); các phần chưa có bằng chứng được trình bày là chưa hoàn thành |
