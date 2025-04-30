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
        return node.value
    
    # Find Maximum
    def find_max(self, node):
        if node is None:
            return None
        while node.right:
            node = node.right
        return node.value
    
    # Delete
    def delete(self, node, key):
        if node is None:
            return None  # Return None instead of False
        
        if key < node.value:
            node.left = self.delete(node.left, key)
        elif key > node.value:
            node.right = self.delete(node.right, key)
        else:
            # Case 1: No left child
            if node.left is None:
                return node.right
            # Case 2: No right child
            elif node.right is None:
                return node.left
            # Case 3: Two children
            else:
                temp = self.find_min(node.right)  # Get minimum value in right subtree
                node.value = temp  # Copy the value
                node.right = self.delete(node.right, temp)  # Delete the minimum node
        return node  # Always return the node (or None)
        
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
    
    # Sum of Nodes
    def sum_of_nodes(self):
        return self._sum_of_nodes(self.root)
    
    # Sum of Nodes Recursive
    def _sum_of_nodes(self,node):
        if node is None:
            return 0
        return node.value + self._sum_of_nodes(node.left) + self._sum_of_nodes(node.right)
    
    # Closest Node
    def find_close_node(self, target):
        return self._find_close_node(self.root, target)
    
    # Closest Node Recursive
    def _find_close_node(self,node,target, closet = None):
        if node is None:
            return closet
        
        if closet is None or abs(node.value - target) < abs(closet - target):
            closet = node.value
        if target < node.value:
            return self._find_close_node(node.left, target, closet)
        else:
            return self._find_close_node(node.right, target, closet)
            
    # Check tree is BST or not
    def is_bst(self):
        def order(node, prev):
            if node is None:
                return True
            if not order(node.left, prev): # Check left tree
                return False
            if prev[0] is not None and node.value <= prev[0]: # Ensure increasing order
                return False
            
            prev[0] = node.value # Update previous value
            return order(node.right, prev) # Check right subtree
        return order(self.root, [None])


    ## Get sorted list using in-order traversal
    def _inorder_list(self, node, result):
        if node is None:
            return
        self._inorder_list(node.left, result)
        result.append(node.value)
        self._inorder_list(node.right, result)

    # Second Smallest
    def second_smallest(self):
        result = []
        self._inorder_list(self.root, result)
        if len(result) < 2:
            return None
        return result[1]

    # Third Smallest
    def third_smallest(self):
        result = []
        self._inorder_list(self.root, result)
        if len(result) < 3:
            return None
        return result[2]

    # Second Largest
    def second_largest(self):
        result = []
        self._inorder_list(self.root, result)
        if len(result) < 2:
            return None
        return result[-2]

    # Third Largest
    def third_largest(self):
        result = []
        self._inorder_list(self.root, result)
        if len(result) < 3:
            return None
        return result[-3]
    
    # Kth Smallest
    def kth_smallest(self, k):
        def inorder(node):
            if node is None:
                return None
            left = inorder(node.left)
            if left is not None:
                return left
            
            self.k_count += 1
            if self.k_count == k:
                return node.value
            
            return inorder(node.right)
        
        self.k_count = 0
        return inorder(self.root)

    # Kth Largest
    def kth_largest(self, k):
        def reverse_inorder(node):
            if node is None:
                return None
            right = reverse_inorder(node.right)
            if right is not None:
                return right
            
            self.k_count += 1
            if self.k_count == k:
                return node.value
            
            return reverse_inorder(node.left)
        
        self.k_count = 0
        return reverse_inorder(self.root)
    
    # No of Leaf Nodes
    def count_leaf_nodes(self):
        return self._count_nodes(self.root)

    ## Count Leaf Nodes
    def _count_nodes(self,node):
        if node is None:
            return 0
        
        if node.left is None and node.right is None:
            return 1
        
        return self._count_nodes(node.left) + self._count_nodes(node.right)


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
print("Sum of nodes:", bst.sum_of_nodes())
print("Closest Node: ", bst.find_close_node(65))
print("Tree is BST:", bst.is_bst())
print("Min Number: ", bst.find_min(bst.root))

print("Second Smallest:", bst.second_smallest())  # ➝ 30
print("Third Smallest:", bst.third_smallest())    # ➝ 40
print("Second Largest:", bst.second_largest())    # ➝ 70
print("Third Largest:", bst.third_largest())      # ➝ 60

# Kth elements
print("Second Smallest:", bst.kth_smallest(2))  # ➝ 30
print("Third Smallest:", bst.kth_smallest(3))    # ➝ 40
print("Second Largest:", bst.kth_largest(2))    # ➝ 70
print("Third Largest:", bst.kth_largest(3))      # ➝ 60
print("Leaf nodes count:",bst.count_leaf_nodes())

    

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

# Sum of Nodes
    ## Step 1
        sum_of_nodes() → _sum_of_nodes(root) → _sum_of_nodes(50)

        node.value = 50
        Go to left: _sum_of_nodes(30)
        Go to right: _sum_of_nodes(70)
        Final result = 50 + left_sum + right_sum

    ## Step 2 - Left Subtree of 50
        _sum_of_nodes(30)

        node.value = 30
        Go to left: _sum_of_nodes(20)
        Go to right: _sum_of_nodes(40)
        Final = 30 + left_sum + right_sum

    ## Step 2.1 - Left of 30
        _sum_of_nodes(20)

        node.value = 20
        left = None → returns 0
        right = None → returns 0
        So 20 + 0 + 0 = 20

    ## Step 2.2 - Right of 30
        _sum_of_nodes(40)

        node.value = 40
        left = None → 0
        right = None → 0
        So 40 + 0 + 0 = 40
        ✅ Now, go back to node 30:
        30 + 20 + 40 = 90

    ## Step 2 - Right Subtree of 50
        _sum_of_nodes(70)

        node.value = 70
        Go to left: _sum_of_nodes(60)
        Go to right: _sum_of_nodes(80)
        Final = 70 + left_sum + right_sum

    ## Step 2.1 - Left of 70:
        _sum_of_nodes(60)

        node.value = 60
        left = None → 0
        right = None → 0
        So 60 + 0 + 0 = 60

    ## Step 2.2 - Right of 70
        _sum_of_nodes(80)

        node.value = 80
        left = None → 0
        right = None → 0
        So 80 + 0 + 0 = 80
        ✅ Back to node 70:
        70 + 60 + 80 = 210

    ## Final step — go back to root (50):
        50 + 90 (from left) + 210 (from right) = 350

    ## Visual Flow

           _50_
          ↙    ↘
         30     70
         ↙ ↘   ↙ ↘
        20 40 60 80

        → 20 + 40 = 60
        → 30 + 60 = 90

        → 60 + 80 = 140
        → 70 + 140 = 210

        → 50 + 90 + 210 = 350 ✅

# Find Closest Node (65)
    ## Start
        bst.find_close_node(65)


    ## Start at root (50):
        node = 50, closet = None
        closet becomes 50 (since it’s the first node)
        Is 65 < 50? → No, go right to 70

    ## Move to node 70:
        node = 70, closet = 50
        Compare closeness:
            abs(70 - 65) = 5
            abs(50 - 65) = 15
        Since 70 is closer, update closet = 70
        Is 65 < 70? → Yes, go left to 60

    ## Move to node 60:
        node = 60, closet = 70
        Compare closeness:
            abs(60 - 65) = 5
            abs(70 - 65) = 5
        They are equal, so closet remains 70 (you can keep 60 too, both are equally close)
        Is 65 < 60? → No, go right → but 60 has no right child → node = None

    ## Base Case:
        node = None → return closet
        So, final answer is: 70 ✅

    ## Visual Flow
            50          -> closet = 50
                \
                70        -> abs(70-65) < abs(50-65)? Yes → closet = 70
                /
            60           -> abs(60-65) == abs(70-65)? Yes → closet = 70


# Checking Tree is BST or Not
    Check whether the tree is a valid BST using in-order traversal, which visits:
    Left → Root → Right

    We’re passing prev = [None] to track the previous node value during traversal. This is used to ensure each next node is greater than the previous one.

    ## Step-by-Step Execution
        1. Call: order(50, [None])
            Go left to 30

        2. Call: order(30, [None])
            Go left to 20

        3. Call: order(20, [None])
            Go left → None → returns True
            prev[0] = None, so skip comparison
            Update prev[0] = 20
            Go right → None → returns True
            Return True to previous (30)
            ✅ Now back to node 30

        4. Still in order(30, [20])
            Compare: 30 > 20 → ✅
            Update prev[0] = 30
            Go right to 40

        5. Call: order(40, [30])
            Go left → None → returns True
            Compare: 40 > 30 → ✅
            Update prev[0] = 40
            Go right → None → returns True
            Return True to previous (50)
            ✅ Now back to node 50

        6. Still in order(50, [40])
            Compare: 50 > 40 → ✅
            Update prev[0] = 50
            Go right to 70

        7. Call: order(70, [50])
            Go left to 60

        8. Call: order(60, [50])
            Go left → None → returns True
            Compare: 60 > 50 → ✅
            Update prev[0] = 60
            Go right → None → returns True
            Return True to 70
            ✅ Back to node 70

        9. Still in order(70, [60])
            Compare: 70 > 60 → ✅
            Update prev[0] = 70
            Go right to 80

        10. Call: order(80, [70])
            Go left → None → returns True
            Compare: 80 > 70 → ✅
            Update prev[0] = 80
            Go right → None → returns True
            Return True to 70, then to 50, then final True from is_bst()

    Final Output:
        ✔️ Tree is a valid BST → True

    ## Visual Flow
        20 → check (✓) → prev = 20  
        30 → check 30 > 20 (✓) → prev = 30  
        40 → check 40 > 30 (✓) → prev = 40  
        50 → check 50 > 40 (✓) → prev = 50  
        60 → check 60 > 50 (✓) → prev = 60  
        70 → check 70 > 60 (✓) → prev = 70  
        80 → check 80 > 70 (✓) → prev = 80 

# Kth Smallest
    kth_smallest(3):
    Start at 50 → Go left to 30
    At 30 → Go left to 20

    At 20, no left →
    ✅ visit 20 → k_count = 1

    Back to 30 →
    ✅ visit 30 → k_count = 2

    Go right to 40 →
    ✅ visit 40 → k_count = 3 ✅
    Now k_count == k → return 40

    👉 Final answer: 40 is the 3rd smallest

# Kth Largest
    kth_largest(2):
    Start at 50 → Go right to 70
    At 70 → Go right to 80

    At 80, no right →
    ✅ visit 80 → k_count = 1

    Back to 70 →
    ✅ visit 70 → k_count = 2 ✅
    Now k_count == k → return 70

    👉 Final answer: 70 is the 2nd largest




















"""