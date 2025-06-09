class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen=set()
        d=0
        for num in nums:
            if num in seen:
                d=num
                break
            seen.add(num)
        s=sum(set(nums))
        n=len(nums)

        ans=(n*(n+1))//2

        return d,ans-s