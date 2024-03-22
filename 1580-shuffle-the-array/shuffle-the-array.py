from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a = nums[:n]
        b = nums[n:]
        res = []
        
        for i in range(n):
            res.append(a[i])
            res.append(b[i])
        
        return res
