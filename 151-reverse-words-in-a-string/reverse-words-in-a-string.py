class Solution:
    def reverseWords(self, s: str) -> str:
        lst=[]
        lst=s.split()
        lst.reverse()
        return ' '.join(lst)
        