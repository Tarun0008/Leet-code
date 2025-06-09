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
        print(n,s,d)

        ans=(n*(n+1))//2
        print(ans-s)
        return d,ans-s