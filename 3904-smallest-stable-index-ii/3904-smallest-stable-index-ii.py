class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        mini=[]
        n = len(nums)
        ele = nums[-1]
        i=n-1
        while i>=0:
            ele = min(ele,nums[i])
            mini.append(ele)
            i-=1
        mini.reverse()
        maxi=nums[0]
        ans = []
        #print(mini)
        for i in range(n):
            maxi= max(nums[i],maxi)
            if maxi-mini[i]<=k:
                return i
        return -1