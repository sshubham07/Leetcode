class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        d1,d2= abs(x-z),abs(y-z)
        if d1>d2:
            return 2
        elif d2>d1:
            return 1
        return 0
        