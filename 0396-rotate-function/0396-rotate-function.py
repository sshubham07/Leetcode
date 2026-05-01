class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        total = sum(nums)
        f=0
        n = len(nums)
        for i in range(len(nums)):
            f+=nums[i]*i
        ans = f
        for i in range(n-1,-1,-1):
            f-=nums[i]*n
            f+=total
            ans = max(ans,f)
        return ans