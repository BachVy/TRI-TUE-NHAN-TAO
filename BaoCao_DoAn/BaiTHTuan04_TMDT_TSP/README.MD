# Triển Khai Thuật Toán Nearest Neighbor Cho TSP
## Giới Thiệu
Dự án này triển khai thuật toán Nearest Neighbor (Heuristic Greedy) cho bài toán Người Bán Hàng Du Lịch (Traveling Salesman Problem - TSP) theo lập trình hướng đối tượng (OOP) bằng Python. Nó hỗ trợ tải ma trận khoảng cách từ file TXT hoặc tạo ngẫu nhiên, thực hiện giải TSP, visualize kết quả qua animation GIF và in từng bước greedy.

### Tính Năng Chính
- Tải ma trận: Tạo ma trận khoảng cách ngẫu nhiên hoặc load từ file TXT.
- Triển khai Nearest Neighbor: Từ scratch với các bước chọn thành phố gần nhất chưa thăm, tính chi phí tích lũy và quay về điểm xuất phát.
- Visualize: Tạo animation GIF hiển thị đường đi từng bước với chi phí tích lũy.
- In từng bước: Hiển thị verbose cho greedy steps.
- Lưu trữ: Tự động lưu ma trận TXT và GIF vào thư mục results/.

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
:
```python -m venv venv
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
- Chương trình sẽ hỏi đường dẫn file ma trận (TXT) hoặc 'random'.
- Nếu random, nhập số thành phố n (khuyến nghị ≤20).
- Chương trình sẽ:
    - Tải và in ma trận khoảng cách (lưu vào results/ nếu random).
    - Chạy Nearest Neighbor (verbose để xem từng bước chọn thành phố).
    - Tạo và lưu animation GIF (từng bước đường đi với chi phí tích lũy).

### Ví Dụ Chạy Với Random (n=4)
- Nhập 'random' → Nhập n=4.
- Kết quả: Đường đi greedy (e.g., 0 -> 2 -> 1 -> 3 -> 0), chi phí ~89.5, lưu GIF.

### Tùy Chỉnh
- Thay đổi n: Nhập khi hỏi (lớn hơn cho test heuristic).
- Ma trận từ file: Tạo file matrix.txt với ma trận symmetric (e.g., 0 10 15\n10 0 35...).
- Không verbose: Gọi TSPAlgorithm(verbose=False) trong main.py.

## Cấu Trúc Thư Mục
Dự án được tổ chức theo cấu trúc modular đơn giản, với mã nguồn chính ở thư mục gốc và thư mục results/ được tạo tự động khi chạy. Dưới đây là cây thư mục đầy đủ (bao gồm file mẫu sau khi chạy một lần):
```
BaiHTTuan04_TMDT_TSP/                       # Thư mục gốc dự án
├── main.py                                 # Script chính: Chạy toàn bộ quy trình
├── matrix_handler.py                       # Class MatrixHandler: Tải ma trận (file/random), lưu file
├── tsp_algorithm.py                        # Class TSPAlgorithm: Triển khai Nearest Neighbor (greedy)
├── tsp_result.py                           # Dataclass TSPResult: Lưu kết quả (chi phí và đường đi)
├── tsp_visualizer.py                       # Class TSPVisualizer: Tạo animation GIF
├── requirements.txt                        # Danh sách thư viện cần thiết
├── README.md                               # Tài liệu hướng dẫn này
└── results/                                # Thư mục tự tạo (chứa output sau khi chạy)
    ├── random_dist_matrix.txt              # File TXT ma trận khoảng cách ngẫu nhiên
    └── tsp_animation.gif                   # Animation GIF đường đi TSP (từng bước)
```
- **Lưu ý về results/:**
    - Thư mục này được tạo tự động khi chạy main.py.
    - Ma trận chỉ lưu nếu dùng random (không ghi đè).
    - GIF luôn lưu với tên cố định; xóa thủ công nếu chạy nhiều lần.

- **File tùy chọn:**
    - README.md.txt: Bản sao README (có thể đổi tên thành README.md).


## Lưu ý & Troubleshooting
- Lỗi Matplotlib/Pillow: Nếu không lưu GIF, kiểm tra pip install pillow matplotlib và chạy trên môi trường GUI (không headless).
- Lỗi Import: Đảm bảo chạy từ thư mục gốc dự án (python main.py).
- Ma trận không symmetric: Code vẫn chạy nhưng kết quả có thể không chính xác, kiểm tra input.
- Hiệu suất: Nhanh cho n lớn nhưng heuristic không luôn tối ưu.
- Không GUI: Comment plt.show() trong tsp_visualizer.py chỉ lưu file.
- Mở rộng: Thêm cải thiện 2-opt bằng cách chỉnh solve() trong tsp_algorithm.py.