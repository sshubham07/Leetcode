class Solution:
    def calc(self,s, i, dp, op,count):
        if i==len(s):
            return op==0
        temp = (op,count,i)
        if dp.get(temp) is not None:
            return dp[temp]
        if s[i]=='(':
            dp[temp] = self.calc(s,i+1,dp,op+1,count)
        elif s[i]==')':
            if op<=0:
                return False
            dp[temp] = self.calc(s,i+1,dp,op-1,count)
        else:
            if op>0:
                dp[temp]=self.calc(s,i+1,dp,op+1,count) or self.calc(s,i+1,dp,op-1,count) or self.calc(s,i+1,dp,op,count)
            else:
                dp[temp]=self.calc(s,i+1,dp,op+1,count) or self.calc(s,i+1,dp,op,count)
        return dp[temp]
    def checkValidString(self, s: str) -> bool:
        dp={}
        return self.calc(s,0,dp,0,0)