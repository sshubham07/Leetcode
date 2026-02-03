class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        i=0
        n=len(nums)
        while i+1<n and nums[i]<nums[i+1]:
            i+=1
        if i==0 or i==n-1:
            return False
        #i+=1
        prev = i
        while i+1<n and nums[i]>nums[i+1]:
            i+=1
        if i==prev or i==n-1:
            return False
        #i+=1
        #prev = i
        while i+1<n and nums[i]<nums[i+1]:
            i+=1
        return i+1==n