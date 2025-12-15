# TRÍ TUỆ NHÂN TẠO – BÀI TẬP & BÁO CÁO

### Họ và tên: Bạch Ngọc Vy
### MSSV: 2001231067
Repository này chứa các bài tập và báo cáo môn **Trí tuệ nhân tạo**, bao gồm
các thuật toán tìm kiếm, tối ưu và phân cụm, được cài đặt bằng Python.

---

## 📁 Cấu trúc thư mục
```
TTRI-TUE-NHAN-TAO/
│
├─ BaoCao_DoAn/
│ ├─ BaiTHTuan02_AStar_TSP/
│ │ ├─ results/
│ │ ├─ astar.py
│ │ ├─ graph.py
│ │ ├─ main.py
│ │ ├─ points.py
│ │ ├─ README.md
│ │ ├─ requirements.txt
│ │ ├─ runner.py
│ │ ├─ solver.py
│ │ └─ visualizer.py
│ │
│ ├─ BaiTHTuan04_TMDT_TSP/
│ │ ├─ results/
│ │ ├─ BaiTHTuan04_TMDT_TSP.ipynb
│ │ ├─ main.py
│ │ ├─ matrix_handler.py
│ │ ├─ README.md
│ │ ├─ requirements.txt
│ │ ├─ tsp_algorithm.py
│ │ └─ tsp_result.py
│ │
│ └─ BaiTHTuan05_Kmeans/
│   ├─ results/
│   ├─ data_loader.py
│   ├─ kmeans_model.py
│   ├─ main.py
│   ├─ README.md
│   ├─ requirements.txt
│   └─ visualization.py
│
└─ BaoCaoTuan_TrenLop/
  ├─ BaoCao_TTNT_Tuan04.ipynb
  ├─ BaoCaoTTNT_Buoi03.ipynb
  └─ TTNT_Tuan03.ipynb
```
---

## 📌 Mô tả chi tiết

### 🔹 `BaoCao_DoAn/`
Chứa các bài thực hành và đồ án dùng để báo cáo kết thúc môn.

#### BaiTHTuan02_AStar_TSP/
Cài đặt bài toán Travelling Salesman Problem (TSP) sử dụng thuật toán A*.
- `astar.py` : Cài đặt thuật toán A*
- `graph.py` : Biểu diễn đồ thị
- `main.py` : Chương trình chính
- `points.py`: Khởi tạo tập điểm
- `runner.py`: Chạy thử nghiệm
- `solver.py`: Giải quyết bài toán
- `visualizer.py`: Trực quan hóa quá trình tìm kiếm
- `results/`: Lưu kết quả chạy và hình ảnh minh họa
- `README.md`: Hướng dẫn chi tiết
- `requirements.txt`: Danh sách thư viện yêu cầu

#### BaiTHTuan04_TMDT_TSP/
Bài thực hành liên quan đến tối ưu TSP (theo nội dung tuần 4).
- `BaiTHTuan04_TMDT_TSP.ipynb`: Notebook chính với code và phân tích
- `main.py`: Chương trình chính
- `matrix_handler.py`: Xử lý ma trận khoảng cách
- `tsp_algorithm.py`: Cài đặt thuật toán TSP
- `tsp_result.py`: Xử lý và hiển thị kết quả
- `results/`: Lưu kết quả chạy
- `README.md`: Hướng dẫn chi tiết
- `requirements.txt`: Danh sách thư viện yêu cầu

#### BaiTHTuan05_Kmeans/
Cài đặt và thử nghiệm thuật toán K-means clustering.
- `data_loader.py`: Tải và xử lý dữ liệu
- `kmeans_model.py`: Mô hình K-means
- `main.py`: Chương trình chính
- `visualization.py`: Trực quan hóa kết quả phân cụm
- `results/`: Lưu kết quả chạy và hình ảnh
- `README.md`: Hướng dẫn chi tiết
- `requirements.txt`: Danh sách thư viện yêu cầu

---

### 🔹 `BaoCaoTuan_TrenLop/`
Chứa các báo cáo Jupyter Notebook trình bày nội dung lý thuyết và thực hành trên lớp.

- `TTNT_Tuan03.ipynb` : Nội dung tuần 3
- `BaoCaoTTNT_Buoi03.ipynb` : Báo cáo buổi 3
- `BaoCao_TTNT_Tuan04.ipynb` : Báo cáo tuần 4

---

## 🛠 Công cụ sử dụng
- Python 3
- Jupyter Notebook / Google Colab
- VS Code
- Git & GitHub
- Thư viện: `numpy`, `matplotlib`, `networkx` (tuỳ bài)

---

## ▶️ Hướng dẫn chạy

### Với file `.py`
```
cd BaoCao_DoAn/BaiTHTuan02_AStar_TSP/  # Hoặc thư mục tương ứng
pip install -r requirements.txt
python main.py
```
### Với file .ipynb
- Mở bằng Google Colab hoặc VS Code (Jupyter Extension)
- Chạy các cell theo thứ tự từ trên xuống
## 📊 Kết quả
- Trực quan quá trình tìm kiếm / hội tụ của thuật toán
- Đồ thị biểu diễn kết quả cuối cùng

