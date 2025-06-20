class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        mp = {}
        ans =0
        for i,dir in enumerate(s):
            mp[dir] = mp.get(dir,0)+1
            temp = min(i+1,abs(mp.get('N',0)-mp.get('S',0))+abs(mp.get('E',0)-mp.get('W',0))+2*k)
            ans = max(temp,ans)
        return ans
        