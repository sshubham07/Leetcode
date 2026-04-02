class Solution:
    def calc(self,coins,dp,i,j,n):
        if i==len(coins)-1 and j==len(coins[0])-1:
            if n>0:
                return max(0,coins[i][j])
            return coins[i][j]
        temp = (i,j,n)
        if dp.get(temp) is not None:
            return dp[temp]
        ans = float('-inf')
        if n>0:
            if i+1<len(coins) and coins[i][j]<0:
                ans = max(ans,self.calc(coins,dp,i+1,j,n-1))
            if j+1<len(coins[0]) and coins[i][j]<0:
                ans = max(ans,self.calc(coins,dp,i,j+1,n-1))
        if i+1<len(coins):
                ans = max(self.calc(coins,dp,i+1,j,n)+coins[i][j],ans)
        if j+1<len(coins[0]):
            ans = max(ans,self.calc(coins,dp,i,j+1,n)+coins[i][j])
        dp[temp]=ans
        return ans
    def maximumAmount(self, coins: List[List[int]]) -> int:
        dp={}
        return self.calc(coins,dp,0,0,2)