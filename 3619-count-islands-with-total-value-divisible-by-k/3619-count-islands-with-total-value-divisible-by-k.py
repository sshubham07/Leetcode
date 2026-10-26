class Solution:
    def calc(self,grid,i,j):
        self.total+=grid[i][j]
        grid[i][j]=0
        row=[0,1,0,-1]
        col=[1,0,-1,0]
        for k in range(4):
            ti=i+row[k]
            tj=j+col[k]
            if 0<=ti<len(grid) and 0<=tj<len(grid[0]) and grid[ti][tj]>0:
                self.calc(grid,ti,tj)
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n,m=len(grid),len(grid[0])
        ans=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    self.total=0
                    self.calc(grid,i,j)
                    if self.total%k==0:
                        ans+=1
        return ans