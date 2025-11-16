class Solution:
    def numSub(self, s: str) -> int:
        ans = 0
        count = 0
        for i in range(len(s)):
            if s[i]=='1':
                count+=1
            else:
                ans += count*(count+1)//2
                ans%=1000000007
                count = 0
        ans += count*(count+1)//2
        ans%=1000000007
        return ans
        