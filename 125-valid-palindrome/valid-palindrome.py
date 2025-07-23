class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss="".join(filter(str.isalnum,s)).lower()
        print(ss)
        if ss == ss[::-1]:
            return True
        return False