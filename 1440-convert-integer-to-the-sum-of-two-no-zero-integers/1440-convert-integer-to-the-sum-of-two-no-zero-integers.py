class Solution:
    def check(self,i,j):
        return '0' not in str(i) and '0' not in str(j)
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1,n):
            if self.check(i,n-i):
                return [i,n-i]