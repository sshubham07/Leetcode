class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        count = 0
        for i in s:
            if i=='a':
                count+=1
            else:
                count -=1
        return abs(count)