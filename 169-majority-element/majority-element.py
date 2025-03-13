class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        res={}

        for num in nums:
            res[num]=res.get(num,0)+1
        ma=max(res, key=res.get)


        print(res)
        print(ma)
        val=res.get(ma)
        print(val)
        return ma
        