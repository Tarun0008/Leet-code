class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        a=Counter(nums)
        
        for key,value in a.items():
            print(key,value)
            if key!=1 and value==1:
                return key
            elif value==1:
                return key