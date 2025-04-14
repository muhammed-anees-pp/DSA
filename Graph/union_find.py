class GraphUF:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v):
        self.edges.append((u, v))

    def find(self, parent, i):
        if parent[i] == -1:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if xroot != yroot:
            parent[xroot] = yroot

    def is_cyclic(self):
        parent = [-1] * self.V

        for u, v in self.edges:
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x == y:  # If u and v have the same root, cycle exists
                return True
            self.union(parent, x, y)

        return False

# Example Usage
g = GraphUF(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 0)  # Cycle

print("Cycle Detected (Undirected Graph):", g.is_cyclic())  # Output: True