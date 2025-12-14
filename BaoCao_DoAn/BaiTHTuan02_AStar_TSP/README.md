# 🗺️ Giải Quyết Bài Toán Người Du Lịch (TSP) bằng Thuật Toán A*

 Đây là project Python triển khai thuật toán tìm kiếm tối ưu A\* để giải quyết
phiên bản đơn giản của **Bài toán Người Du Lịch (Traveling Salesperson Problem – TSP)**.

Bài toán đặt ra là:  
> Tìm đường đi ngắn nhất bắt đầu từ điểm kho (node 0), đi qua tất cả các điểm còn lại, không bắt buộc quay về kho (TSP Path).
---

## 🚀 Cấu trúc project
```
BaiTHTuan02_AStar_TSP/
├── results/ # Lưu kết quả (ảnh, GIF)
├── astar.py # Lớp AStarSolver: cài đặt thuật toán A*
├── graph.py # Lớp TSPGraph: đồ thị và heuristic
├── main.py # Chương trình chính
├── points.py # Sinh điểm, tính khoảng cách
└── visualizer.py # Trực quan hóa quá trình và kết quả
```
---

## 🛠️ Yêu cầu & cài đặt

Project sử dụng các thư viện Python sau:

- `numpy`
- `matplotlib`
- `imageio`

Cài đặt bằng lệnh:

```
pip install numpy matplotlib imageio
```
## 🧠 Các thành phần chính
---
### 1️⃣ points.py
- Định nghĩa lớp Point với tọa độ $(x, y)$ và chỉ mục.
- Tạo n điểm ngẫu nhiên.
- Điểm 0 cố định tại $(0, 0)$ (đóng vai trò kho).
- Tính ma trận khoảng cách Euclidean giữa mọi cặp điểm.
---
### 2️⃣ graph.py
Lớp TSPGraph: biểu diễn đồ thị TSP.

Thuộc tính dist: ma trận khoảng cách.

Hàm heuristic khả chấp (admissible):

- $h = \min\_dist \times \frac{\text{remaining}}{2}$


Trong đó:

- $\min_dist$: khoảng cách ngắn nhất từ điểm hiện tại đến một điểm chưa thăm
- $\text{remaining}$: số lượng điểm chưa thăm

📌 Heuristic này đảm bảo A* luôn tìm ra nghiệm tối ưu.

- is_goal: kiểm tra xem tất cả các điểm đã được thăm hay chưa.
---
### 3️⃣ astar.py
- Lớp AStarSolver: triển khai thuật toán A* với heapq (priority queue).
- Trạng thái được biểu diễn bởi bộ:

```
(current, visited, g, path)
```
Trong đó:
- current: điểm hiện tại
- visited: bitmask các điểm đã thăm
- g: chi phí thực tế từ kho đến hiện tại
- path: danh sách các điểm đã đi qua

Hàm calc_f:
```
𝑓 = 𝑔 + ℎ
```

- visited_states dùng để lưu chi phí g nhỏ nhất của mỗi trạng thái,
giúp tránh duyệt lại các trạng thái kém hiệu quả.
--- 
### 4️⃣ visualizer.py
- Lớp Visualizer: trực quan hóa quá trình tìm kiếm.
- Ghép các ảnh PNG thành GIF mô phỏng quá trình A*
- Vẽ đường đi tối ưu cuối cùng
- Hiển thị tổng chi phí

🏃 Cách chạy chương trình
Chạy file main.py:

```
python main.py
```
Chương trình chạy tương tác trong terminal.

---
### 🔄 Quá trình tương tác
Khi chạy, chương trình sẽ yêu cầu nhập:

Load từ file JSON điểm? (y/n, mặc định n)

- y: load điểm từ file cũ

- n: tạo điểm mới

Số lượng điểm n (mặc định 5, tối đa 12)

- Khuyến nghị: n ≤ 12

- Sử dụng dữ liệu mặc định? (y/n)

- y: dùng dữ liệu mẫu (n nhỏ)

- n: sinh điểm ngẫu nhiên
---
## 📊 Kết quả
Sau khi chạy xong, các kết quả được lưu trong thư mục results/:
- a_star_tsp.gif
→ GIF mô phỏng quá trình tìm kiếm của A*
- final_result.png
→ Đồ thị kết quả cuối cùng (đường đi + tổng chi phí)
- random_points_n.json
→ File JSON lưu các điểm đã sinh (nếu dùng điểm ngẫu nhiên)
---
## ⚠️ Lỗi thường gặp & cách khắc phục
### ❌ Không tìm thấy thư viện
Lỗi:
```
ModuleNotFoundError: No module named 'imageio'
```
Khắc phục:
```
pip install numpy matplotlib imageio
```
### ❌ Chạy quá lâu / treo chương trình
Nguyên nhân:

- Số điểm n quá lớn

Giải pháp:

- Giảm số điểm

- Khuyến nghị: n ≤ 12

### ❌ Lỗi đọc / ghi file JSON
Lỗi:
```
FileNotFoundError: json.JSONDecodeError
```
Khắc phục:
- Kiểm tra đường dẫn file JSON
- Đảm bảo file đúng định dạng

### ❌ Không tạo được GIF
Nguyên nhân:

- Thiếu backend cho imageio

Khắc phục:
```
pip install imageio-ffmpeg
```
## ✅ Ghi chú
- Project tập trung vào minh họa thuật toán A* cho TSP

- Không tối ưu cho dữ liệu lớn