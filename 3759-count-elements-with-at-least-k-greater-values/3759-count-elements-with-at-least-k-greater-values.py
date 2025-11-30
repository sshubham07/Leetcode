class Solution:
    def calc(self, nums, num,l,h):
        # if nums[h]<=num:
        #     return h+1
        temp = h+1
        while l<=h:
            mid = h-(h-l)//2
            if nums[mid]>num:
                temp = mid
                h=mid-1
            else:
                l=mid+1
        return temp


    def countElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        n = len(nums)
        #print(nums)
        for i in range(len(nums)):
            index = self.calc(nums,nums[i],i+1,len(nums)-1)
            #print(index)
            if n-index>=k:
                ans +=1
        return ans