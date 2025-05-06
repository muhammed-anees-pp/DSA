"""
Clone Graph
"""
class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node):
    if not node:
        return None

    old_to_new = {}

    def dfs(curr_node):
        if curr_node in old_to_new:
            return old_to_new[curr_node]

        # Create a new node with the same value
        clone = Node(curr_node.val)
        old_to_new[curr_node] = clone

        # Clone all the neighbors
        for neighbor in curr_node.neighbors:
            clone.neighbors.append(dfs(neighbor))

        return clone

    return dfs(node)

# Build a simple graph: 1 -- 2
node1 = Node(1)
node2 = Node(2)
node1.neighbors.append(node2)
node2.neighbors.append(node1)

# Clone the graph
cloned = clone_graph(node1)

# Simple check to show cloning worked
print(f"Original node value: {node1.val}, Cloned node value: {cloned.val}")
print(f"Original neighbor value: {node1.neighbors[0].val}, Cloned neighbor value: {cloned.neighbors[0].val}")
