from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices  # Number of vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic_util(self, v, visited, rec_stack):
        visited[v] = True
        rec_stack[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:  # If node is in recursion stack, cycle exists
                return True

        rec_stack[v] = False  # Remove the node from recursion stack
        return False

    def is_cyclic(self):
        visited = [False] * self.V
        rec_stack = [False] * self.V

        for node in range(self.V):
            if not visited[node]:  # Run DFS for each component
                if self.is_cyclic_util(node, visited, rec_stack):
                    return True
        return False

# Example Usage
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)  # Cycle
g.add_edge(2, 3)

print("Cycle Detected (Directed Graph):", g.is_cyclic())  # Output: True
