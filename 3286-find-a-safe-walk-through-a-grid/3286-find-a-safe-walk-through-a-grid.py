from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:

        m = len(grid)
        n = len(grid[0])

        health -= grid[0][0]

        if health <= 0:
            return False

        best = [[-1] * n for _ in range(m)]
        best[0][0] = health

        q = deque()
        q.append((0, 0, health))

        dirs = [(0,1), (1,0), (0,-1), (-1,0)]

        while q:

            r, c, h = q.popleft()

            if r == m - 1 and c == n - 1:
                return True

            for dr, dc in dirs:

                nr = r + dr
                nc = c + dc

                if 0 <= nr < m and 0 <= nc < n:

                    nh = h - grid[nr][nc]

                    if nh <= 0:
                        continue

                    if nh > best[nr][nc]:
                        best[nr][nc] = nh
                        q.append((nr, nc, nh))

        return False