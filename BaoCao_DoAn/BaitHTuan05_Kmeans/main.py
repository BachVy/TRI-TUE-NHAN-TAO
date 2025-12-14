import numpy as np
from data_loader import DataLoader
from kmeans_model import KMeansModel
from visualization import plot_and_save_scatter
from datetime import datetime
import os 

if __name__ == "__main__":
    np.random.seed(42)

    # Instantiate DataLoader
    loader = DataLoader()

    # --- Start of fix: Monkey-patching the _plot_and_save_initial_data method --- 
    def _fixed_plot_and_save_initial_data(self):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        title = 'Dữ liệu ban đầu (màu theo nhãn thực tế)' if self.is_iris and self.true_labels is not None else 'Dữ liệu ban đầu'
        marker = 'o'
        s = 10

        c = 'blue'
        cmap = None
        if self.is_iris and self.true_labels is not None:
            c = self.true_labels
            cmap = 'viridis'

        # Prepare the 'scatters' argument for visualization.plot_and_save_scatter
        # This will be the main data points to plot
        initial_scatter_data_args = {
            'c': c,
            'marker': marker,
            's': s,
            'cmap': cmap
        }
        scatters_list = [(self.X[:, 0], self.X[:, 1], initial_scatter_data_args)]

        # Call the plot_and_save_scatter function with correct keyword arguments
        plot_and_save_scatter(
            scatters=scatters_list,
            centers_scatter=None, 
            overlay=None,         
            title=title,
            xlabel=self.xlabel,
            ylabel=self.ylabel,
            filename_prefix=f'initial_data_{timestamp}'
        )

    # Apply the monkey-patch
    loader._plot_and_save_initial_data = _fixed_plot_and_save_initial_data.__get__(loader, DataLoader)
    # --- End of fix ---

    # Now call the load_data method, which will use the monkey-patched function
    loader.load_data()
    X = loader.X
    true_labels = loader.true_labels
    n_cluster = loader.n_cluster
    xlabel = loader.xlabel
    ylabel = loader.ylabel

    # Chạy K-Means
    model = KMeansModel(n_cluster)
    model.fit(X, verbose=True)

    # Vẽ và lưu kết quả
    model.plot_and_save_results(true_labels, xlabel, ylabel)

    # Đánh giá nếu có nhãn thực tế
    model.evaluate_and_save(true_labels, xlabel, ylabel)
