class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        ans=0

        for i in range(1,len(arr)-1):

            if arr[i-1] < arr[i] and arr[i+1]<arr[i]:
                l=r=i
                
                while l>0 and arr[l-1]<arr[l]:
                    l-=1
                  
                while r<len(arr)-1 and arr[r]>arr[r+1]:
                    r+=1
                    
                
                ans=max(ans,r-l+1)
        return ans