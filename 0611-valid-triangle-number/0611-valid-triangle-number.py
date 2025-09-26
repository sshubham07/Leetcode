class Solution:
    def calc(self,sum,l,nums):
        h=len(nums)-1
        ans = l-1
        while l<=h:
            mid= h-(h-l)//2
            if nums[mid]<sum:
                ans = mid
                l = mid+1
            else:
                h=mid-1
        #print(ans)
        return ans
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans =0
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                ans += self.calc(nums[i]+nums[j],j+1,nums)-j
        return ans
        