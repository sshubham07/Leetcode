class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)):
            if d.get(nums[i]) is None:
                d[nums[i]]=[]
            d[nums[i]].append(i)
        ans = float('inf')
        for val in d.values():
            for i in range(1,len(val)-1):
                ans = min(ans,val[i]-val[i-1]+val[i+1]-val[i]+val[i+1]-val[i-1])
        return ans if ans !=float('inf') else -1