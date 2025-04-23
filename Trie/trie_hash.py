class TriNode:
    def __init__(self):
        self.children = {}
        self.end_word = False

class Trie:
    def __init__(self):
        self.root = TriNode()
        
    # Insert
    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TriNode()
            node = node.children[char]
        node.end_word = True
    
    # Search
    def search(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_word
    
    # Start with
    def start_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    # Display
    def display(self,node=None, word=""):
        if node is None:
            node = self.root
        if node.end_word:
            print(word)
        for char, child in node.children.items():
            self.display(child,word + char)
            
    # Autocomplete
    def autocomplete(self,prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        words = []
        
        def dfs(current,path):
            if current.end_word:
                words.append(path)
            for char, child in current.children.items():
                dfs(child, path+char)
        
        dfs(node,prefix)
        return words
    
    # Delete
    def delete(self, word):
        def _delete(node, word, depth=0):
            if depth == len(word):
                if not node.end_word:
                    return False
                node.end_word = False
                return len(node.children) == 0
            
            char = word[depth]
            if char not in node.children:
                return False
            
            should_delete = _delete(node.children[char], word, depth + 1)
            
            if should_delete:
                del node.children[char]
                return len(node.children) == 0 and not node.end_word
            return False
        return _delete(self.root, word)
    
    # Long Prefix
    def longest_prefix(self):
        node = self.root
        prefix = ""
        while node and len(node.children) == 1 and not node.end_word:
            char = next(iter(node.children))
            prefix += char
            node = node.children[char]
        return prefix
        
    # Unique Word Count
    def unique_word_count(self):
        count = 0
        def dfs(node):
            nonlocal count
            if node.end_word:
                count += 1
            for child in node.children.values():
                dfs(child)
        dfs(self.root)
        return count
        
    # Count Words with Prefix
    def count_words_with_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        count = 0
        def dfs(current):
            nonlocal count
            if current.end_word:
                count += 1
            for child in current.children.values():
                dfs(child)
        dfs(node)
        return count
    
    
 
trie = Trie()
trie.insert("cat")
trie.insert("can")
trie.insert("car")
print(trie.autocomplete("ca"))
trie.delete("car")
trie.display()
print(trie.longest_prefix())
print(trie.unique_word_count())
trie.insert("cap")
trie.insert("cabin")
trie.insert("dog")
trie.insert("mouse")
trie.display()
print(trie.count_words_with_prefix("ca"))


"""
# Insert
    1. cat
        Step-by-step:
            Start at root.
            'c' not in children → create new node for 'c'
            'a' not in 'c''s children → create new node for 'a'
            't' not in 'a''s children → create new node for 't'
            Mark 't' node as end_word = True
    2. can
            'c' already exists → move to 'c'
            'a' already exists → move to 'a'
            'n' not in 'a''s children → create node 'n'
            Mark 'n' as end_word = True

    Structure:
        (root)
            └── c
                └── a
                    ├── t (end_word = True)
                    ├── n (end_word = True)
                    └── r (end_word = True)


# Search
    How it works:
        Start at the root node.
        For each character in the word:
        If the character is not in the current node’s children → the word doesn't exist → return False
        Otherwise, move to the next node (child)
        After the loop, check if the current node is marked with end_word = True
        If yes → word exists → return True
        If no → only a prefix exists, not a complete word → return False

    1.search("cat")
        Steps:
        'c' in root → ✅
        'a' in 'c' → ✅
        't' in 'a' → ✅
        't' is end_word = True → ✅ Return True

    2. search("ca")
        Steps:
            'c' in root → ✅
            'a' in 'c' → ✅
            No more letters.
            But node 'a' is not end_word → ❌ Return False
            Even though "ca" is a prefix, it's not a complete word in the Trie.

    3. search("car")
        Steps:
            'c' → ✅
            'a' → ✅
            'r' → ✅
            'r' is end_word = True → ✅ Return True

    4. search("cab")
        Steps:
            'c' → ✅
            'a' → ✅
            'b' not in 'a' → ❌ Return False

# Starts with
    Purpose:
        This function checks whether any word in the Trie starts with the given prefix.
        Unlike search(), it doesn't care if the prefix is a full word or not, just whether it exists in the path.

    How it works:
        Start at the root node.
        For each character in the prefix:
        If the character is not present in the current node’s children → return False
        Else, move to that child node.
        If the loop completes without hitting a missing character → return True (because the path exists in the Trie)
    Example:
        1. start_with("ca")
            Trie contains: "cat", "can", "car"
            Steps:
            'c' in root → ✅
            'a' in 'c' → ✅
            All characters found → ✅ Return True
            Even though "ca" is not a complete word, it's a prefix of many words.
        2. start_with("cat")
            Steps:

            'c' → ✅
            'a' → ✅
            't' → ✅
            All found → ✅ Return True
            This is both a prefix and a complete word.

# Autocomplete
    Step 1: Starting autocomplete("ca")
    Step 2: Traversing the Prefix "ca"
        ➤ First Iteration:
            char = 'c'
            'c' is in root.children
            Move to node for 'c'

        ➤ Second Iteration:
            char = 'a'
            'a' is in node.children (i.e., children of 'c')
            Move to node for 'a'

        ✅ Now we’ve successfully reached the node representing 'a', which is at the end of the prefix "ca".

Step 3: Prepare for DFS
    DFS Breakdown Step-by-Step
        We are at node for 'a', and we now go deeper:
            Children of 'a':
                't' → leads to "cat"
                'n' → leads to "can"
                'r' → leads to "car"

            🧭 First Branch: 't'
                char = 't'
                path = 'ca' + 't' = "cat"
                Node 't' is end of word ✅ → "cat" added to list.

            🧭 Second Branch: 'n'
                path = 'ca' + 'n' = "can"
                Node 'n' is end of word ✅ → "can" added.

            🧭 Third Branch: 'r'
                path = 'ca' + 'r' = "car"
                Node 'r' is end of word ✅ → "car" added.
    
    Final:
        ["cat", "can", "car"]

# Delete
    trie.delete("car")

        📍Step 1:
            _delete(node=root, word="car", depth=0)
                depth = 0
                ch = word[0] = 'c'
                'c' in node.children → ✅
                Recurse:
                    _delete(node=node.children['c'], word="car", depth=1)

        
        📍Step 2:
            _delete(node='c' node, word="car", depth=1)
                depth = 1
                ch = word[1] = 'a'
                'a' in node.children → ✅
                Recurse:
                    _delete(node=node.children['a'], word="car", depth=2)


        📍Step 3:
            _delete(node='a' node, word="car", depth=2)
                depth = 2
                ch = word[2] = 'r'
                'r' in node.children → ✅
                Recurse:  
                    _delete(node=node.children['r'], word="car", depth=3)

        📍Step 4: (End of Word)
        _delete(node='r' node, word="car", depth=3)
            depth = len(word) → reached end of the word
            Check if node.end_word == True → ✅
            Set node.end_word = False
            Check if node.children == {} → ✅
            Return True → this 'r' node can be safely deleted.
        
        Backtrack Now:

            ⬅️ Back to Step 3 ('a' node)
                should_delete = True  # from the previous call
                del node.children['r']  # remove 'r' child from 'a'
                Return: len(node.children) == 2 → 'n' and 't' still exist
                        node.end_word == False
                So:
                return False  # Don't delete this node

            ⬅️ Back to Step 2 ('c' node)
                should_delete = False
                    return False

            ⬅️ Back to Step 1 (root)
                should_delete = False
                    return False
    
    Final Trie:
            root
             |
             c
             |
             a
           /   \
         t       n

# Longest Prefix
    node = root
    prefix = ""

    First Iteration:

        node is root
        len(node.children) = 1 ✅ (only 'c')
        node.end_word = False ✅
        char = 'c'
        prefix += 'c' → "c"
        node = node.children['c']

    Second Iteration:

        node is 'c' node
        len(node.children) = 1 ✅ (only 'a')
        node.end_word = False ✅
        char = 'a'
        prefix += 'a' → "ca"
        node = node.children['a']

    Third Iteration:

        node is 'a' node
        len(node.children) = 2 ❌ (has 't' and 'n')
        ❌ Stop the loop

    Final:
        return "ca"

# Unique Word Count
    Setup:
        count = 0

    DFS from root:
        At root: children = c
        Move to c: children = a
        Move to a: children = t, n
            First go to t:
                t.end_word = True → count = 1
                t has no children → backtrack

            Now go to n:
                n.end_word = True → count = 2
                n has no children → backtrack

        All children visited
    
    Final:
        Count = 2

# Count Words with Prefix
    print(trie.count_words_with_prefix("ca"))

        Step-by-Step Execution
            Step 1: Traverse down the prefix "ca"
                node = self.root
                for char in prefix:  # prefix = "ca"

                Iteration 1:
                    char = 'c'
                    'c' in node.children → ✅ Yes
                    node = node.children['c'] → Now at node for 'c'

                Iteration 2:
                    char = 'a'
                    'a' in node.children → ✅ Yes
                    node = node.children['a'] → Now at node for 'a'

                ✅ We successfully reached the node representing "ca"


            Step 2: DFS from node "a" to count all complete words under it
                Start DFS from node "a":
                    "a".end_word = False → count still 0
                    children of "a": t, n, r, p

                DFS 1: child = 't'
                    node for 't'.end_word = True → count = 1
                    't' has no children → backtrack

                DFS 2: child = 'n'
                    node for 'n'.end_word = True → count = 2
                    'n' has no children → backtrack

                DFS 3: child = 'r'
                    node for 'r'.end_word = True → count = 3
                    'r' has no children → backtrack

                DFS 4: child = 'p'
                    node for 'p'.end_word = True → count = 4
                    'p' has no children → backtrack

            Final:
                Count = 4

"""