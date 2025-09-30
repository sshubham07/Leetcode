class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        ans = []
        n = len(nums)
        for i in range(1,n):
            ans.append((nums[i-1]+nums[i])%10)
        return self.triangularSum(ans)