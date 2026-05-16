class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = float('inf')
        l=0
        h = len(nums)-1
        while l<=h:
            mid = h-(h-l)//2
            if nums[l] == nums[mid] == nums[h]:
                ans = min(ans, nums[l]) # safeguard: check the boundary element too
                l += 1
                h -= 1
                continue
            if nums[mid]>=nums[l]:
                ans = min(ans,nums[l])
                l=mid+1
            else:
                ans = min(ans,nums[mid])
                h=mid-1
        return ans