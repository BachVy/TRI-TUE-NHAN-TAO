# 🚚 Bài toán Người Bán Hàng Du Lịch (Traveling Salesman Problem – TSP)
## 📌 Giới thiệu

### Dự án này triển khai giải pháp cho Bài toán Người Bán Hàng Du Lịch (Traveling Salesman Problem – TSP) sử dụng thuật toán Nearest Neighbor (Greedy Heuristic).

## 🔍 Mô tả bài toán

TSP yêu cầu tìm một chu trình có chi phí nhỏ nhất:
- Đi qua tất cả các thành phố đúng một lần
- Quay về điểm xuất phát
- Tổng chi phí là nhỏ nhất

🧠 Thuật toán sử dụng: **Nearest Neighbor (Greedy)**
- Bắt đầu từ thành phố 0
- Ở mỗi bước, chọn thành phố chưa thăm gần nhất
- Lặp cho đến khi thăm hết
- Quay về thành phố xuất phát

📎 Đây là một heuristic greedy đơn giản, nhanh, dễ hiểu nhưng không đảm bảo tối ưu toàn cục.

## ✨ Tính năng chính

### 📂 Đọc ma trận khoảng cách từ file TXT hoặc tạo ngẫu nhiên

- Ma trận đối xứng (G[i][j] = G[j][i])

- Đường chéo chính bằng 0

### 🧮 Giải bài toán TSP bằng Nearest Neighbor

### 🖨️ In chi tiết từng bước chọn thành phố và chi phí tích lũy

### 🎞️ Tạo GIF animation minh họa quá trình đi

### 💾 Lưu kết quả vào thư mục results/

## 🛠️ Công nghệ sử dụng

### Ngôn ngữ: Python 3.12

### Thư viện:
- numpy
- networkx
- matplotlib
- pillow (tạo GIF)


## 💻 Yêu cầu hệ thống

### Python 3.8+

### Các thư viện được liệt kê trong requirements.txt

## 📦 Cài đặt
### 1️⃣ Clone hoặc tải project
```
git clone <repo-url>
cd TSP_Project
```
### 2️⃣ Cài đặt thư viện
```
pip install -r requirements.txt
```
Hoặc cài thủ công:
```
pip install numpy networkx matplotlib pillow
```
## 📁 Cấu trúc dự án
```
TSP_Project/
├── main.py                     # File chính (hàm main)
├── matrix_handler.py           # Xử lý ma trận (đọc file, tạo random, lưu)
├── tsp_algorithm.py            # Thuật toán Nearest Neighbor (greedy)
├── tsp_result.py               # Dataclass lưu đường đi và chi phí
├── tsp_visualizer.py           # Tạo animation GIF
├── requirements.txt            # Danh sách thư viện
└── results/                    # Thư mục lưu kết quả
    ├── random_dist_matrix.txt  # Ma trận ngẫu nhiên (nếu dùng random)
    └── tsp_animation.gif       # GIF mô phỏng đường đi
```
## ▶️ Hướng dẫn sử dụng
Chạy chương trình
```
python main.py
```
### Nhập dữ liệu

Nhập đường dẫn file TXT chứa ma trận khoảng cách
hoặc nhập random để tạo ma trận ngẫu nhiên

Nếu chọn random:

- Nhập số thành phố n

- Khuyến nghị: n ≤ 20 để chạy nhanh

## 📤 Kết quả đầu ra
### Console

In từng bước:
- Thành phố được chọn
- Chi phí từng bước
- Chi phí tích lũy
- In đường đi cuối cùng và tổng chi phí

### File
- results/random_dist_matrix.txt: ma trận ngẫu nhiên (nếu tạo)
- results/tsp_animation.gif: animation từng bước

### 🎞️ GIF:
Mỗi frame thêm một cạnh
Tiêu đề hiển thị:
```
Bước 2: 0 -> 1 -> 3 (Chi phí tích lũy: 25.5)
```
## 🧪 Ví dụ chạy
```
Nhập đường dẫn file ma trận khoảng cách (TXT) hoặc 'random': random
Nhập số thành phố (n, khuyến nghị ≤20): 4
Tạo và lưu ma trận vào 'results/random_dist_matrix.txt'.

--- Nearest Neighbor từng bước ---
Bước 1: Từ 0 đến 2 (chi phí 23.0, tích lũy 23.0)
Bước 2: Từ 2 đến 1 (chi phí 35.0, tích lũy 58.0)
Bước 3: Từ 1 đến 3 (chi phí 25.0, tích lũy 83.0)
Quay về 0: +6.5 (tổng 89.5)

Đường đi: 0 -> 2 -> 1 -> 3 -> 0
Chi phí min: 89.50
```
## 📄 Ví dụ file ma trận TXT
```
0 10 15 20
10 0 35 25
15 35 0 30
20 25 30 0
```
## ⚙️ Triển khai thuật toán
### Nearest Neighbor (Greedy Heuristic)
Các bước:
1. Bắt đầu từ thành phố 0
2. Đánh dấu đã thăm
3. Lặp n-1 lần:
- Chọn thành phố chưa thăm gần nhất
- Quay về thành phố 0
- Tính tổng chi phí

## ⚠️ Lưu ý

1. Hiệu suất: Phù hợp n nhỏ

2. Ma trận:
- Đối xứng
- Đường chéo = 0

3. GIF lỗi:
```
pip install pillow
```