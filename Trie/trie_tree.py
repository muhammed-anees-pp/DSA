class Node:
    def __init__(self):
        self.child = [None] * 26
        self.end = False
        self.count = 0 # To track the count of words passing through this node

class Tree:
    def __init__(self):
        self.root = Node()
    
    # Insert
    def insert(self, key):
        current = self.root
        for i in key:
            ind = ord(i) - ord('a')
            if not current.child[ind]:
                current.child[ind] = Node()
            current = current.child[ind]
            current.count += 1 # Increment count of words passing through
        current.end = True
    
    # Display
    def display(self):
        def dsp(current,word):
            if current.end:
                print(word)
            for i in range(26):
                if current.child[i]:
                    dsp(current.child[i], word + chr(i + ord('a')))
        dsp(self.root, '')
    
    # Search
    def search(self,key):
        current = self.root
        for i in key:
            ind = ord(i) - ord('a')
            if not current.child[ind]:
                return False
            current = current.child[ind]
        return current.end
    
    # Prefix search
    def prefixsearch(self,key):
        current = self.root
        for i in key:
            ind = ord(i) - ord('a')
            if not current.child[ind]:
                return False
            current = current.child[ind]
        return True
    
    # Delete
    def delete_key(self,key):
        def _delete(current, key, depth):
            if current is None:
                return False
            if depth == len(key):
                if current.end:
                    current.end = False
                    return not any(current.child)
                return False
            ind = ord(key[depth]) - ord('a')
            delete_current_node = _delete(current.child[ind], key,depth + 1)
            if delete_current_node:
                current.child[ind] = None
                return not current.end and not any(current.child)
            return False
        return _delete(self.root, key, 0)
    
    # Autocomplete
    def autocomplete(self,prefix):
        current = self.root
        for char in prefix:
            ind = ord(char) - ord('a')
            if not current.child[ind]:
                return []
            current = current.child[ind]
        
        result = []
        self._collect_words(current, prefix,result)
        return result
    
    # Collect Words
    def _collect_words(self,node, word, result):
        if node.end:
            result.append(word)
        for i in range(26):
            if node.child[i]:
                self._collect_words(node.child[i], word + chr(i + ord('a')), result)
    
    # Longest Prefix
    def longest_prefix(self):
        current = self.root
        prefix = ''
        while current and sum(child is not None for child in current.child) == 1 and not current.end:
            for i in range(26):
                if current.child[i]:
                    prefix += chr(i + ord('a'))
                    current = current.child[i]
                    break
        return prefix
    
    # Count Words with Prefix
    def count_words_with_prefix(self,prefix):
        current = self.root
        for char in prefix:
            ind = ord(char) - ord('a')
            if not current.child[ind]:
                return 0
            current = current.child[ind]
        return current.count
        
    # Unique Prefix
    def unique_prefix(self,key):
        current = self.root
        prefix = ''
        for char in key:
            ind = ord(char) - ord('a')
            if not current.child[ind]: 
                return "Word not found"
            if current.child[ind].count == 1:
                prefix += char
                return prefix
            prefix += char
            current = current.child[ind]
        return prefix
    

# Example     
tr = Tree()
tr.insert("app")
tr.insert("apple")
tr.insert("apt")
tr.insert("bat")
tr.display()
print()
tr.delete_key("bat")
tr.display()
print(tr.autocomplete("a"))
print(tr.longest_prefix())
print(tr.count_words_with_prefix("app"))
print(tr.unique_prefix("apple"))

print(tr.search("app"))    # ✅ Returns True (because "app" is a complete word)
print(tr.search("appl"))  # ❌ Returns False (not marked as complete word)

print(tr.prefixsearch("ap"))     # ✅ True (prefix of both "app" and "apple")
print(tr.prefixsearch("app"))    # ✅ True
print(tr.prefixsearch("appl"))   # ✅ True
print(tr.prefixsearch("apple"))  # ✅ True
print(tr.prefixsearch("appley")) # ❌ False
print(tr.prefixsearch("bat"))    # ✅ True


"""
# Insert
Inserting ["app", "apple", "apt"]
    Step-by-step for "app":
    🔁 Loop through each letter:
        'a' → index = ord('a') - ord('a') = 0
            There’s no node for 'a', so we create it.
            Move to 'a' node.
            count becomes 1.

        'p' → index = ord('p') - ord('a') = 15
            No 'p' yet, so create it.
            Move to 'p' node.
            count becomes 1.

        'p' again → index = 15
            No second 'p' yet, create it.
            Move to it.
            count becomes 1.
            ✅ Now we're at the end of the word, so mark this node’s end = True.

    Now insert "apple":
        'a' → index 0
            Already exists, move to 'a' node.
            Increase count to 2.

        'p' → index 15
            Already exists, move to 'p' node.
            Increase count to 2.

        'p' → index 15
            Already exists, move to second 'p' node.
            Increase count to 2.

        'l' → index = ord('l') - ord('a') = 11
            Not present, create node.
            Move to 'l', count = 1.

        'e' → index = 4
            Create node for 'e'.
            count = 1.
            ✅ Mark this final node’s end = True.

    Now insert "apt":
        'a' → index 0
            Already there, move to 'a', count = 3

        'p' → index 15
            Already there, move to 'p', count = 3

        't' → index = 19
            Not there, create it, count = 1
            ✅ Mark this node’s end = True

    Trie Structure:
            (root)
          |
          a (count=3)
          |
          p (count=3)
         / \
      (p)  (t)
      |     \
     l       (end)
     |
     e

# Display
    What happens inside dsp(self.root, '')?
        It works like this:

        1. Start at root with word = ''.
        2. Go to 'a' → word = 'a'
        3. Go to 'p' → word = 'ap'
        4. Go to 'p' again → word = 'app'
            ✅ end = True, so it prints 'app'
        5. Go to 'l' → word = 'appl'
        6. Go to 'e' → word = 'apple'
            ✅ end = True, so it prints 'apple'
        7. Backtrack to 'p', then go to 't' → word = 'apt'
            ✅ end = True, so it prints 'apt'
        8. Backtrack fully, now from root go to 'b' → word = 'b'
        9. Go to 'a' → word = 'ba'
        10. Go to 't' → word = 'bat'
            ✅ end = True, so it prints 'bat'
        
    Output:
        app
        apple
        apt
        bat

# Delete
    Trie structure:
        root
        └── a
            └── p
                └── p (end=True)  ← "app"
                        └── l
                            └── e (end=True) ← "apple"

    delete_key("apple")
    _delete(root, "apple", 0)

    Recursive Steps:
        📍 Depth 0: 'a'
        python
        Copy
        Edit
        ind = 0
        _delete(current.child[0], "apple", 1)

        📍 Depth 1: 'p'
        python
        Copy
        Edit
        ind = 15
        _delete(current.child[15], "apple", 2)

        📍 Depth 2: 'p'
        python
        Copy
        Edit
        ind = 15
        _delete(current.child[15], "apple", 3)

        📍 Depth 3: 'l'
        python
        Copy
        Edit
        ind = 11
        _delete(current.child[11], "apple", 4)

        📍 Depth 4: 'e'
        python
        Copy
        Edit
        ind = 4
        _delete(current.child[4], "apple", 5)

        📍 Depth 5: End of word
        depth == len(key) → ✅
        current.end = True → ✅
        Set current.end = False → unmark the word
        Check: not any(current.child) → 'e' has no children → ✅
        Return True (safe to delete 'e')

    Backtracking:
        🔙 Depth 4: 'l'
        delete_current_node = True
        So: current.child[4] = None → delete 'e'
        Check: not current.end and not any(current.child) → 'l' is not end of word and has no children → ✅
        Return True

        🔙 Depth 3: 'p'
        delete_current_node = True
        So: current.child[11] = None → delete 'l'
        Now check:
        Is current.end == True? → Yes, because 'app' ends here → ❌
        So we don't delete this 'p'
        Return False
    
    Final Structure:
        root
        └── a
            └── p
                └── p (end=True)  ← "app"

# Auto Complete
    autocomplete("ap")

    Step-by-Step:
        Start at root.
        Traverse 'a' → valid.
        Traverse 'p' → valid.
        Call _collect_words() from here.
        From 'ap' node, the following paths exist:
        'p' → 'app'
        'p' + 'l' + 'e' → 'apple'
        't' → 'apt'
    
    Output:
        ['app', 'apple', 'apt']

# Longest Prefix
    Let’s say the Trie contains only these words:
    "app", "apple", "apt"

    Step-by-step Execution:
        Start at root → prefix = ''
        'a' is the only child → add 'a' → prefix = 'a'
        Move to 'a' node → only child is 'p' → add 'p' → prefix = 'ap'
        Move to 'p' → there are two children ('p' and 't')
        → branching happens, so stop here
        👉 Longest common prefix = "ap"
                

# Unique Prefix
    ✅ Word: "app"
        'a' → count = 3 (used by app, apple, apt) → not unique → prefix = 'a'
        'p' → count = 3 (used by app, apple, apt) → not unique → prefix = 'ap'
        'p' → count = 2 (used by app, apple) → not unique → prefix = 'app'
        There’s no character with count = 1 in the path, but "app" is a complete word, so we still use it.
        👉 Unique prefix = "app"

    ✅ Word: "apple"
        'a' → count = 3 → not unique → prefix = 'a'
        'p' → count = 3 → not unique → prefix = 'ap'
        'p' → count = 2 → not unique → prefix = 'app'
        'l' → count = 1 → unique! ✅
        👉 Unique prefix = "appl"

    ✅ Word: "apt"
        'a' → count = 3 → not unique → prefix = 'a'
        'p' → count = 3 → not unique → prefix = 'ap'
        't' → count = 1 → unique! ✅
        👉 Unique prefix = "apt"

    ✅ Word: "bat"
        'b' → count = 1 → only one word starts with 'b' → unique! ✅
        👉 Unique prefix = "b"
    
"""