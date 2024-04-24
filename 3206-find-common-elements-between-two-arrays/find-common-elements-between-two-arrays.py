class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a1=0
        a2=0

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                a1+=1
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                a2+=1

        return[a1,a2]