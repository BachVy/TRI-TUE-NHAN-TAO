# Triển Khai Thuật Toán A* Cho Biến Thể TSP (Người Giao Hàng) Và Trực Quan Hóa
## Giới Thiệu
Dự án này triển khai thuật toán A* (A-star) triển khai theo lập trình hướng đối tượng (OOP) bằng Python để giải quyết biến thể của bài toán Người Du Hành (TSP - Traveling Salesman Problem). Nó tập trung vào đường đi mở từ kho (điểm 0) thăm tất cả các điểm giao hàng, sử dụng heuristic admissible để đảm bảo tối ưu. Hệ thống hỗ trợ tải dữ liệu từ file JSON hoặc tạo ngẫu nhiên, thực hiện tìm kiếm và trực quan hóa quá trình từng bước qua GIF animation và đồ thị kết quả.

## Tính Năng Chính
- Tải dữ liệu: Tạo điểm ngẫu nhiên (kho cố định tại (0,0), các điểm khác trong [0,5]x[0,5]), hoặc load từ file JSON.
- Triển khai A*: Sử dụng bitmask cho visited, priority queue (heapq) cho f = g + h, heuristic min_dist * (remaining / 2) để hướng dẫn tìm kiếm.
- Visualize: Vẽ từng bước (path tạm, queue top 3), tạo GIF animation (tốc độ tùy chỉnh), và đồ thị kết quả cuối (path xanh, chi phí).
- Lưu trữ: Tự động lưu file JSON (điểm), PNG (hình ảnh step/final), và GIF vào thư mục results/.

## Yêu Cầu Hệ Thống
- Python: 3.8 trở lên.
- Thư viện: Xem file requirements.txt để cài đặt.

### Cài Đặt
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

- Chương trình sẽ hỏi lựa chọn dữ liệu (load từ file JSON hoặc tạo ngẫu nhiên).
- Nếu tạo ngẫu nhiên: Nhập số lượng điểm (n, mặc định 5, max 12).
- Chương trình sẽ:
    - Tải và tạo điểm (lưu JSON vào results/).
    - Chạy A* (verbose để xem từng bước: pop nút, mở rộng, queue f).
    - Visualize từng bước (lưu PNG tạm), tạo GIF animation.
    - Vẽ kết quả cuối (lưu PNG) và dọn dẹp frames tạm.
    - In danh sách file trong results/.


### Ví Dụ Chạy Với Tạo Ngẫu Nhiên (n=5)
- Chọn "random" → Nhập n=5.
- Kết quả: Path ví dụ [0, 2, 4, 1, 3], chi phí ~10-15 (tùy random), GIF hiển thị 5-6 bước A*, lưu file trong results/.

### Tùy Chỉnh

- Thay đổi n: Nhập khi hỏi (max 12 để tránh chậm).
- Tốc độ GIF: Chỉnh duration trong visualizer.py (mặc định 8.5s/frame để chậm, dễ quan sát).
- Load file: Tạo file JSON với format [{"index":0,"x":0,"y":0}, ...] và nhập đường dẫn.
- Không verbose: Chỉnh print trong solver.py hoặc tăng max_steps trong main.py.

## Cấu Trúc Thư Mục
Dự án được tổ chức theo cấu trúc modular đơn giản, với mã nguồn chính ở thư mục gốc và thư mục results/ được tạo tự động khi chạy. Dưới đây là cây thư mục đầy đủ (bao gồm file mẫu sau khi chạy một lần):
```
BaiHTuan02 Astar TSP/                      # Thư mục gốc dự án
├── points.py                              # Class Point và hàm utility: generate_random_points, get_distance_matrix
├── graph.py                               # Class TSPGraph: Mô hình đồ thị, heuristic, neighbors
├── solver.py                              # Class AStarSolver: Triển khai A* (solve_with_visual, calc_f)
├── visualizer.py                          # Class Visualizer: Vẽ step, tạo GIF, plot final, cleanup
├── runner.py                              # Class TSPRunner: Quản lý flow (interactive choice, run)
├── main.py                                # Script chính: Chạy toàn bộ quy trình
├── requirements.txt                       # Danh sách thư viện cần thiết
├── README.md                              # Tài liệu hướng dẫn này
├── BaiHTuan02 Astar TSP.ipynb             # File Jupyter Notebook: Báo cáo chi tiết (tùy chọn, cho demo)
└── results/                               # Thư mục tự tạo (chứa output sau khi chạy)
    ├── a_star_tsp.gif                     # GIF animation từng bước A*
    ├── final_result.png                   # Hình ảnh kết quả cuối (path xanh, chi phí)
    └── random_points_12.json              # File JSON dữ liệu điểm ngẫu nhiên (n=12)
```
- **Lưu ý về results/:**
- Thư mục này được tạo tự động khi chạy main.py.
- Tất cả file không có timestamp (ghi đè nếu chạy lại), nhưng có thể chỉnh để thêm (ví dụ: trong runner.py).
- Nếu chạy nhiều lần, thư mục sẽ chứa file mới (có thể xóa thủ công nếu cần).

- **File tùy chọn:**
- README.md.txt: Bản sao README (có thể đổi tên thành README.md).
- BaiHTuan02 Astar TSP.ipynb: Notebook Jupyter để chạy và demo (tích hợp code từ main.py).

## Lưu ý & Troubleshooting
- Lỗi Matplotlib: Nếu không lưu PNG/GIF, cài backend Agg (matplotlib.use('Agg')) hoặc chạy trên Jupyter/Colab.
- Lỗi Import: Đảm bảo chạy từ thư mục gốc dự án (python main.py).
- n lớn: A* chậm với n > 10, tăng max_steps nếu cần, nhưng giới hạn 12.
- Không có GUI: Code chỉ lưu file (không plt.show()).
- Mở rộng: Thêm quay về kho bằng cách + dist[path[-1]][0] trong solver.py; thay heuristic trong graph.py.