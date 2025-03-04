class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:


        samp=sorted(set(nums))
        nums[:len(samp)]=samp
        return len(samp)