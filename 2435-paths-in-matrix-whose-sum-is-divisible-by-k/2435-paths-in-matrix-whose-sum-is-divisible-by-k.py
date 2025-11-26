class Solution:
    def calc(self,i,j,sum,dp,grid,k):
        if i==len(grid)-1 and j==len(grid[0])-1:
            if (sum)%k==0:
                return 1
            return 0
        temp = f"{i}-{j}-{sum}"
        if dp.get(temp) is not None:
            return dp[temp]
        ans = 0
        if i+1<len(grid):
            ans+=self.calc(i+1,j,(sum+grid[i+1][j])%k,dp,grid,k)
        if j+1<len(grid[0]):
            ans+=self.calc(i,j+1,(sum+grid[i][j+1])%k,dp,grid,k)
        dp[temp]=ans%1000000007
        return dp[temp]
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        dp={}
        return self.calc(0,0,grid[0][0],dp,grid,k)
        