class Solution:
    def isHappy(self, n: int) -> bool:
        
        s=0

        while n>=5:
            d=0
            for digit in str(n):
                d=d+int(digit)**2
            n=d
        if n==1:
            return True
        else:
            return False