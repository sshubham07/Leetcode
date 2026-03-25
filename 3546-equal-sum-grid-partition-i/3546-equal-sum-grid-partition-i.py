class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        res=0
        row,col=[0]*len(grid),[0]*len(grid[0])
        total=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                row[i]+=grid[i][j]
                col[j]+=grid[i][j]
                total+=grid[i][j]
        temp=0
        for i in range(len(row)-1):
            temp+=row[i]
            if 2*temp==total:
                return True
        temp=0
        for i in range(len(col)-1):
            temp+=col[i]
            if 2*temp==total:
                return True
        return False
            