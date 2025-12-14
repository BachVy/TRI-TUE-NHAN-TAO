import numpy as np
from scipy.spatial.distance import cdist
from sklearn.metrics import adjusted_rand_score, confusion_matrix
from datetime import datetime
import matplotlib.pyplot as plt
from visualization import plot_and_save_scatter, plot_and_save_comparison

class KMeansModel:
    """
    Lớp triển khai thuật toán K-Means (không visualize từng bước, chỉ fit với verbose).
    """
    def __init__(self, n_clusters, max_iter=100, tolerance=1e-4, seed=42):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.tolerance = tolerance
        self.seed = seed
        np.random.seed(seed)
        self.centers = None
        self.labels = None
        self.iterations = 0
        self.X = None  

    def _init_centers(self, X):
        indices = np.random.choice(X.shape[0], self.n_clusters, replace=False)
        return X[indices]

    def _predict_labels(self, X, centers):
        D = cdist(X, centers)
        return np.argmin(D, axis=1)

    def _update_centers(self, X, labels):
        centers = np.zeros((self.n_clusters, X.shape[1]))
        for k in range(self.n_clusters):
            Xk = X[labels == k, :]
            if len(Xk) > 0:
                centers[k] = np.mean(Xk, axis=0)
            else:
                centers[k] = X[np.random.choice(X.shape[0])]
        return centers

    def _has_converged(self, centers, new_centers):
        return np.all(np.abs(centers - new_centers) < self.tolerance)

    def fit(self, X, verbose=True):
        self.X = X  
        init_centers = self._init_centers(X)
        labels = np.zeros(X.shape[0], dtype=int)
        centers = init_centers.copy()

        if verbose:
            print("=== BƯỚC 1: KHỞI TẠO TÂM CỤM NGẪU NHIÊN ===")
            for i, center in enumerate(centers):
                print(f"  Tâm {i}: {center}")

        self.iterations = 0
        while self.iterations < self.max_iter:
            self.iterations += 1
            if verbose:
                print(f"\n--- Lần lặp {self.iterations} ---")

            old_labels = labels.copy()
            labels = self._predict_labels(X, centers)
            num_changes = np.sum(labels != old_labels)
            if verbose:
                print(f"  Gán nhãn: {np.bincount(labels, minlength=self.n_clusters)} điểm mỗi cụm")
                print(f"  Số điểm thay đổi nhãn: {num_changes}")

            new_centers = self._update_centers(X, labels)
            if verbose:
                print("  Tâm cụm mới:")
                for i, center in enumerate(new_centers):
                    print(f"    Tâm {i}: {center}")

            if self._has_converged(centers, new_centers):
                if verbose:
                    print(f"  → Hội tụ! Không thay đổi đáng kể (ngưỡng {self.tolerance}).")
                centers = new_centers
                break
            centers = new_centers

        if self.iterations >= self.max_iter and verbose:
            print(f"  → Đạt tối đa {self.max_iter} lần lặp mà chưa hội tụ.")

        self.centers = centers
        self.labels = labels

        if verbose:
            print(f"\n=== BƯỚC 3: KẾT QUẢ CUỐI CÙNG ===")
            print(f"Thuật toán hội tụ sau {self.iterations} lần lặp.")
            print("Phân bố nhãn cuối:")
            print(np.bincount(labels, minlength=self.n_clusters))
            print("Tâm cụm cuối:")
            for i, center in enumerate(centers):
                print(f"  Tâm {i}: {center}")

        return self

    def plot_and_save_results(self, true_labels=None, xlabel='x', ylabel='y'):
        """
        Vẽ và lưu ảnh kết quả cuối cùng.
        """
        # Chuẩn bị dữ liệu cho scatter: Tách cụm và tâm
        scatters = []
        for i in range(self.n_clusters):
            data = self.X[self.labels == i]
            scatters.append((data[:, 0], data[:, 1], {'color': 'b', 'marker': 'o', 's': 30, 'alpha': 0.7, 'label': f'Cụm {i} ({len(data)} điểm)'}))
        centers_scatter = [(self.centers[i][0], self.centers[i][1], {'color': 'r', 'marker': 'x', 's': 200, 'linewidth': 3, 'edgecolors': 'black', 'label': f'Tâm {i}'}) for i in range(self.n_clusters)]
        overlay = (self.X[:, 0], self.X[:, 1], {'c': true_labels, 'marker': '*', 's': 50, 'alpha': 0.4, 'cmap': 'viridis', 'label': 'Nhãn thực tế'}) if true_labels is not None else None
        plot_and_save_scatter(scatters, centers_scatter, overlay, 'Kết quả cuối cùng', xlabel, ylabel, 'ket_qua_cuoi_cung')

    def evaluate_and_save(self, true_labels=None, xlabel='x', ylabel='y'):
        """
        Đánh giá với nhãn thực tế nếu có và lưu metrics.
        """
        if true_labels is None:
            print("\nKhông có nhãn thực tế để so sánh (dữ liệu ngẫu nhiên hoặc CSV).")
            return

        print("\n=== BƯỚC 4: SO SÁNH VỚI NHÃN THỰC TẾ ===")
        # Adjusted Rand Index
        ari = adjusted_rand_score(true_labels, self.labels)
        print(f"Adjusted Rand Index (ARI): {ari:.4f} (gần 1 là tốt, 0 là ngẫu nhiên)")

        # Confusion Matrix
        cm = confusion_matrix(true_labels, self.labels)
        print("Confusion Matrix (hàng: nhãn thực, cột: cụm dự đoán):")
        print(cm)

        # Mapping gợi ý
        print("Gợi ý mapping cụm dự đoán sang nhãn thực (dựa trên đa số):")
        species = ['setosa', 'versicolor', 'virginica']
        for i in range(self.n_clusters):
            cluster_true = true_labels[self.labels == i]
            if len(cluster_true) > 0:
                majority = np.bincount(cluster_true).argmax()
                count = np.bincount(cluster_true)[majority]
                species_name = species[majority] if majority < len(species) else 'N/A'
                print(f"  Cụm {i} → Nhãn thực {majority} ({species_name}): {count}/{len(cluster_true)} điểm")

        # Lưu metrics vào file TXT
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        metrics_file = f'results/metrics_{timestamp}.txt'
        with open(metrics_file, 'w') as f:
            f.write(f"ARI: {ari:.4f}\n")
            f.write("Confusion Matrix:\n" + str(cm) + "\n")
        print(f"Lưu metrics vào: {metrics_file}")

        # Vẽ và lưu ảnh so sánh
        plot_and_save_comparison(self.X, true_labels, self.labels, xlabel, ylabel)
