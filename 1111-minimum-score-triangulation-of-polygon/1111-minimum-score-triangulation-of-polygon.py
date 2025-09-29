from typing import List

class Solution:
    def calc(self, i, j, values, dp):
        # Base case: fewer than 3 vertices → cannot form triangle
        if j - i < 2:
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        res = float('inf')
        
        # Try all possible third vertices k between i and j
        for k in range(i + 1, j):
            cost = values[i] * values[k] * values[j]
            res = min(res,
                      cost + self.calc(i, k, values, dp) + self.calc(k, j, values, dp))
        
        dp[i][j] = res
        return res

    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[-1] * n for _ in range(n)]
        return self.calc(0, n - 1, values, dp)
