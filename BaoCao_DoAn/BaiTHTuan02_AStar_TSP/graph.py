from typing import List
from points import Point, get_distance_matrix

class TSPGraph:
    def __init__(self, points: List[Point]):
        self.points = points
        self.n = len(points)
        self.dist = get_distance_matrix(points)
        self.start_node = 0  

    def heuristic(self, current: int, visited: int) -> float:
        """Heuristic admissible: min_dist * (remaining / 2)"""
        unvisited = [i for i in range(self.n) if not (visited & (1 << i))]
        if not unvisited:
            return 0.0
        min_dist = min(self.dist[current][j] for j in unvisited)
        remaining = len(unvisited)
        return min_dist * (remaining / 2.0)

    def is_goal(self, visited: int) -> bool:
        return visited == (1 << self.n) - 1

    def get_unvisited_neighbors(self, current: int, visited: int) -> List[int]:
        return [i for i in range(self.n) if not (visited & (1 << i))]
