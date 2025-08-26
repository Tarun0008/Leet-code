class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        mergelist=nums1[:m]+nums2[:n]
        
        mergelist=sorted(mergelist)
        nums1[:m+n]=mergelist
        