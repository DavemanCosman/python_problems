## We can also pass the following graph in the __init__ method
# graph = {
#    "A": {"B": 3, "C": 3},
#    "B": {"A": 3, "D": 3.5, "E": 2.8},
#    "C": {"A": 3, "E": 2.8, "F": 3.5},
#    "D": {"B": 3.5, "E": 3.1, "G": 10},
#    "E": {"B": 2.8, "C": 2.8, "D": 3.1, "G": 7},
#    "F": {"G": 2.5, "C": 3.5},
#    "G": {"F": 2.5, "E": 7, "D": 10},
# }
from heapq import heapify, heappop, heappush

class Graph:
    def __init__(self, graph: dict = {}):
       self.graph = graph  # A dictionary for the adjacency list

    def add_edge(self, node1, node2, weight):
       if node1 not in self.graph:  # Check if the node is already added
           self.graph[node1] = {}  # If not, create the node
       self.graph[node1][node2] = weight  # Else, add a connection to its neighbour

    def shortest_distances(self, source: str, target: str):
        # Initialize the values of all nodes with infinity
        distances = {node: float("inf") for node in self.graph}
        distances[source] = 0 # set source value to 0 (from source to source, distance = 0)
        
        pq = [ (0, source) ]
        heapify(pq)
        visited = set()
        
        while pq:
            current_distance,current_node = heappop(pq)
            
            if current_node in visited:
                continue # skip if node is already visited
            visited.add(current_node) #else adds the node to visited
            
            for neighbour, weight in self.graph[current_node].items():
                #calculate distance from current_node to neighbour
                tentative_distance = current_distance + weight
                if tentative_distance < distances[neighbour]:
                    distances[neighbour] = tentative_distance
                    heappush(pq, (tentative_distance, neighbour))
        
        predecessors = {node: None for node in self.graph}
        
        for node, distance in distances.items():
            for neighbour, weight in self.graph[node].items():
                if distances[neighbour] == distance + weight:
                    predecessors[neighbour] = node
        
        path = []
        current_node = target
        while current_node:
            path.append(current_node)
            current_node = predecessors[current_node]
        
        path.reverse()
        
        return distances, path
        
## testing heapify
# pq = [ (3,"A"), (1,"C"), (7,"D") ]
# heapify(pq)
# print(heappop(pq))
# print(heappop(pq))
    
G = Graph()

# Add A and its neighbours
G.add_edge("A", "B", 3)
G.add_edge("A", "C", 3)

# Add B and its neighbours
G.add_edge("B", "A", 3)
G.add_edge("B", "D", 3.5)
G.add_edge("B", "E", 2.8)

# Add C and its neighbours
G.add_edge("C", "A", 3)
G.add_edge("C", "E", 2.8)
G.add_edge("C", "F", 3.5)

# Add D and its neighbours
G.add_edge("D", "B", 3.5)
G.add_edge("D", "E", 3.1)
G.add_edge("D", "G", 10)

# Add E and its neighbours
G.add_edge("E", "B", 2.8)
G.add_edge("E", "C", 2.8)
G.add_edge("E", "D", 3.1)
G.add_edge("E", "G", 7)

# Add F and its neighbours
G.add_edge("F", "G", 2.5)
G.add_edge("F", "C", 3.5)

# Add G and its neighbours
G.add_edge("G", "F", 2.5)
G.add_edge("G", "E", 7)
G.add_edge("G", "D", 10)

## test with node B to node F
start_node = "B"
end_node = "F"

distances, path = G.shortest_distances(start_node, end_node)
print(distances, "\n")

to_end = distances[end_node]
print(f"The shortest distance from {start_node} to {end_node} is {to_end}")
print(f"The shortest path is {path}")


start_node = "A"
end_node = "G"

distances, path = G.shortest_distances(start_node, end_node)
print(distances, "\n")

to_end = distances[end_node]
print(f"The shortest distance from {start_node} to {end_node} is {to_end}")
print(f"The shortest path is {path}")

start_node = "G"
end_node = "D"

distances, path = G.shortest_distances(start_node, end_node)
print(distances, "\n")

to_end = distances[end_node]
print(f"The shortest distance from {start_node} to {end_node} is {to_end}")
print(f"The shortest path is {path}")