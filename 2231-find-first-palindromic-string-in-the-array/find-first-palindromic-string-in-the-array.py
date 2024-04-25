class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        for word in words:
            a=word.split()
            if word == word[::-1]:
                return word   
        return ""
        