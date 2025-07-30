class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows=len(matrix)
        cols=len(matrix[0])

        zr=set()
        zc=set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    zr.add(i)
                    zc.add(j)
        

        for i in zr:
            for j in range(cols):
                matrix[i][j]=0

        for j in zc:
            for i in range(rows):
                matrix[i][j]=0

