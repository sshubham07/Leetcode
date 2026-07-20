class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        total = n*m
        ans = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                flati = i*m + j
                new_flati = (flati+k)%total
                newi = new_flati//m
                newj = new_flati%m
                ans[newi][newj]=grid[i][j]
        return ans
