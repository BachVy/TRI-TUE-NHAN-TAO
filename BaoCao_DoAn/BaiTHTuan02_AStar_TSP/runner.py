import os
import json
from typing import List, Tuple
from points import Point, generate_random_points
from graph import TSPGraph
from solver import AStarSolver
from visualizer import Visualizer

class TSPRunner:
    """
    Class quản lý toàn bộ flow TSP: Hỏi lựa chọn load/random, setup points, Solve A*, Visualize theo OOP.
    - Luôn hỏi đầu tiên: load file hay tạo random.
    - Nếu load: Hỏi file_path, tự đọc và set n.
    - Nếu random: Hỏi n, generate random points, lưu JSON.
    """

    def __init__(self):
        self.points: List[Point] = []
        self.n: int = 0
        self.dist_matrix: List[List[float]] = []  
        self.graph = None
        self.solver = None
        self.visualizer = None
        self.results_dir = 'results'

        self._interactive_choice()

        from points import get_distance_matrix
        self.dist_matrix = get_distance_matrix(self.points)

    def _interactive_choice(self) -> None:
        """Hỏi lựa chọn: load file hay tạo random."""
        choice = input("Load từ file JSON hay tạo điểm ngẫu nhiên? (load/random, mặc định random): ").strip().lower()
        if choice == 'load':
            self._load_from_file_interactive()
        else:
            self._generate_random_interactive()

    def _load_from_file_interactive(self) -> None:
        """Hỏi file_path, load points, tự set n."""
        file_path = input("Nhập đường dẫn file JSON (ví dụ: /content/random_points_6.json): ").strip()
        if not os.path.exists(file_path):
            print("File không tồn tại. Fallback về tạo ngẫu nhiên.")
            self._generate_random_interactive()
            return

        try:
            with open(file_path, 'r') as f:
                points_data = json.load(f)
            self.points = []
            for data in points_data:
                index = data.get('index', len(self.points))
                x = data.get('x', 0.0)
                y = data.get('y', 0.0)
                self.points.append(Point(x, y, index))
            self.n = len(self.points)
            print(f"Đã load {self.n} điểm từ file: {self.points}")
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Lỗi đọc file: {e}. Fallback về tạo ngẫu nhiên.")
            self._generate_random_interactive()

    def _generate_random_interactive(self) -> None:
        """Hỏi n, generate random points, lưu JSON."""
        try:
            n_input = input("Nhập số lượng điểm (n, mặc định 5, max 12): ").strip()
            self.n = int(n_input) if n_input else 5
            if self.n > 12:
                print("Cảnh báo: n > 12 có thể chậm. Đặt n=12.")
                self.n = 12
            if self.n < 3:
                self.n = 3
        except ValueError:
            self.n = 5
            print("Input không hợp lệ, dùng n=5 mặc định.")

        self.points = generate_random_points(self.n)

        # Tự động lưu JSON
        os.makedirs(self.results_dir, exist_ok=True)
        points_data = [{'index': p.index, 'x': p.x, 'y': p.y} for p in self.points]
        points_file = os.path.join(self.results_dir, f'random_points_{self.n}.json')
        with open(points_file, 'w') as f:
            json.dump(points_data, f, indent=4)
        print(f"Đã lưu điểm ngẫu nhiên vào: {points_file}")

    def _initialize_components(self) -> None:
        """Khởi tạo graph, solver, visualizer (sử dụng self.dist_matrix nếu cần)."""
        self.graph = TSPGraph(self.points)
        self.solver = AStarSolver(self.graph)
        self.visualizer = Visualizer(self.points)
        print("Khởi tạo components (graph, solver, visualizer)...")

    def run(self, max_steps: int = 50) -> Tuple[List[int], float]:
        """Chạy toàn bộ: Solve A*, visualize steps, tạo GIF/final plot, cleanup."""
        self._initialize_components()

        path, cost, steps = self.solver.solve_with_visual(max_steps=max_steps)
        print("\nPath tối ưu:", path)
        print("Tổng chi phí:", round(cost, 2))

        if path:
            # Visualize steps
            for step_num, (current_path, queue_sample) in enumerate(steps):
                title = "Initialization" if step_num == 0 else f"Expanded from {current_path[-1]}, Path: {current_path}"
                self.visualizer.plot_step(step_num, current_path, queue_sample, title)

            # Tạo GIF và final plot
            self.visualizer.create_gif(len(steps) - 1)
            self.visualizer.plot_final_result(path, cost)

        # Cleanup
        self.visualizer.cleanup()

        self._list_results()
        return path, cost

    def _list_results(self) -> None:
        """In danh sách file trong results/."""
        if os.path.exists(self.results_dir):
            files = [f for f in os.listdir(self.results_dir) if not f.startswith('.')]
            print(f"\nNội dung thư mục {self.results_dir}:")
            for f in sorted(files):
                print(f"  - {f}")
        else:
            print("Thư mục results không tồn tại.")
