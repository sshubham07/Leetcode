from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        for i in count.keys():
            if i+1 in count:
                ans = max(ans,count[i]+count[i+1])
        return ans

        