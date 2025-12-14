import os
import numpy as np
from typing import Optional

class MatrixHandler:
    """OOP class for handling distance matrices (input, output, generation)."""
    
    def __init__(self, results_dir: str = "results"):
        self.results_dir = results_dir
        os.makedirs(self.results_dir, exist_ok=True)
    
    def read_from_file(self, file_path: str) -> np.ndarray:
        """Read symmetric distance matrix from TXT file."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File không tồn tại: {file_path}")
        
        matrix = []
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    row = [float(x.strip()) for x in line.replace(',', ' ').split() if x.strip()]
                    matrix.append(row)
        
        n = len(matrix)
        if n == 0:
            raise ValueError("File rỗng.")
        
        matrix = np.array(matrix)
        if matrix.shape != (n, n):
            raise ValueError(f"Ma trận không vuông {n}x{n}.")
        
        return matrix
    
    def create_random(self, n: int) -> np.ndarray:
        """Generate symmetric random distance matrix (diagonal=0)."""
        dist = np.random.randint(1, 101, size=(n, n)).astype(float)
        dist[np.diag_indices(n)] = 0
        dist = (dist + dist.T) / 2
        return dist
    
    def save_to_file(self, matrix: np.ndarray, filename: str) -> str:
        """Save matrix to TXT in results dir."""
        filepath = os.path.join(self.results_dir, filename)
        np.savetxt(filepath, matrix, fmt='%.2f', delimiter=' ')
        return filepath
