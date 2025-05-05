from collections import deque

class Node:
    def __init__(self, v):
        self.key = v
        self.left = None
        self.right = None

class BT:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if not self.root:
            self.root = node
            return

        q = [self.root]

        while q:
            curr = q.pop(0)
            if not curr.left:
                curr.left = node
                return
            if not curr.right:
                curr.right = node
                return
            q.append(curr.left)
            q.append(curr.right)

def is_same_tree(q1, q2):
    if not q1 and not q2:
        return True
    if not q1 or not q2:
        return False
    if q1.key != q2.key:
        return False
    return is_same_tree(q1.left, q2.left) and is_same_tree(q1.right, q2.right)

# Testing the code
bt = BT()
print('First tree:')
bt.insert(1)
bt.insert(2)
bt.insert(3)

bt2 = BT()
print('Second tree:')
bt2.insert(1)
bt2.insert(2)
bt2.insert(3)

print(is_same_tree(bt.root, bt2.root))  # Should print True
