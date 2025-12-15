import os
from matrix_handler import MatrixHandler
from tsp_algorithm import TSPAlgorithm
from tsp_visualizer import TSPVisualizer
from tsp_result import TSPResult

def main():
    """Main function to run TSP application."""
    results_dir = "results"
    os.makedirs(results_dir, exist_ok=True)

    # Input
    file_path = input("Nhập đường dẫn file ma trận khoảng cách (TXT) hoặc 'random': ").strip()

    matrix_handler = MatrixHandler(results_dir)
    algo = TSPAlgorithm(verbose=True)
    visualizer = TSPVisualizer(results_dir)

    if file_path.lower() == 'random':
        n = int(input("Nhập số thành phố (n, khuyến nghị ≤15): "))
        dist_matrix = matrix_handler.create_random(n)
        saved_matrix_path = matrix_handler.save_to_file(dist_matrix, 'random_dist_matrix.txt')
        print(f"Tạo và lưu ma trận vào '{saved_matrix_path}'.")
    else:
        try:
            dist_matrix = matrix_handler.read_from_file(file_path)
            n = len(dist_matrix)
            print(f"Đã đọc ma trận từ '{file_path}'. Số thành phố: {n}")
            saved_matrix_path = None
        except Exception as e:
            print(f"Lỗi: {e}. Fallback random.")
            n = int(input("Nhập số thành phố (n): "))
            dist_matrix = matrix_handler.create_random(n)
            saved_matrix_path = matrix_handler.save_to_file(dist_matrix, 'random_dist_matrix.txt')
            print(f"Tạo và lưu ma trận fallback vào '{saved_matrix_path}'.")

    # Run TSP
    result: TSPResult = algo.solve(dist_matrix)


    print(f"\n=== KẾT QUẢ TSP ===")
    print(f"Chi phí min: {result.min_cost:.2f}")
    print(f"Đường đi: {' -> '.join(map(str, result.path))} -> 0")

    # Create and save animation
    print("\nĐang tạo GIF animation...")
    gif_path = visualizer.create_animation(dist_matrix, result)
    print(f"Animation lưu thành '{gif_path}'")

if __name__ == "__main__":
    main()