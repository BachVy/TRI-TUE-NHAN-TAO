# Triển Khai Thuật Toán K-Means Clustering Tùy Chỉnh Và Trực Quan Hóa
## Giới Thiệu
Dự án này triển khai thuật toán K-Means Clustering theo phong cách lập trình hướng đối tượng (OOP) bằng Python. Nó hỗ trợ tải dữ liệu từ nhiều nguồn (ngẫu nhiên, file CSV, hoặc bộ dữ liệu Iris từ Scikit-learn), thực hiện phân cụm, visualize kết quả và đánh giá độ chính xác (nếu có nhãn thực tế).
### Tính Năng Chính
- Tải dữ liệu: Tạo dữ liệu ngẫu nhiên, load từ CSV, hoặc sử dụng Iris dataset (2D để dễ visualize).
- Triển khai K-Means: Từ scratch với các bước khởi tạo tâm, gán nhãn, cập nhật tâm, và kiểm tra hội tụ.
- Visualize: Vẽ đồ thị dữ liệu ban đầu, kết quả phân cụm, và so sánh với nhãn thực tế.
- Đánh giá: Tính Adjusted Rand Index (ARI), Confusion Matrix, và gợi ý mapping cụm.
- Lưu trữ: Tự động lưu file CSV (dữ liệu), PNG (hình ảnh), và TXT (metrics) vào thư mục results/.

## Yêu Cầu Hệ Thống

- Python: 3.8 trở lên.
- Thư viện: Xem file requirements.txt để cài đặt.

## Cài Đặt

1. Clone hoặc tải dự án về máy:
```
git clone <repo-url>  # Nếu từ Git
# Hoặc tải ZIP và giải nén
```
2. Tạo môi trường ảo (khuyến nghị):
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
# Hoặc venv\Scripts\activate  # Windows
```
3. Cài đặt thư viện:
```
pip install -r requirements.txt
```
## Hướng Dẫn Sử Dụng
### Chạy Dự Án
Chạy file chính:
```
python main.py
```
- Chương trình sẽ hỏi lựa chọn dữ liệu (1: Ngẫu nhiên, 2: CSV, 3: Iris).
- Nhập số lượng điểm/cụm nếu cần.
- Chương trình sẽ:
    - Tải và visualize dữ liệu ban đầu (lưu vào results/).
    - Chạy K-Means (verbose để xem từng bước).
    - Visualize kết quả (lưu PNG).
    - Đánh giá nếu có nhãn thực tế (lưu metrics TXT).

### Ví Dụ Chạy Với Iris (K=3)
- Chọn 3 → Nhập K=3.
- Kết quả: Phân cụm 3 loài hoa, ARI ~0.5-0.7, lưu file so sánh.

### Tùy Chỉnh
- Thay đổi K: Nhập khi hỏi.
- Dữ liệu CSV: Tạo file data.csv với cột x,y.
- Không verbose: Gọi model.fit(X, verbose=False) trong main.py.

## Cấu Trúc Thư Mục
Dự án được tổ chức theo cấu trúc modular đơn giản, với mã nguồn chính ở thư mục gốc và thư mục results/ được tạo tự động khi chạy. Dưới đây là cây thư mục đầy đủ (bao gồm file mẫu sau khi chạy một lần):
```
BaiHTuan5 Kmeans/                          # Thư mục gốc dự án
├── data_loader.py                         # Class DataLoader: Tải dữ liệu (ngẫu nhiên, CSV, Iris)
├── kmeans_model.py                        # Class KMeansModel: Triển khai K-Means (fit, evaluate, plot)
├── visualization.py                       # Hàm tiện ích: Vẽ đồ thị và lưu file (scatter, comparison)
├── main.py                                # Script chính: Chạy toàn bộ quy trình
├── requirements.txt                       # Danh sách thư viện cần thiết
├── README.md                              # Tài liệu hướng dẫn này
├── BaoCaoTHCNT_Tuan5.ipynb                # File Jupyter Notebook: Báo cáo chi tiết (tùy chọn, cho demo)
└── results/                               # Thư mục tự tạo (chứa output sau khi chạy)
    ├── generated_data_20251215_143738.csv # File CSV dữ liệu ngẫu nhiên (timestamp)
    ├── initial_data_20251215_143738.png   # Hình ảnh dữ liệu ban đầu
    ├── ket_qua_cuoi_cung_20251215_143740.png # Hình ảnh kết quả phân cụm
    ├── metrics_20251215_143740.txt        # File TXT: Metrics đánh giá (ARI, Confusion Matrix)
    └── comparison_final_20251215_143740.png # Hình ảnh so sánh nhãn thực tế vs K-Means
```
- **Lưu ý về results/:**
    - Thư mục này được tạo tự động khi chạy main.py.
    - Tất cả file có timestamp (YYYYMMDD_HHMMSS) để tránh ghi đè.
    - Nếu chạy nhiều lần, thư mục sẽ chứa nhiều file (có thể xóa thủ công nếu cần).

- **File tùy chọn:**
    - README.md.txt: Bản sao README (có thể đổi tên thành README.md).
    - BaoCaoTHCNT_Tuan5.ipynb: Notebook Jupyter để chạy và demo (tích hợp code từ main.py).

## Lưu Ý & Troubleshooting
- Lỗi Matplotlib: Nếu không hiển thị đồ thị, cài tkinter hoặc chạy trên Jupyter/Colab.
- Lỗi Import: Đảm bảo chạy từ thư mục gốc dự án (python main.py).
- Dữ liệu lớn: K-Means có thể chậm với n_samples > 10k; tăng max_iter nếu cần.
- Không có GUI: Comment plt.show() để chỉ lưu file.
- Mở rộng: Thêm dataset mới bằng cách chỉnh _load_* trong data_loader.py.