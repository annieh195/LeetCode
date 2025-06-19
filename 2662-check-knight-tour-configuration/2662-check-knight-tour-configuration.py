class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        M = len(grid)
        N = len(grid[0])
        i, j = 0, 0
        move = 0
        dir = [[2,1], [2,-1], [-2,1], [-2,-1], [1,2], [1,-2], [-1,2], [-1,-2]]

        if grid[0][0] != 0:
            return False

        while move < M*N-1:
            found = False
            for dx, dy in dir:
                ni, nj = i+dx, j+dy
                if 0 <= ni < M and 0 <= nj < N and move+1 == grid[ni][nj]:
                    move += 1
                    i, j = ni, nj
                    found = True
                    break
            if not found:
                return False
        return True
                