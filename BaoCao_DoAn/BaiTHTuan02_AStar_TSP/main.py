from points import generate_random_points, DEFAULT_POINTS_DATA 
from graph import TSPGraph
from astar import AStarSolver
from visualizer import Visualizer
import os
import json  

load_file = input("Load từ file JSON điểm? (y/n, mặc định n): ").strip().lower() == 'y'
points = None
n = None

if load_file:
    file_path = input("Nhập đường dẫn file JSON (ví dụ: /content/random_points_6.json): ").strip()
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as f:
                points_data = json.load(f)
            # Tạo list Point từ JSON
            points = []
            for data in points_data:
                index = data.get('index', len(points))
                x = data.get('x', 0.0)
                y = data.get('y', 0.0)
                points.append(Point(x, y, index)) 
            n = len(points)
            print(f"Đã load {n} điểm từ file: {points}")
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Lỗi đọc file: {e}. Fallback về input thủ công.")
            load_file = False
    else:
        print("File không tồn tại. Fallback về input thủ công.")
        load_file = False

# Nếu không load file, fallback về input n như cũ
if not load_file:
    try:
        n_input = input("Nhập số lượng điểm (n, mặc định 5, max 12): ").strip()
        n = int(n_input) if n_input else 5
        if n > 12:
            print("Cảnh báo: n > 12 có thể chậm. Đặt n=12.")
            n = 12
        if n < 3:
            n = 3 
    except ValueError:
        n = 5
        print("Input không hợp lệ, dùng n=5 mặc định.")

    # Tạo points động (default nếu n <=5, random nếu lớn hơn hoặc chọn)
    use_default = input("Sử dụng dữ liệu mặc định? (y/n, mặc định y): ").strip().lower() == 'n'
    is_random = False
    if use_default:
        points = generate_random_points(n)
        is_random = True
    else:
        if n <= 5:
            points = DEFAULT_POINTS_DATA[:n]  # Cắt default nếu n nhỏ
            is_random = False
        else:
            points = generate_random_points(n)  # Random nếu n lớn
            is_random = True

    print(f"Sử dụng {n} điểm: {points}")

    # Lưu points ngẫu nhiên vào file JSON trong results/ (nếu random)
    if is_random:
        if not os.path.exists('results'):
            os.makedirs('results')
        points_data = [{'index': p.index, 'x': p.x, 'y': p.y} for p in points]
        points_file = os.path.join('results', f'random_points_{n}.json')
        with open(points_file, 'w') as f:
            json.dump(points_data, f, indent=4)
        print(f"Đã lưu điểm ngẫu nhiên vào: {points_file}")

# Khởi tạo
graph = TSPGraph(points)
solver = AStarSolver(graph)
visualizer = Visualizer(points)

# Chạy A* 
path, cost, steps = solver.solve_with_visual(max_steps=50)  # Tăng max_steps cho n lớn

# In kết quả tổng
print("\nPath tối ưu:", path)
print("Tổng chi phí:", round(cost, 2))

if path:
    # Vẽ từng step (lưu tạm frames)
    for step_num, (current_path, queue_sample) in enumerate(steps):
        title = "Initialization" if step_num == 0 else f"Expanded from {current_path[-1]}, Path: {current_path}"
        visualizer.plot_step(step_num, current_path, queue_sample, title)

    # Tạo GIF vào results/
    visualizer.create_gif(len(steps) - 1)

    # Đồ thị cuối vào results/
    visualizer.plot_final_result(path, cost)

# Dọn dẹp frames tạm
visualizer.cleanup()

# In danh sách file trong results/
if os.path.exists(visualizer.results_dir):
    files = [f for f in os.listdir(visualizer.results_dir) if not f.startswith('.')]
    print(f"\nNội dung thư mục {visualizer.results_dir}:")
    for f in sorted(files):
        print(f"  - {f}")
else:
    print("Thư mục results không tồn tại.")
