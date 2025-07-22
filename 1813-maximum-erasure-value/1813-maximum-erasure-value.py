class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s= set()
        ans = 0
        start=0
        temp=0
        for i in range(len(nums)):
            while nums[i] in s:
                s.remove(nums[start])
                temp-=nums[start]
                start+=1
            temp+=nums[i]
            s.add(nums[i])
            ans = max(ans,temp)
        return ans

