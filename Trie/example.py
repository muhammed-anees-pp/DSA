class Node:
    def __init__(self):
        self.child = [None] * 26
        self.end = False
        self.count = 0  # To track the count of words passing through this node

class Tree:
    def __init__(self):
        self.root = Node()

    def insert(self, key):
        current = self.root
        for i in key:
            index = ord(i) - ord('a')
            if not current.child[index]:
                current.child[index] = Node()
            current = current.child[index]
            current.count += 1  # Increment count of words passing through
        current.end = True
        

    def display(self):
        def dsp(current, word):
            if current.end:
                print(word)
            for i in range(26):
                if current.child[i]:
                    dsp(current.child[i], word + chr(i + ord('a')))
        dsp(self.root, '')

    def search(self, key):
        current = self.root
        for i in key:
            index = ord(i) - ord('a')
            if not current.child[index]:
                return False
            current = current.child[index]
        return current.end

    def prefixsearch(self, key):
        current = self.root
        for i in key:
            index = ord(i) - ord('a')
            if not current.child[index]:
                return False
            current = current.child[index]
        return True

    def delete_key(self, key):
        def _delete(curr, key, depth):
            if curr is None:
                return False
            if depth == len(key):
                if curr.end:
                    curr.end = False
                    return not any(curr.child)  # Delete node if it has no children
                return False
            index = ord(key[depth]) - ord('a')
            should_delete_current_node = _delete(curr.child[index], key, depth + 1)
            if should_delete_current_node:
                curr.child[index] = None
                return not curr.end and not any(curr.child)
            return False

        return _delete(self.root, key, 0)

    def autocomplete(self, prefix):
        current = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            if not current.child[index]:
                return []
            current = current.child[index]

        result = []
        self._collect_words(current, prefix, result)
        return result

    def _collect_words(self, node, word, result):
        if node.end:
            result.append(word)
        for i in range(26):
            if node.child[i]:
                self._collect_words(node.child[i], word + chr(i + ord('a')), result)

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

    def count_words_with_prefix(self, prefix):
        current = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            if not current.child[index]:
                return 0
            current = current.child[index]
        return current.count

    def find_unique_prefix(self, key):
        current = self.root
        prefix = ''
        for char in key:
            index = ord(char) - ord('a')
            if current.child[index].count == 1:
                prefix += char
                return prefix
            prefix += char
            current = current.child[index]
        return prefix

# Testing the Tree with new functions
ob = Tree()
ob.insert('abcd')
ob.insert('abcde')
ob.insert('abc')
ob.insert('how')
ob.insert('home')

ob.display()
print("Longest Prefix:", ob.longest_prefix())  # Should return 'abc' because 'abcd', 'abcde', 'abc' share it
print("Count Words with Prefix 'ho':", ob.count_words_with_prefix('ho'))  # Should return 2 ('how', 'home')
print("Unique Prefix of 'home':", ob.find_unique_prefix('home'))  # Should return 'hom'