"""
Longest Common Prefix
"""

def longestCommonPrefix(strs):
        if not strs:
            return ""
        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix

# Example usage:
words = ["flower","flow","flight"]
print(longestCommonPrefix(words))

words2 = ["dog","racecar","car"]
print(longestCommonPrefix(words2))