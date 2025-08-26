class Solution:
    def areaOfMaxDiagonal(self, matrix: List[List[int]]) -> int:
        m=-1
        ans=0
        for l,b in matrix:
            d=math.sqrt((l*l)+(b*b))
            if d>m:
                m=d
                ans=l*b
            elif d==m:
                ans=max(ans,l*b)

        return ans




