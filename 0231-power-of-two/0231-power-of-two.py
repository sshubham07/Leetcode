class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count =0
        while n:
            count += n%2
            n//=2
            if count>1:
                return False
        return count ==1
        