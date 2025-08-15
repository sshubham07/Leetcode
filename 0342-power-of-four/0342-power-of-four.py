class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n>=1:
            while n>1 and n%4==0:
                n//=4
        return n==1