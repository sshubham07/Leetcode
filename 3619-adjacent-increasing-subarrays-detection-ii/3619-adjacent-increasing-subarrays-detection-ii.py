class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        ans=0
        currl=1
        prevl=0
        n = len(nums)
        for i in range(1,n):
            if nums[i-1]<nums[i]:
                currl+=1
            else:
                prevl=currl
                currl=1
            ans = max(ans,currl//2,min(prevl,currl))
        return ans