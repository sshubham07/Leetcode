class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans =0
        s = set()
        for i in nums:
            if i>0 and i not in s:
                s.add(i)
                ans += i
        if ans ==0:
            return max(nums)
        return ans
        