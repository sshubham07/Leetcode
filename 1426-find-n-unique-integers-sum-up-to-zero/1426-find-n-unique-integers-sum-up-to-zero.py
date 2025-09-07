class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        if n%2!=0:
            ans.append(0)
        if n == 1:
            return ans
        start = n//2
        for i in range(-start, start+1):
            if i!=0:
                ans.append(i)
        return ans