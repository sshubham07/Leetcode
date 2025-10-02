class Solution:
    def calc(self, n,e,dp,empty):
        if n==0 and empty<e:
            return 0
        if dp[n][e][empty]!=-1:
            return dp[n][e][empty]
        if empty>=e and n>0:
            dp[n][e][empty]=max(1+self.calc(n-1,e,dp,empty+1),self.calc(n+1,e+1,dp,empty-e))
        elif empty>=e:
            dp[n][e][empty]=self.calc(n+1,e+1,dp,empty-e)
        else:
            dp[n][e][empty]=1+self.calc(n-1,e,dp,empty+1)
        return dp[n][e][empty]
    def maxBottlesDrunk(self, n: int, e: int) -> int:
        dp = [[[-1]*(n+e+2) for i in range(n+e+2)] for j in range(n+e+2)]
        return self.calc(n,e,dp,0)