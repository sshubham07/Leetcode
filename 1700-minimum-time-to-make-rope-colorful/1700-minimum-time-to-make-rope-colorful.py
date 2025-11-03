class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        i=1
        prev = colors[0]
        maxi = neededTime[0]
        s = neededTime[0]
        ans = 0
        while i<n:
            if colors[i]!=prev:
                prev=colors[i]
                s = neededTime[i]
                maxi = neededTime[i]
                i+=1
            else:
                while i<n and colors[i]==prev:
                    maxi=max(neededTime[i],maxi)
                    s+=neededTime[i]
                    i+=1
                ans+=(s-maxi)
        return ans