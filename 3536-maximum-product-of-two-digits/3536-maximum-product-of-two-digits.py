class Solution:
    def maxProduct(self, n: int) -> int:
        n = [int(digit) for digit in str(n)]
        n.sort()
        return int(n[-1])*int(n[-2])
        