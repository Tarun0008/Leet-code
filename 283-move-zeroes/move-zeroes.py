class Solution:
    def moveZeroes(self, num: List[int]) -> None:
        a=0
        for i in range(len(num)):
            if num[i]!=0:
                num[a]=num[i]
                a+=1
        for i in range(a,len(num)):
            num[i]=0
        print(num)

        """
        Do not return anything, modify nums in-place instead.
        """
        