import os
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from tsp_result import TSPResult

class TSPVisualizer:
    """OOP class for creating TSP animation."""
    
    def __init__(self, results_dir: str = "results"):
        self.results_dir = results_dir
    
    def create_animation(self, dist_matrix: np.ndarray, result: TSPResult) -> str:
        """Create and save GIF animation with cumulative cost."""
        n = len(dist_matrix)
        path = result.path
        G = nx.complete_graph(n)
        for i in range(n):
            for j in range(i + 1, n):
                G[i][j]['weight'] = dist_matrix[i][j]
        
        pos = nx.spring_layout(G, seed=42)
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Steps: cumulative edges
        steps = []
        for i in range(len(path) + 1):
            step_edges = [(path[j], path[(j + 1) % len(path)]) for j in range(i)] if i > 0 else []
            steps.append(step_edges)
        
        def init():
            nx.draw_networkx_edges(G, pos, ax=ax, alpha=0.2, width=0.5)
            nx.draw_networkx_nodes(G, pos, ax=ax, node_color='lightblue', node_size=500)
            nx.draw_networkx_labels(G, pos, ax=ax, labels={i: str(i) for i in range(n)}, font_size=12, font_weight='bold')
            ax.set_title("TSP: Bắt đầu từ 0 (Chi phí: 0.0)")
            return ax
        
        def animate(frame):
            ax.clear()
            nx.draw_networkx_edges(G, pos, ax=ax, alpha=0.2, width=0.5)
            nx.draw_networkx_nodes(G, pos, ax=ax, node_color='lightblue', node_size=500)
            nx.draw_networkx_labels(G, pos, ax=ax, labels={i: str(i) for i in range(n)}, font_size=12, font_weight='bold')
            
            current_edges = steps[frame]
            if current_edges:
                nx.draw_networkx_edges(G, pos, ax=ax, edgelist=current_edges, edge_color='red', width=2, arrows=True, arrowsize=20)
            
            # Cumulative cost up to frame
            current_cost = 0.0
            if frame > 0:
                for j in range(frame):
                    from_city = path[j]
                    to_city = path[(j + 1) % len(path)]
                    current_cost += dist_matrix[from_city, to_city]
            
            current_path_str = ' -> '.join(map(str, path[:frame + 1]))
            if frame == len(path):
                current_path_str += ' -> 0'
            
            title = f"Bước {frame}: {current_path_str} (Chi phí tích lũy: {current_cost:.1f})"
            ax.set_title(title)
            return ax
        
        anim = FuncAnimation(fig, animate, init_func=init, frames=len(steps), interval=1500, blit=False, repeat=True)
        
        # Save GIF to results dir
        gif_path = os.path.join(self.results_dir, 'tsp_animation.gif')
        anim.save(gif_path, writer='pillow', fps=0.67)
        plt.close(fig)  # Close to free memory
        
        return gif_path
