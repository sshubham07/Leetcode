class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l = len(['L' for i in moves if i=='L'])
        r = len(['R' for i in moves if i=='R'])
        d = len(['D' for i in moves if i=='_'])
        #print(l,r,d)
        if l>r:
            total = l+d
        else:
            total = r+d
        #print(total)
        return total-min(l,r)