class Solution:
    def calc(self,i,j,k,strs,m,n,dp):
        if i==len(strs):
            return 0
        temp = f"{i}-{j}-{k}"
        if dp.get(temp) is not None:
            return dp[temp]
        count_zero,count_one=0,0
        for char in strs[i]:
            if char=='1':
                count_one+=1
            else:
                count_zero+=1
        ans = 0
        if count_zero+j<=m and count_one+k<=n:
            ans=max(1+self.calc(i+1,count_zero+j,count_one+k,strs,m,n,dp),self.calc(i+1,j,k,strs,m,n,dp))
        else:
            ans = self.calc(i+1,j,k,strs,m,n,dp)
        dp[temp]=ans
        return ans
            
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp={}
        return self.calc(0,0,0,strs,m,n,dp)
        