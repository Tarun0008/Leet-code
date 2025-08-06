class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if len(nums)==1:
            return nums
        k=k%len(nums)
        ans=[]
        ans2=[]
        q=deque()
        for i in range(len(nums)-k):
           ans.append(nums[i])
        for i in range(len(nums)-k,len(nums)):
            ans2.append(nums[i])
        q.extend(ans)
        for i in reversed(ans2):
            q.appendleft(i)
        nums[:]=list(q)
        print(list(q))
