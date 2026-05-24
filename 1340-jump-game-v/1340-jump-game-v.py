class Solution:
    def calc(self, arr,d,dp,n,i):
        if dp[i] != -1:
            return dp[i]
        temp = 0
        for j in range(i+1,min(n,i+d+1)):
            if arr[j]<arr[i]:
                temp = max(temp,1+self.calc(arr,d,dp,n,j))
            else:
                break
        for j in range(i-1,max(-1,i-d-1),-1):
            if arr[j]<arr[i]:
                temp = max(temp,1+self.calc(arr,d,dp,n,j))
            else:
                break
        dp[i] = temp
        return dp[i]
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp=[-1]*n
        ans = 1
        for i in range(n):
            ans = max(ans,1+self.calc(arr,d,dp,n,i))
        return ans