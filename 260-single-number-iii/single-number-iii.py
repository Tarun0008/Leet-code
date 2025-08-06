class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}

        for num in nums:
            if num not in d:
                d[num]=1
            else:
                if d[num]==1:
                    del d[num]
        return list(d.keys())
                