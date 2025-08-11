class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n==1:
            return True
        i,a=0,0
        while(a<=n and i<=n):
            a=2**i
            i+=1
            if a==n:
                return True
        return False