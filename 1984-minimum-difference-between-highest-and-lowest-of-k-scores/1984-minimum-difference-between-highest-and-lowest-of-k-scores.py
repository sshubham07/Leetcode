class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        mini=float('inf')
        nums.sort()
        for i in range(k-1,len(nums)):
            mini = min(mini,nums[i]-nums[i-k+1])
        return mini