import matplotlib.pyplot as plt
from datetime import datetime
import os

def plot_and_save_scatter(scatters, centers_scatter=None, overlay=None, title='Scatter Plot', xlabel='x', ylabel='y', filename_prefix='plot'):
    """
    Vẽ scatter plot với các lớp dữ liệu, tâm cụm, và overlay (nếu có), sau đó lưu file.
    - scatters: List of (x, y, kwargs) for data points.
    - centers_scatter: List of (x, y, kwargs) for centers.
    - overlay: (x, y, kwargs) for overlay layer.
    """
    plt.figure(figsize=(10, 7))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True, alpha=0.3)

    # Vẽ dữ liệu chính
    for x, y, kwargs in scatters:
        plt.scatter(x, y, **kwargs)

    # Vẽ tâm cụm nếu có
    if centers_scatter:
        for x, y, kwargs in centers_scatter:
            plt.scatter(x, y, **kwargs)

    # Overlay nếu có
    if overlay:
        x, y, kwargs = overlay
        plt.scatter(x, y, **kwargs)

    plt.legend()
    plt.gcf().canvas.flush_events()

    # Lưu file
    os.makedirs('results', exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'results/{filename_prefix}_{timestamp}.png'
    try:
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"Lưu ảnh: {filename}")
    except Exception as e:
        print(f"Lỗi lưu ảnh: {e}")
    plt.show()

def plot_and_save_comparison(X, true_labels, pred_labels, xlabel, ylabel):
    """
    Vẽ và lưu ảnh so sánh nhãn thực tế vs dự đoán.
    """
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.scatter(X[:, 0], X[:, 1], c=true_labels, cmap='viridis', s=50)
    plt.title('Nhãn thực tế')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.subplot(1, 2, 2)
    plt.scatter(X[:, 0], X[:, 1], c=pred_labels, cmap='viridis', s=50)
    plt.title('Cụm K-Means')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.gcf().canvas.flush_events()

    # Lưu file
    os.makedirs('results', exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'results/comparison_final_{timestamp}.png'
    try:
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"Lưu ảnh so sánh: {filename}")
    except Exception as e:
        print(f"Lỗi lưu ảnh so sánh: {e}")
    plt.show()
