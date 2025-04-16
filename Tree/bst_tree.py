from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self) -> None:
        self.root = None
    
    # Insert
    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
            return
        self._insert_rc(self.root,value)
        
    # Insert recursive - private
    def _insert_rc(self,node,value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_rc(node.left,value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_rc(node.right,value)
    
    # Level Order Traversal (Breadth-First Traversal)
    def level_order(self):
        if self.root is None:
            return []
        
        queue = deque([self.root])
        result = []
        
        while queue:
            current = queue.popleft()
            result.append(current.value)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        return result
    
    # Preorder
    def preorder(self, node):
        if node is None:
            return
        print(node.value, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)
    
    # Inorder
    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.value, end=" ")
        self.inorder(node.right)
        
    # Postorder
    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.value, end=" ")
    
    # Find Minimum  
    def find_min(self, node):
        if node is None:
            return None
        while node.left:
            node = node.left
        return node
    
    # Find Maximum
    def find_max(self, node):
        if node is None:
            return None
        while node.right:
            node = node.right
        return node
    
    # Delete
    def delete(self, key, node):
        if node is None:  
            return None
        if key < node.value:
            node.left = self.delete(key, node.left)
        elif key > node.value:
            node.right = self.delete(key, node.right)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            temp = self.find_min(node.right)
            node.value = temp.value
            node.right = self.delete(temp.value, node.right)
        return node
        
    # Search
    def search(self,key):
        def _search(node,key):
            if node is None:
                return False
            if node.value == key:
                return True
            elif key < node.value:
                return _search(node.left,key)
            else:
                return _search(node.right,key)
        return _search(self.root, key)
    
    # Height
    def height(self,node):
        if node is None:
            return -1
        
        return max(self.height(node.left), self.height(node.right)) + 1
    
    # Depth
    def find_depth(self,root,key,depth=0):
        if root is None:
            return -1
        if root.value == key:
            return depth
        left_depth = self.find_depth(root.left, key, depth + 1)
        if left_depth != -1:
            return left_depth
        return self.find_depth(root.right, key, depth + 1)
        

# Examples
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)
print("Level Order: ", bst.level_order())
print(bst.search(60))

    

"""
# Structure

          50
         /  \
       30    70
      / \    / \
    20  40  60  80

# Insertion
    1. tree.insert(50)
        root is None, so Node(50) becomes the root.

    2. tree.insert(30)
        root exists → calls _insert_rc(node=50, value=30)

            30 < 50: check left of 50 → it's None

            Insert Node(30) as left of 50

    3. tree.insert(70)
        Calls _insert_rc(node=50, value=70)

            70 > 50: check right of 50 → it's None

            Insert Node(70) as right of 50

    4. tree.insert(20)
        _insert_rc(node=50, 20) → 20 < 50 → go left to 30

        _insert_rc(node=30, 20) → 20 < 30 → left is None

        Insert Node(20) as left of 30

    5. tree.insert(40)
        _insert_rc(50, 40) → 40 < 50 → left to 30

        _insert_rc(30, 40) → 40 > 30 → right is None

        Insert Node(40) as right of 30

    6. tree.insert(60)
        _insert_rc(50, 60) → 60 > 50 → right to 70

        _insert_rc(70, 60) → 60 < 70 → left is None

        Insert Node(60) as left of 70

    7. tree.insert(80)
        _insert_rc(50, 80) → 80 > 50 → right to 70

        _insert_rc(70, 80) → 80 > 70 → right is None

        Insert Node(80) as right of 70

# Level Order Traversal (Breadth-First Traversal)
    ## Initial State
        queue = deque([50])

        result = []
    
    Iterations,
    1:
        current = 50

        result = [50]

        queue = deque([30, 70]) ← children of 50 added
    2:
        current = 30

        result = [50, 30]

        queue = deque([70, 20, 40]) ← children of 30 added

    3:
        current = 70

        result = [50, 30, 70]

        queue = deque([20, 40, 60, 80]) ← children of 70 added

    4:
        current = 20

        result = [50, 30, 70, 20]

        queue = deque([40, 60, 80]) ← 20 has no children

    5:
        current = 40

        result = [50, 30, 70, 20, 40]

        queue = deque([60, 80]) ← 40 has no children

    6:
        current = 60

        result = [50, 30, 70, 20, 40, 60]

        queue = deque([80]) ← 60 has no children

    7:
        current = 80

        result = [50, 30, 70, 20, 40, 60, 80]

        queue = deque([]) ← 80 has no children

    Final:
        [50, 30, 70, 20, 40, 60, 80]


# Delete(60)
    ## Iterations
        Iteration 1:
        node = 50, key = 60

        60 > 50, so go right → node.right = delete(60, node.right)

    Iteration 2:
        node = 70, key = 60

        60 < 70, so go left → node.left = delete(60, node.left)

    Iteration 3:
        delete(60, node=70.left)  # node = 60

          70
         /
        60

        We want to delete 60.

        What does the code do here?
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

        So it checks:

            Does 60 have a left child? ❌ No

            Does 60 have a right child? ❌ No

            👉 That means 60 is a leaf node (no children at all).

        What happens when a leaf node is deleted?
            We just remove it and return None, because there's no child to replace it.

        So this line runs:
            return None

        This goes back to the previous function call, where we were at node = 70, and node.left was 60.

        We update that like this:
            node.left = None  # 60 is gone now

            

# Search (60)
    Step 1:
        Start at the root, which is 50.
        60 > 50, so go to the right subtree.

    Step 2:
        Now at 70.
        60 < 70, so go to the left subtree.

    Step 3:
        Now at 60.
        60 == 60, match found → return True.





"""