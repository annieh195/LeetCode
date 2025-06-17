class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dir = [[0,1], [1,0], [0,-1], [-1,0]]
        M = len(matrix)
        N = len(matrix[0])
        res = [matrix[0][0]]
        d = 0
        i, j = 0,0
        Mlow, Mhigh, Nlow, Nhigh = 0, M, 0, N

        while len(res) < M*N:
            ni, nj = i+dir[d][0], j+dir[d][1]
            if Nlow <= nj < Nhigh and Mlow <= ni < Mhigh:
                res.append(matrix[ni][nj])
                i,j = ni,nj
            else:
                d = (d+1)%4
                if d == 0:
                    Nlow += 1
                if d == 1:
                    Mlow += 1
                if d == 2:
                    Nhigh -= 1
                if d == 3:
                    Mhigh -= 1
        return res
                