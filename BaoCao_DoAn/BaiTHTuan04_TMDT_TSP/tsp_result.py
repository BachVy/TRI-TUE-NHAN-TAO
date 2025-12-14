from dataclasses import dataclass
from typing import List

@dataclass
class TSPResult:
    """Dataclass to hold TSP results."""
    min_cost: float
    path: List[int]
