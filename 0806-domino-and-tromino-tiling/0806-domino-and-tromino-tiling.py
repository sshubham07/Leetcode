class Solution:
    def calc(self,n,dp):
        if dp.get(n) is not None:
            return dp[n]
        dp[n] = (self.calc(n-1,dp)*2 + self.calc(n-3,dp))%1000000007
        return dp[n]
    def numTilings(self, n: int) -> int:
        dp = {}
        dp[0] = 1  # empty board
        dp[1] = 1  # only 1 vertical domino
        dp[2] = 2  # (two vertical dominoes OR two horizontal dominoes)
        return self.calc(n,dp)