class Solution:
    def calc(self, num,l,nums):
        h = len(nums)-1
        ans = l
        while h>=l:
            mid = h-(h-l)//2
            if nums[mid]>=num:
                ans = max(ans,mid)
                l=mid+1
            else:
                h=mid-1
        return ans
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        for i in range(len(nums1)):
            if i>=len(nums2):
                break
            if nums2[i]<nums1[i]:
                continue
            temp = self.calc(nums1[i],i,nums2)
            if temp>i:
                ans = max(ans,temp-i)
        return ans