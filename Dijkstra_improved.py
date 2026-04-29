from heapq import heappop, heappush
from typing import Dict, List, Optional, Tuple

class Graph:
    def __init__(self, graph: Optional[Dict[str, Dict[str, float]]] = None):
        self.graph = graph if graph is not None else {}

    def add_edge(self, node1: str, node2: str, weight: float) -> None:
        if node1 not in self.graph:
            self.graph[node1] = {}
        self.graph[node1][node2] = weight
        if node2 not in self.graph:            # ensure targets are present in adjacency map
            self.graph[node2] = {}

    def shortest_distances(self, source: str, target: str) -> Tuple[Dict[str, float], List[str]]:
        if source not in self.graph:
            raise KeyError(f"Source {source!r} not in graph")

        distances: Dict[str, float] = {node: float("inf") for node in self.graph}
        predecessors: Dict[str, Optional[str]] = {node: None for node in self.graph}
        distances[source] = 0.0

        pq: List[Tuple[float, str]] = [(0.0, source)]
        visited = set()

        while pq:
            current_distance, current_node = heappop(pq)
            if current_node in visited:
                continue
            visited.add(current_node)

            if current_node == target:
                break

            for neighbour, weight in self.graph.get(current_node, {}).items():
                tentative = current_distance + weight
                if tentative < distances[neighbour]:
                    distances[neighbour] = tentative
                    predecessors[neighbour] = current_node   # set predecessor here
                    heappush(pq, (tentative, neighbour))

        # Reconstruct path only if reachable
        if distances.get(target, float("inf")) == float("inf"):
            path: List[str] = []
        else:
            path = []
            cur = target
            while cur is not None:
                path.append(cur)
                cur = predecessors[cur]
            path.reverse()

        return distances, path 