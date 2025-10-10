class Solution:
    def calc(self,energy,i,dp,k):
        if i>=len(energy):
            return 0
        if dp[i]!=float('-inf'):
            return dp[i]
        dp[i]= energy[i]+self.calc(energy,i+k,dp,k)
        return dp[i]
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = [float('-inf')]*n
        ans = float('-inf')
        for i in range(n):
            ans = max(ans,self.calc(energy,i,dp,k))
        return ans

        