class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        if n==0:
            return True

        for i in range(length):
            if flowerbed[i] == 0:
                
                if (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
                    flowerbed[i] = 1  
                    n -= 1
                   

                    if n == 0:
                        return True  

        return n == 0  