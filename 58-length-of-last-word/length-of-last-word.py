class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans=s.split()
        ans=ans[::-1]
        return len(ans[0])