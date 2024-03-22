class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort(reverse=True)
        for i in range(len(arr)-1):

            if arr[i]-arr[i+1]!=arr[0]-arr[1]:
                return False
        
        return True
        