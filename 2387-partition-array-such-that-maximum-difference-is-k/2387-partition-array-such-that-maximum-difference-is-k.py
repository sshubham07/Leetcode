class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        s,count=0,1
        for i, num in enumerate(nums):
            if num-nums[s]>k:
                count += 1
                s = i
        return count