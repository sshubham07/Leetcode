class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        n=len(cost)
        ans=0
        i=n-1
        while i>=0:
            if i-1>=0:
                ans +=(cost[i]+cost[i-1])
            else:
                ans +=(cost[i])
            i-=3
        return ans