from collections import Counter
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        one_count=cnt.get(1,0)
        ans = one_count if one_count%2 else one_count-1
        cnt.pop(1,None)
        for num in cnt:
            res=0
            x=num
            while x in cnt and cnt[x]>1:
                res+=2
                x*=x
            ans = max(ans,res+(1 if x in cnt else -1))
        return ans
        