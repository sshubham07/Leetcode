class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = {}
        ans = 0
        for items in dominoes:
            key = str(min(items[0],items[1]))+'~'+str(max(items[0],items[1]))
            d[key] = d.get(key,0)+1
        for values in d.values():
            if values >1:
                ans += (values)*(values-1)//2
        return ans
