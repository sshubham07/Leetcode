class Solution:
    def calc(self,s,t,dp,i,j):
        if j==len(t):
            return 1
        if i==len(s):
            return 0
        temp = (i,j)
        if dp.get(temp) is not None:
            return dp[temp]
        ans = 0
        if s[i]==t[j]:
            ans=self.calc(s,t,dp,i+1,j+1)
        ans+=self.calc(s,t,dp,i+1,j)
        dp[temp]=ans
        return ans
        
    def numDistinct(self, s: str, t: str) -> int:
        dp={}
        return self.calc(s,t,dp,0,0)