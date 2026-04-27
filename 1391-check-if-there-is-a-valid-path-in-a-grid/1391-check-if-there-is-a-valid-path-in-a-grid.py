class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        dirs = {
        1: [(0,-1), (0,1)],     # left, right
        2: [(-1,0), (1,0)],     # up, down
        3: [(0,-1), (1,0)],     # left, down
        4: [(0,1), (1,0)],      # right, down
        5: [(0,-1), (-1,0)],    # left, up
        6: [(0,1), (-1,0)]      # right, up
        }
        vis = {(0,0)}
        q = deque([(0,0)])
        while q:
            x,y = q.popleft()
            if x==len(grid)-1 and y==len(grid[0])-1:
                return True
            for dx,dy in dirs[grid[x][y]]:
                nx,ny = x+dx,y+dy
                if (nx,ny) not in vis and nx>=0 and nx<len(grid) and ny>=0 and ny<len(grid[0]) and (-dx,-dy) in dirs[grid[nx][ny]]:
                    vis.add((nx,ny))
                    q.append((nx,ny))
        return False