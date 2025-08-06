class Solution:
    def convert(self, s: str, numRows: int) -> str:
        r=numRows

        if r==1 or r>=len(s):
            return s

        rows=['']*r
        cr=0
        gd=False

        for char in s :
            rows[cr]+=char

            if cr==0 or cr==r-1:
                gd=not gd
            if gd:
                 cr+=1
            else:
                cr-=1
        return "".join(rows)