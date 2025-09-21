class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        maxi=nums[0]
        mini=nums[0]
        for i in nums:
            maxi = max(i,maxi)
            mini = min(i,mini)
        return k*(maxi-mini)
        