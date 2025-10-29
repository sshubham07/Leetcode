class Solution:
    def smallestNumber(self, n: int) -> int:
        ans = n
        while True:
            if '0' not in bin(ans)[1:]:
                return ans
            ans +=1
        
        