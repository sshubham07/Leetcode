class Solution:
    def calc(self,nums,i,target,dp):
        if i==len(nums)-1:
            return 0
        if dp.get(i) is not None:
            return dp[i]
        ans = float('-inf')
        for j in range(i+1,len(nums)):
            if abs(nums[i]-nums[j])<=target:
                ans = max(ans,1+self.calc(nums,j,target,dp))
        dp[i]=ans
        return ans
    def maximumJumps(self, nums: List[int], target: int) -> int:
        dp={}
        res= self.calc(nums,0,target,dp)
        return res if res>=0 else -1