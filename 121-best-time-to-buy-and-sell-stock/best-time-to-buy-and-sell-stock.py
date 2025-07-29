class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp=float('inf')
        mx=0

        for price in prices:
            mp=min(mp,price)
            p=price-mp
            mx=max(mx,p)
        return mx