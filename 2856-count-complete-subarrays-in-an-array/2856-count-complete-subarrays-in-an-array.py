class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        s = set()
        d = {}
        for i in nums:
            s.add(i)
        diff = len(s)
        ans,start,n =0,0,len(nums)
        for i in range(n):
            d[nums[i]] = d.get(nums[i],0)+1
            while len(d) == diff:
                ans += n-i
                d[nums[start]] -= 1
                if d[nums[start]] == 0:
                    del d[nums[start]]
                start += 1 
        return ans

        