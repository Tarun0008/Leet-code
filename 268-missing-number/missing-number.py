class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n=len(nums)
    
        a=n*(n+1)//2
        print(a)
        
        b=sum(nums)
        print(b)

        return a-b
        
        