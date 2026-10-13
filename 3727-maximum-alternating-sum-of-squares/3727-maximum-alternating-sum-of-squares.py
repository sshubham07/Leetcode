class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse=True,key=lambda i:abs(i))
        start = 0
        end = n-1
        i=0
        ans=0
        while start<=end:
            if i%2==0:
                ans+=nums[start]*nums[start]
                start+=1
            else:
                ans-=nums[end]*nums[end]
                end-=1
            i+=1
            i%=2
        return ans
        