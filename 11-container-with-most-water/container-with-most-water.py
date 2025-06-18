class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea=0
        n=len(height)
        left=0
        right=n-1

        while left<right:

            h=min(height[left],height[right])
            w=right-left
            area=h*w
            maxarea=max(area,maxarea)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxarea


        