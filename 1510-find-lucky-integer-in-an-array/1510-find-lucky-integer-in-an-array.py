from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = Counter(arr)
        ans = -1
        for key,val in d.items():
            if key==val:
                ans = max(ans,val)
        return ans
        