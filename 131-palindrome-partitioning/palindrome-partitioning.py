class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(word):
            return word == word[::-1]

        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                prefix = s[start:end]
                if is_palindrome(prefix):
                    backtrack(end, path + [prefix])
        
        backtrack(0, [])
        return res