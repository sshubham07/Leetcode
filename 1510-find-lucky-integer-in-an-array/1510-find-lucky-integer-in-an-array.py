from collections import defaultdict
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = defaultdict(int)
        ans = -1
        for i in arr:
            d[i]+=1
        for key,val in d.items():
            if key==val:
                ans = max(ans,val)
        return ans
        