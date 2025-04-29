class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count,ans,start,maxi,n =0,0,0,nums[0],len(nums)
        for i in nums:
            maxi = max(maxi, i)
        for i in range(len(nums)):
            if nums[i] == maxi:
                count += 1
            while count == k:
                ans += n-i
                if nums[start] == maxi:
                    count -=1
                start +=1
        return ans
