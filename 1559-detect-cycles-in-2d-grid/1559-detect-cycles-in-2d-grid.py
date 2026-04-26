class Solution:
    def calc(self,i,j,grid,p1,p2,d,c):
        d.add((i,j))
        dirx = [1,0,-1,0]
        diry = [0,1,0,-1]
        for k in range(4):
            tempx,tempy=i+dirx[k],j+diry[k]
            if tempx>=0 and tempy>=0 and tempx<len(grid) and tempy<len(grid[0]) and grid[tempx][tempy]==c and (tempx!=p1 or tempy!=p2):
                if (tempx,tempy) in d:
                    return True
                if self.calc(tempx,tempy,grid,i,j,d,c):
                    return True
    def containsCycle(self, grid: List[List[str]]) -> bool:
        d= set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in d:
                    if self.calc(i,j,grid,-1,-1,d,grid[i][j]):
                        print(i,j)
                        return True
        return False