class Digraph:
    def __init__(self, edges=None):
        self.dict = {}
        if edges:
            for start, end in edges:
                self.add_edge(start, end)
    
    # Add Edge
    def add_edge(self, start, end):
        if start not in self.dict:
            self.dict[start] = []
        self.dict[start].append(end)
        if end not in self.dict:
            self.dict[end] = []
        
    # Add Edges
    def add_edges(self,vertex, edges):
        if vertex not in self.dict:
            self.dict[vertex] = edges
        else:
            self.dict[vertex].extend(edges)

    # Add Vertex
    def add_vertex(self, vertex):
        if vertex not in self.dict:
            self.dict[vertex]=[]
            print("New vertex")
        else:
            print("Already exist")

    # Remove Vertex
    def remove_vertex(self,vertex):
        if vertex in self.dict:
            for key in list(self.dict):
                if vertex in self.dict[key]:
                    self.dict[key].remove(vertex)
            del self.dict[vertex]
            print("Removed")
        else:
            print("Vertex doesn't exist")

    # Remove Edge
    def remove_edge(self,vertex,edge):
        if vertex in self.dict and edge in self.dict[vertex]:
            self.dict[vertex].remove(edge)
            print("Removed")
        else:
            print("Edge don't exist")
            
    # Longest Path
    def longest_path(self, start, end, path=None):
        if start not in self.dict:
            return []
        if path is None:
            path = []
        path = path + [start]

        if start == end:
            return path
        
        longest = []
        for neighbor in self.dict.get(start, []):
            if neighbor not in path:
                new_path = self.longest_path(neighbor, end, path)
                if len(new_path) > len(longest):
                    longest = new_path
        return longest
    
    # Shortest Path
    def shortest_path(self,start,end,path=None):
        if start not in self.dict:
            return []
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return path
        
        shortest = []
        for neighbor in self.dict.get(start,[]):
            if neighbor not in path:
                new_path = self.shortest_path(neighbor, end,path)
                if new_path:
                    if shortest is None or len(new_path) < len(shortest):
                        shortest = new_path
        return shortest
    
    # BfS
    def bfs(self,node):
        visited = set()
        queue = [node]
        print("\nBFS Traversal: ")
        while queue:
            current = queue.pop(0)
            if current not in visited:
                print(current, end=" ")
                visited.add(current)
                queue.extend(self.dict.get(current, []))
        print()
        return visited
    
    # DFS
    def dfs(self,node):
        visited = set()
        stack = [node]
        
        print("\nDFS Traversal: ")
        while stack:
            current = stack.pop()
            if current not in visited:
                print(current, end=" ")
                visited.add(current)
                stack.extend(self.dict.get(current,[]))
        print()
        return visited
    



edges = [('A', 'B'), ('A', 'C'),('C','D'),('A','D')]
g = Digraph(edges)     # Constructor automatically calls add_edge() for each pair
g.add_edge('B', 'D')   # add B → D
g.add_edges('C', ['D', 'E']) # C → D and C → E
print(g.dict)
g.add_vertex('B')
print(g.dict)
g.remove_vertex('B')
print(g.dict)
g.remove_edge('A','C')
g.add_vertex('B')
print(g.dict)
print(g.longest_path('A', 'D'))
g.bfs('A')
g.dfs('A')


"""
# Add Edge
Add one single neighbor.
Uses append, which adds a single element to the list.


# Add Edges
Adds multiple neighbors at once.
Uses extend, which adds all elements from a list into the current list.

    Result:
    {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D', 'E']
    }

# Remove Vertex
if vertex in self.dict
Step 1: Iterating Over Keys
for key in list(self.dict):
self.dict has keys 'A', 'B', 'C'.
list(self.dict) creates a list: ['A', 'B', 'C'].
The loop iterates over each key to check for edges pointing to 'B'.

Step 2: Check for Incoming Edges
if vertex in self.dict[key]:

For each key, check if 'B' is in self.dict[key] (the adjacency list of key).
If 'B' is present, it means there’s an edge from key to 'B' (an incoming edge to 'B').
Let’s process each key:

Key = 'A':
self.dict['A'] = ['B', 'C'].
Is 'B' in ['B', 'C']? Yes.
Proceed to remove 'B'.
Key = 'B':
self.dict['B'] = ['D'].
Is 'B' in ['D']? No.
Skip to the next key.
Key = 'C':
self.dict['C'] = ['D', 'E'].
Is 'B' in ['D', 'E']? No.
Skip to the next key.

Step 3: Remove Incoming Edges
self.dict[key].remove(vertex)
This line executes only for key = 'A' (from the previous step).
self.dict['A'] = ['B', 'C'].
Execute: self.dict['A'].remove('B').
This removes the first occurrence of 'B' from ['B', 'C'].
Result: self.dict['A'] = ['C'].

Step 4: Delete the Vertex
del self.dict[vertex]
vertex = 'B'.
del self.dict['B'] removes the key 'B' and its adjacency list ['D'] from self.dict.
This eliminates 'B' as a vertex and its outgoing edge B → D.

Final Out:
self.dict = {
    'A': ['C'],
    'C': ['D', 'E']
}








"""