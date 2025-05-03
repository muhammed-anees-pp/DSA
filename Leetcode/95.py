"""
Unique Binary Search Trees II
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generate_trees(n):
    if n == 0:
        return []

    def build_trees(start, end):
        trees = []

        if start > end:
            trees.append(None)
            return trees

        for root_val in range(start, end + 1):
            left_subtrees = build_trees(start, root_val - 1)
            right_subtrees = build_trees(root_val + 1, end)

            for left in left_subtrees:
                for right in right_subtrees:
                    root = TreeNode(root_val)
                    root.left = left
                    root.right = right
                    trees.append(root)

        return trees

    return build_trees(1, n)

def preorder(root):
    if not root:
        return "None"
    return f"{root.val}, ({preorder(root.left)}), ({preorder(root.right)})"

# Example
n = 3
all_trees = generate_trees(n)

print("Total unique BSTs:", len(all_trees))
print("Preorder traversal of each tree:")

for i, tree in enumerate(all_trees, 1):
    print(f"Tree {i}: {preorder(tree)}")

