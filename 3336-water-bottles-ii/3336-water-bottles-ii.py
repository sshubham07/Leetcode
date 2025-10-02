class Solution:
    def maxBottlesDrunk(self, n: int, e: int) -> int:
        ans = 0
        empty=0
        while n>0 or empty>=e:
            if n>0:
                ans +=n
                empty+=n
                n=0
            else:
                ans+=1
                empty-=e-1
                e+=1
        return ans
        