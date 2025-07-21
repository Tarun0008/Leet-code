class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str, digits)))
        num=num+1
        ans=[]
        for char in str(num):
            ans.append(int(char))
        return ans