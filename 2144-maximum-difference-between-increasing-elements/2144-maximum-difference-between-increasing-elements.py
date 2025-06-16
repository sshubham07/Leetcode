class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mini = nums[0]
        ans = -1
        for i in range(1,len(nums)):
            if nums[i]>mini:
                ans = max(ans, nums[i]-mini)
            mini=min(mini,nums[i])
        return ans
