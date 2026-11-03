class Solution:
    def minMoves(self, nums: List[int]) -> int:
        largest = nums[0]
        s=0
        n = len(nums)
        for i in range(n):
            s+=nums[i]
            largest=max(largest,nums[i])
        return largest*n-s
