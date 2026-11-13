# Datasheet — FAERS 2025, báo cáo người từ 65 tuổi

## Nguồn và phiên bản
- Nguồn: FDA Adverse Event Reporting System (FAERS), giai đoạn Q1–Q4 năm 2025.
- Bảng dữ liệu nhóm sử dụng: DEMO, DRUG, REAC, THER.
- Ngày tải các tệp gốc: chưa được ghi nhận trong tài liệu hiện có.
- SHA-256: chưa tính; cần ghi kèm tên file cụ thể sau khi tính.
- Nguồn công khai: https://www.fda.gov/drugs/surveillance/fda-adverse-event-reporting-system-faers

## Đối tượng, đơn vị phân tích và xử lý
- Báo cáo FAERS có tuổi được chuẩn hóa về năm và từ 65 tuổi trở lên.
- Giữ phiên bản có `caseversion` cao nhất của mỗi `caseid`.
- Nhãn `FALL=1` khi bảng REAC ghi nhận phản ứng `FALL`; `FALL=0` nghĩa là **không ghi nhận FALL trong báo cáo**, không có nghĩa người đó chưa từng ngã.
- Đơn vị phân tích: **ca báo cáo FAERS**, không phải bệnh nhân duy nhất.
- Tổng số: 342.948; train 274.358; test 68.590, chia theo `caseid`.
- Số báo cáo FALL toàn bộ: 10.499 (~3,06%); test: 1.986 (~2,90%).

## Các biến baseline
| Biến | Mô tả |
|---|---|
| `age_years` | Tuổi quy về năm |
| `sex` | Giới tính trong báo cáo |
| `n_unique_meds` | Số thuốc khác nhau theo cách xử lý của nhóm |
| `FALL` | Có/không ghi nhận phản ứng FALL |

## Tiến độ chuẩn hóa thuốc
- [Script tách hoạt chất](../code/tach_hoat_chat_csv.py): tạo danh mục hoạt chất sơ bộ từ `prod_ai_reported` hoặc tên thuốc dự phòng.
- [Script xác minh RxNorm](../code/xac_minh_rxnorm.py): tra RxNorm và chia tên thành [đã khớp](../results/03_DA_KHOP_RXNORM.csv) / [cần kiểm tra](../results/02_CAN_KIEM_TRA.csv).
- Chưa tính xong ACB 2012 cho từng `caseid` và chưa tạo đặc trưng DDI.

## Giới hạn và bảo mật
- FAERS là dữ liệu báo cáo biến cố bất lợi, không phải nghiên cứu theo dõi tiến cứu; không đủ căn cứ để suy ra nguy cơ ngã tương lai hay quan hệ nhân quả.
- Dữ liệu có thể thiếu thông tin và có sai lệch báo cáo; `caseid` không phải định danh bệnh nhân.
- **Chưa kiểm tra toàn diện tên cột/nội dung tệp CSV được tải lên GitHub** để xác nhận không có định danh trực tiếp. Cần kiểm tra trước khi công bố.
- Chưa có mã code lọc FAERS gốc trong thư mục `code` hiện đang được chuẩn bị; phải bổ sung nếu tìm lại được.
