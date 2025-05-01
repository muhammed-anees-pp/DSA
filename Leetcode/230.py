"""
Kth Smallest Element in a BST
"""
def kth_smallest(root,k):
    k_count = [0]

    def order(node):
        if node is None:
            return None
        
        left = order(node.left)
        if left is not None:
            return left
        
        k_count[0] += 1
        if k_count[0] == k:
            return node.value
        return order(node.right)
    return order(root)
        

## Testing
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


root = TreeNode(100)
root.left = TreeNode(60)
root.right = TreeNode(150)
root.left.left = TreeNode(50)
root.left.right = TreeNode(70)
root.right.left = TreeNode(145)
root.right.right = TreeNode(155)
root.left.left.left = TreeNode(45)
root.left.left.right = TreeNode(55)
root.left.right.left = TreeNode(65)
root.left.right.right = TreeNode(80)
root.right.left.left = TreeNode(140)
root.right.left.right = TreeNode(146)
root.right.right.left = TreeNode(154)
root.right.right.right = TreeNode(160)

# Example usage:
k = 5
result = kth_smallest(root, k)
print(f"The {k}rd smallest element is: {result}")