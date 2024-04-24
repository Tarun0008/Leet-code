
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ma = max(candies)
        lst = []
        for candy in candies:
            if candy + extraCandies >= ma:
                lst.append(True)
            else:
                lst.append(False)
        return lst