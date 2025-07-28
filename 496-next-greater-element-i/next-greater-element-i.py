class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        g={}
        for i in reversed(nums2):
            while stack and stack[-1]<i:
                stack.pop()

            if stack:
                g[i]=stack[-1]
            else:
                g[i]=-1
            stack.append(i)
        r=[]
        for num in nums1:
            r.append(g[num])
        return r