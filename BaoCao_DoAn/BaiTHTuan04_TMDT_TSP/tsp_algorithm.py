import numpy as np
from typing import List
from tsp_result import TSPResult

class TSPAlgorithm:
    """OOP class for Nearest Neighbor Heuristic (Greedy) algorithm for TSP."""
    
    def __init__(self, verbose: bool = True):
        self.verbose = verbose
    
    def solve(self, dist_matrix: np.ndarray) -> TSPResult:
        """Solve TSP using Nearest Neighbor: Start from 0, greedily pick closest unvisited city."""
        n = len(dist_matrix)
        visited = [False] * n
        path = [0]  # Start from city 0
        visited[0] = True
        current_city = 0
        total_cost = 0.0
        
        if self.verbose:
            print("\n--- Nearest Neighbor từng bước ---")
        
        for step in range(1, n):
            min_dist = float('inf')
            next_city = -1
            
            # Tìm thành phố gần nhất chưa thăm
            for city in range(n):
                if not visited[city] and dist_matrix[current_city][city] < min_dist:
                    min_dist = dist_matrix[current_city][city]
                    next_city = city
            
            if next_city == -1:
                raise ValueError("Không thể tìm đường đi (ma trận không kết nối).")
            
            path.append(next_city)
            visited[next_city] = True
            total_cost += min_dist
            current_city = next_city
            
            if self.verbose:
                print(f"Bước {step}: Từ {current_city} đến {next_city} (chi phí {min_dist:.1f}, tích lũy {total_cost:.1f})")
        
        # Quay về 0
        return_cost = dist_matrix[current_city][0]
        total_cost += return_cost
        path.append(0)  # Close the tour (for visualization)
        
        if self.verbose:
            print(f"Quay về 0: +{return_cost:.1f} (tổng {total_cost:.1f})")
            print(f"Đường đi: {' -> '.join(map(str, path[:-1]))} -> 0")  # Exclude last 0 for print
        
        return TSPResult(min_cost=total_cost, path=path[:-1])  # Path without duplicate 0
