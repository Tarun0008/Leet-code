class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        c=1
        for num in arr:
            while c<num:
                k-=1
                if k==0:
                    return c
                c+=1
            c=num+1
        return c+k-1




        