import matplotlib.pyplot as plt
import imageio
import os
import shutil
from typing import List, Tuple
from points import Point

class Visualizer:
    def __init__(self, points: List[Point]):
        self.points = points
        self.results_dir = 'results'
        self.frames_dir = 'frames'

    def plot_step(self, step_num: int, current_path: List[int], queue_items: List[Tuple], title: str):
        """Vẽ và lưu PNG cho step vào frames_dir (tạm, không vào results)"""
        if not os.path.exists(self.frames_dir):
            os.makedirs(self.frames_dir)
        plt.figure(figsize=(8, 6))
        # Vẽ điểm
        for i, point in enumerate(self.points):
            color = 'red' if i in current_path else 'blue'
            plt.scatter(point.x, point.y, c=color, s=1000)
            plt.text(point.x, point.y, str(i), fontsize=12, ha='center')
        # Vẽ path
        if len(current_path) > 1:
            for i in range(len(current_path)-1):
                p1 = self.points[current_path[i]]
                p2 = self.points[current_path[i+1]]
                plt.arrow(p1.x, p1.y, p2.x - p1.x, p2.y - p1.y, head_width=0.1, head_length=0.1, fc='red', ec='red')
        # Queue text
        if queue_items:
            queue_text = "Queue top 3 (path, f):\n" + "\n".join(
                f"  {idx+1}: Path={str(state[3])}, f={self._calc_f(state):.2f}" for idx, state in enumerate(queue_items[:3])
            )
            plt.text(0.02, 0.98, queue_text, transform=plt.gca().transAxes, verticalalignment='top',
                     bbox=dict(boxstyle='round', facecolor='wheat'), fontsize=8)
        plt.title(f"A* TSP Step {step_num}: {title}")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.xlim(-1, 5)
        plt.ylim(-1, 5)
        # Lưu tạm vào frames
        png_path = os.path.join(self.frames_dir, f'step_{step_num:03d}.png')
        plt.savefig(png_path, dpi=100, bbox_inches='tight')
        plt.close()
        print(f"Đã lưu step {step_num} (tạm): {png_path}")

    def _calc_f(self, state: Tuple) -> float:
        return 0.0  # Dummy

    def create_gif(self, num_steps: int, duration: float = 1.5):
        """Tạo GIF từ frames_dir và lưu vào results/"""
        if not os.path.exists(self.results_dir):
            os.makedirs(self.results_dir)
        gif_path = os.path.join(self.results_dir, 'a_star_tsp.gif')
        with imageio.get_writer(gif_path, mode='I', duration=duration) as writer:
            for s in range(num_steps + 1):
                frame_path = os.path.join(self.frames_dir, f'step_{s:03d}.png')
                if os.path.exists(frame_path):
                    image = imageio.imread(frame_path)
                    writer.append_data(image)
        print(f"GIF đã được tạo: {gif_path}")

    def plot_final_result(self, path: List[int], cost: float):
        """Vẽ và lưu đồ thị kết quả cuối vào results/"""
        if not os.path.exists(self.results_dir):
            os.makedirs(self.results_dir)
        plt.figure(figsize=(10, 7))
        for i, point in enumerate(self.points):
            plt.scatter(point.x, point.y, c='red', s=1000)
            plt.text(point.x, point.y, str(i), fontsize=14, ha='center', fontweight='bold')
        for i in range(len(path)-1):
            p1 = self.points[path[i]]
            p2 = self.points[path[i+1]]
            plt.arrow(p1.x, p1.y, p2.x - p1.x, p2.y - p1.y, head_width=0.15, head_length=0.15, fc='green', ec='green', linewidth=2)
        plt.text(0.5, -0.1, f"Tổng chi phí: {round(cost, 2)}", transform=plt.gca().transAxes,
                 ha='center', fontsize=16, fontweight='bold', bbox=dict(boxstyle='round', facecolor='lightgreen'))
        plt.title(f"Kết Quả Cuối Cùng: Path Tối Ưu {path} (A* TSP)", fontsize=16, fontweight='bold')
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.xlim(-1, 5)
        plt.ylim(-1, 5)
        final_path = os.path.join(self.results_dir, 'final_result.png')
        plt.savefig(final_path, dpi=150, bbox_inches='tight')
        plt.show() 
        plt.close()
        print(f"Đồ thị kết quả cuối cùng đã được lưu: {final_path}")

    def cleanup(self):
        """Dọn dẹp frames tạm"""
        if os.path.exists(self.frames_dir):
            shutil.rmtree(self.frames_dir)
        print("Đã dọn dẹp frames tạm.")
