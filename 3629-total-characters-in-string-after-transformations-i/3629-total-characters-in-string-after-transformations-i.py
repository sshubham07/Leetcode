class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        cnt = [0]*26
        mod = 1000000007
        for ch in s:
            cnt[ord(ch)-ord('a')] += 1
        for _ in range(t):
            nxt = [0]*26
            nxt[0] = cnt[25]%mod
            nxt[1] = (cnt[0]+cnt[25])%mod
            for i in range(2,26):
                nxt[i] = cnt[i-1]%mod
            cnt = nxt
        return sum(cnt)%mod
        
