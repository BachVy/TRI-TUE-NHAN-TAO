import heapq
from typing import List, Tuple, Dict
from graph import TSPGraph

class AStarSolver:
    def __init__(self, graph: TSPGraph):
        self.graph = graph
        self.visited_states: Dict[Tuple[int, int], float] = {}  

    def calc_f(self, state: Tuple[int, int, float, List[int]]) -> float:
        current, visited, g, _ = state
        h = self.graph.heuristic(current, visited)
        return g + h

    def solve_with_visual(self, max_steps: int = 20) -> Tuple[List[int], float, List[Tuple[List[int], List[Tuple[int, int, float, List[int]]]]]]:
        """Solve A* với print steps chi tiết và trả steps cho visual"""
        start_state = (self.graph.start_node, 1 << self.graph.start_node, 0.0, [self.graph.start_node])
        start_h = self.graph.heuristic(self.graph.start_node, 1 << self.graph.start_node)
        start_f = self.calc_f(start_state)
        pq = [(-start_f, start_state)]
        heapq.heapify(pq)

        steps = [] 
        step = 0
        print(f"Step {step}: Khởi tạo - Current: {self.graph.start_node}, Path: [{self.graph.start_node}], g: {0:.2f}, h: {start_h:.2f}, f: {start_f:.2f}")
        steps.append(([self.graph.start_node], [start_state]))  
        step += 1

        while pq and step <= max_steps:
            _, state = heapq.heappop(pq)
            current, visited, g, path = state
            state_key = (current, visited)
            if state_key in self.visited_states and self.visited_states[state_key] <= g:
                continue
            self.visited_states[state_key] = g

            print(f"\nStep {step}: Pop nút - Current: {current}, Visited: {bin(visited)[2:]} (điểm: {path}), g: {g:.2f}")

            if self.graph.is_goal(visited):
                h = 0
                f = g + h
                print(f"Step {step}: Tìm thấy goal! Path: {path}, Total g: {g:.2f}, h: {h:.2f}, f: {f:.2f}")
                steps.append((path, []))  
                return path, g, steps

            # Mở rộng với print
            expansions = []
            for next_city in self.graph.get_unvisited_neighbors(current, visited):
                new_visited = visited | (1 << next_city)
                new_g = g + self.graph.dist[current][next_city]
                new_path = path + [next_city]
                h_new = self.graph.heuristic(next_city, new_visited)
                f_new = new_g + h_new
                expansions.append((f_new, next_city, new_g, h_new, new_path, new_visited))
                print(f"  Mở rộng đến {next_city}: g_new={new_g:.2f}, h_new={h_new:.2f}, f_new={f_new:.2f}")

            # Push vào queue
            for _, next_city, new_g, _, new_path, new_visited in sorted(expansions):
                new_state = (next_city, new_visited, new_g, new_path)
                heapq.heappush(pq, (-self.calc_f(new_state), new_state))

            # Lấy queue sample
            queue_sample = self._get_queue_sample(pq)
            print(f"  Queue sau mở rộng (top 3 f): {[round(self.calc_f(s), 2) for s in queue_sample]}")
            steps.append((path, queue_sample))
            step += 1

        print("Không tìm thấy goal trong max_steps.")
        return [], 0.0, steps

    def _get_queue_sample(self, pq: List[Tuple[float, Tuple]]) -> List[Tuple[int, int, float, List[int]]]:
        temp_pq = []
        sample = []
        while len(temp_pq) < 3 and pq:
            neg_f, state = heapq.heappop(pq)
            temp_pq.append((neg_f, state))
            sample.append(state)
        for neg_f, state in reversed(temp_pq):
            heapq.heappush(pq, (neg_f, state))
        return sample
