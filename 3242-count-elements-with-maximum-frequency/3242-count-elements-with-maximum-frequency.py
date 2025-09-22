from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        maxi = 0
        d = Counter(nums)
        for ele in d.values():
            maxi = max(maxi, ele)
        ans = 0
        for ele in d.values():
            if ele==maxi:
                ans+=1
        return ans*maxi