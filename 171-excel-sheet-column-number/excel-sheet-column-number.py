class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res=0

        for char in columnTitle:
            v=ord(char)-ord('A')+1
            res=res*26+v
        return res