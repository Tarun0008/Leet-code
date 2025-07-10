class Solution:
    def reverseWords(self, s: str) -> str:
        lst=[]
        lst=s.split()
        lst.reverse()
        print(lst)
        return ' '.join(lst)
        