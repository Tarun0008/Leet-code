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



#         n = len(nums)  # n = 4 (how many numbers expected)

# a = sum(nums)  # a = 1+2+2+4 = 9 (sum with repeated number)

# b = sum(set(nums))  # b = 1+2+4 = 7 (sum without repeat)

# s = n*(n+1)//2  # s = 4*5/2 = 10 (sum of numbers from 1 to 4)
