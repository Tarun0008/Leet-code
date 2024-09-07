
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        outp=[]
        a=max(candies)
        print(a)

        for i in range(len(candies)):
            if candies[i]+extraCandies>=a:
                outp.append(True)
            else:
                outp.append(False)      
        return outp