class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n<=0:
            return False

        if n==1 or n==3:
            return True
        a=2
        i=0
        while i<=n:
            i=3**a
            a+=1
            if i==n:
                return True
        return False
