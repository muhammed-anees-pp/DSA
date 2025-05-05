"""
Convert Sorted Array to Binary Search Tree
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sorted_array_to_bst(nums):
    def build_tree(left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = build_tree(left, mid - 1)
        node.right = build_tree(mid + 1, right)
        return node
    
    return build_tree(0, len(nums) - 1)

def preorder_traversal(node):
    if not node:
        return []
    return [node.val] + preorder_traversal(node.left) + preorder_traversal(node.right)

# Example
nums = [-10, -3, 0, 5, 9]
root = sorted_array_to_bst(nums)

print("Pre-order traversal of the BST:")
print(preorder_traversal(root))
