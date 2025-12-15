from math import sqrt
from typing import List
import random

class Point:
    def __init__(self, x: float, y: float, index: int):
        self.x = x
        self.y = y
        self.index = index

    def __repr__(self):
        return f"Point({self.index}: ({self.x:.2f}, {self.y:.2f}))"

def generate_random_points(n: int) -> List[Point]:
    """Tạo n điểm ngẫu nhiên: Điểm 0 là kho (0,0), các điểm khác random [0,5]x[0,5]"""
    if n < 1:
        raise ValueError("Số điểm n phải >= 1")
    points = [Point(0.0, 0.0, 0)] 
    for i in range(1, n):
        x = random.uniform(0, 5)
        y = random.uniform(0, 5)
        points.append(Point(x, y, i))
    print(f"Đã tạo {n} điểm ngẫu nhiên: {points}")
    return points

def calculate_distance(p1: Point, p2: Point) -> float:
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    return sqrt(dx*dx + dy*dy)

def get_distance_matrix(points: List[Point]) -> List[List[float]]:
    n = len(points)
    dist = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = calculate_distance(points[i], points[j])
    return dist
