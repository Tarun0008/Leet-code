class Solution:
    def addDigits(self, num: int) -> int:
        
        while num>=10:
            d=0
            for s in str(num):
                d=d+int(s)

            num=int(d)
        return num