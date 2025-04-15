# Binary Tree with it's basic operations and explanation

class Node:
    def __init__(self,value):
        self.left = None
        self.value = value
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
        
    
    # Inserting
    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
            return
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.left is None:
                current.left = Node(value)
                return
            else:
                queue.append(current.left)
            if current.right is None:
                current.right = Node(value)
                return
            else:
                queue.append(current.right)
                
    # Display-Trversal
    ## Preorder
    def preorder(self,node):
        if node is None:
            return
        print(node.value, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)
    
    
    ## Inorder
    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.value, end=" ")
        self.inorder(node.right)
    
    ## Postorder
    def postorder(self,node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.value, end=" ")
        
    # Delete
    def delete(self,value):
        if self.root is None:
            return None
        
        queue = [self.root]
        node_delete = None
        last_node = None
        last_parent = None
        
        while queue:
            current = queue.pop(0)
            if current.value == value:
                node_delete = current
            last_node = current
            if current.left:
                last_parent = current
                queue.append(current.left)
            if current.right:
                last_parent = current
                queue.append(current.right)
        
        if node_delete is None:
            return False
        
        node_delete.value = last_node.value
        
        if last_node == self.root:
            self.root = None
            return
        
        if last_parent:
            if last_parent.left == last_node:
                last_parent.left = None
            else:
                last_parent.right = None
    
    # Depth
    def find_depth(self,root,key,depth = 0):
        if root is None:
            return -1
        
        if root.value == key:
            return depth
        
        left_depth = self.find_depth(root.left, key, depth + 1)
        if left_depth != -1:
            return left_depth
        return self.find_depth(root.right, key, depth + 1)
    
    # Height
    def height(self,node):
        if node is None:
            return -1
        
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return max(left_height,right_height) + 1
    
    # Level
    def level_order(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            print(current.value, end = " ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    
    # Searching
    def search(self,value):
        if self.root is None:
            return False
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.value == value:
                return True
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return False
    
    # Minimum
    def find_min(self):
        if self.root is None:
            return None
        
        queue = [self.root]
        min_value = float("inf")
        while queue:
            current = queue.pop(0)
            min_value = min(min_value, current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return min_value
    
    # Maximum
    def find_max(self):
        if self.root is None:
            return None
        
        queue = [self.root]
        max_value = float("-inf")
        while queue:
            current = queue.pop(0)
            max_value = max(max_value, current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return max_value
        

# Operations
tr = Tree()
tr.insert(10)
tr.insert(20)
tr.insert(30)
tr.insert(40)
tr.insert(50)
tr.insert(60)
tr.insert(70)
print("Preorder Traversal: ", end="")
tr.preorder(tr.root)
print("\nSearching 60:",tr.search(60))
print("Level Order Traversal: ", end="")
tr.level_order()
print("\nMin Value:", tr.find_min())
print("Max Value:", tr.find_max())
print("Depth of node 50:", tr.find_depth(tr.root, 50))
print("Height of tree:", tr.height(tr.root))

tr.delete(30)

# after delete
print("Inorder Traversal: ", end="")
tr.inorder(tr.root)
print("\nPostorder Traversal: ", end="")
tr.postorder(tr.root)










"""
# Tree Structure

       10
    /      \
   20        30
 /   \     /   \
40   50   60    70


# Traversal
    ## Preorder
        [10, 20, 40, 50, 30, 60, 70]

    ## Inorder
        [40, 20, 50, 10, 60, 30, 70]


    ## Postorder
        [40, 50, 20, 60, 70, 30, 10]


# Delete (30)
    ## Initial setup
        queue = [root]  # queue = [10]
        node_delete = None
        last_node = None
        last_parent = None

    1st iteration
        current = 10
        queue = []

        # current.value != 30 → skip

        last_node = 10

        current.left = 20 → last_parent = 10, queue = [20]
        current.right = 30 → last_parent = 10, queue = [20, 30]

    2nd Iteratoin
        current = 20
        queue = [30]

        last_node = 20

        current.left = 40 → last_parent = 20, queue = [30, 40]
        current.right = 50 → last_parent = 20, queue = [30, 40, 50]

    3rd Iteration
        current = 30
        queue = [40, 50]

        current.value == 30 → node_delete = 30

        last_node = 30

        current.left = 60 → last_parent = 30, queue = [40, 50, 60]
        current.right = 70 → last_parent = 30, queue = [40, 50, 60, 70]

    4th Iteration
        current = 40
        queue = [50, 60, 70]

        last_node = 40
        # No children → nothing added

    5th Iteration
        current = 50
        queue = [60, 70]

        last_node = 50
        # No children

    6th Iteration
        current = 60
        queue = [70]

        last_node = 60
        # No children

    7th Iteration
        current = 70
        queue = []

        last_node = 70
        # No children


    End of the loop:
        node_delete = node with value 30

        last_node = node with value 70

        last_parent = parent of 70 = 30

    Replace:
        node_delete.value = last_node.value  # node 30 becomes 70


    Through these step:
        if last_parent.left == last_node:
            last_parent.left = None
        else:
            last_parent.right = None


    Final tree:

            10
        /    \
        20      70
        /  \    /  
    40   50  60  


# Depth
    Function Call:
    find_depth(tr.root, 60)

    Start: depth = 0

    1 Call: `find_depth(10, 60, 0)`
    - 10 != 60
    - Go left subtree

    2 Call: find_depth(20, 60, 1)
    - 20 != 60
    - Go left subtree

    3 Call: find_depth(40, 60, 2)
    - 40 != 60
    - Left is None → returns -1
    - Right is None → returns -1
    - Backtrack to `20`

    4 Call: find_depth(50, 60, 2)
    - 50 != 60
    - Left is None → returns -1
    - Right is None → returns -1
    - Backtrack to `10`

    5 Call: find_depth(30, 60, 1)
    - 30 != 60
    - Go left subtree

    6 Call: find_depth(60, 60, 2)
    - Match Found! → returns 2


# Height

    ## Left Subtree of 10 (node = 20)
        Left: height(40)
        → Left and right are None → returns -1
        → max(-1, -1) + 1 = 0

        Right: height(50)
        → Same as above → 0

        → max(0, 0) + 1 = 1 (height of node 20)

    ## Right Subtree of 10 (node = 30)
        Left: height(60)
        → 0

        Right: height(70)
        → 0

        → max(0, 0) + 1 = 1 (height of node 30)

    ## Final Height at Root (node = 10)
        max(1, 1) + 1 = 2

# Level order
    ## Initial step
        queue = [10]

    ## Loop iterations
        1st:
            current = 10

            Print: 10

            Add 20 and 30 to queue
            ➜ queue = [20, 30]

        2:
            current = 20

            Print: 20

            Add 40 and 50 to queue
            ➜ queue = [30, 40, 50]

        3:
            current = 30

            Print: 30

            Add 60 and 70 to queue
            ➜ queue = [40, 50, 60, 70]

        4:
            current = 40

            Print: 40

            No children to add
            ➜ queue = [50, 60, 70]

        5:
            current = 50

            Print: 50

            No children to add
            ➜ queue = [60, 70]

        6:
            current = 60

            Print: 60

            No children to add
            ➜ queue = [70]

        7:
            current = 70

            Print: 70

            No children to add
            ➜ queue = []


        Final:
            10 20 30 40 50 60 70



"""