import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
import os
from datetime import datetime
import matplotlib.pyplot as plt
from visualization import plot_and_save_scatter 

class DataLoader:
    """
    Lớp tải dữ liệu từ các nguồn khác nhau.
    """
    def __init__(self):
        self.X = None
        self.true_labels = None
        self.n_cluster = None
        self.is_iris = False
        self.xlabel = 'x'
        self.ylabel = 'y'

    def load_data(self):
        """
        Tải dữ liệu dựa trên lựa chọn của người dùng và xử lý lưu trữ.
        """
        print("Các chế độ tạo dữ liệu:")
        print("1. Tạo ngẫu nhiên (nhập số điểm và cụm)")
        print("2. Load từ file CSV (chứa cột 'x' và 'y')")
        print("3. Load dataset thực tế: Iris (sử dụng 2 đặc trưng đầu để visualize 2D)")
        choice = input("Nhập lựa chọn (1, 2, hoặc 3): ").strip()

        # Tạo thư mục results
        os.makedirs('results', exist_ok=True)
        print("Thư mục 'results/' đã sẵn sàng.")

        if choice == '1':
            self._load_random()
        elif choice == '2':
            self._load_csv()
        elif choice == '3':
            self._load_iris()
        else:
            print("Lựa chọn không hợp lệ. Sử dụng Iris dataset mặc định.")
            self._load_iris()

        # Visualize và lưu dữ liệu ban đầu
        self._plot_and_save_initial_data()

    def _load_random(self):
        n_samples_total = int(input("Nhập tổng số lượng điểm dữ liệu (ví dụ: 500): "))
        self.n_cluster = int(input("Nhập số lượng cụm (K) (ví dụ: 3): "))

        # Tạo tâm cụm mẫu
        if self.n_cluster == 3:
            means = [[2, 2], [9, 2], [4, 9]]
        else:
            np.random.seed(42)
            means = np.random.uniform(0, 10, (self.n_cluster, 2)).tolist()
            print(f"Tạo {self.n_cluster} tâm cụm ngẫu nhiên: {means}")

        cov = [[2, 0], [0, 2]]

        # Tạo dữ liệu
        n_samples_per_cluster = n_samples_total // self.n_cluster
        remainder = n_samples_total % self.n_cluster
        X_list = []
        for i in range(self.n_cluster):
            current_samples = n_samples_per_cluster + (1 if i < remainder else 0)
            Xi = np.random.multivariate_normal(means[i], cov, current_samples)
            X_list.append(Xi)
        self.X = np.concatenate(X_list, axis=0)
        print(f"Tạo dữ liệu ngẫu nhiên: {self.X.shape[0]} điểm trong {self.n_cluster} cụm.")

        # Lưu file CSV
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        df = pd.DataFrame(self.X, columns=['x', 'y'])
        df.to_csv(f'results/generated_data_{timestamp}.csv', index=False)
        print(f"Lưu dữ liệu vào results/generated_data_{timestamp}.csv")

    def _load_csv(self):
        file_path = input("Nhập đường dẫn file CSV (ví dụ: data.csv): ").strip()
        try:
            df = pd.read_csv(file_path)
            self.X = df[['x', 'y']].values  
            print(f"Load dữ liệu từ file: {self.X.shape[0]} điểm.")
        except Exception as e:
            print(f"Lỗi khi load file: {e}. Sử dụng dữ liệu mẫu mặc định.")
            self.X = np.random.rand(100, 2) * 10
            print("Sử dụng dữ liệu mẫu: 100 điểm ngẫu nhiên.")

        self.n_cluster = int(input("Nhập số lượng cụm (K) (ví dụ: 3): "))

    def _load_iris(self):
        iris = load_iris()
        self.X = iris.data[:, :2]  
        self.true_labels = iris.target  
        self.is_iris = True
        self.xlabel = 'Đặc trưng 1 (sepal length)'
        self.ylabel = 'Đặc trưng 2 (sepal width)'
        print(f"Load Iris dataset: {self.X.shape[0]} điểm, 2 đặc trưng (sepal length, sepal width).")
        print("Nhãn thực tế: 0=setosa, 1=versicolor, 2=virginica.")
        print("Gợi ý: K=3 cho 3 loài hoa.")
        self.n_cluster = int(input("Nhập số lượng cụm (K) (ví dụ: 3): "))

    def _plot_and_save_initial_data(self):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        title = 'Dữ liệu ban đầu (màu theo nhãn thực tế)' if self.is_iris and self.true_labels is not None else 'Dữ liệu ban đầu'
        marker = 'o'
        s = 10

        if self.is_iris and self.true_labels is not None:
            c = self.true_labels
            cmap = 'viridis'
        else:
            c = 'blue'
            cmap = None

        plot_and_save_scatter(self.X, c, title, self.xlabel, self.ylabel, marker, s, cmap, f'initial_data_{timestamp}')
