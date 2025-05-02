class Solution:
    def pushDominoes(self, d: str) -> str:
        n = len(d)
        left_forces,right_forces = [0]*n, [0]*n
        f = 0
        for i in range(n):
            if d[i] == 'R':
                f = n+1
            elif d[i] =='L':
                f = 0
            f = max(f-1,0)
            left_forces[i] = f
        f = 0
        for i in range(n-1,-1,-1):
            if d[i] == 'L':
                f = n+1
            elif d[i] =='R':
                f = 0
            f = max(f-1,0)
            right_forces[i] = f
        ans=''
        for i in range(n):
            if left_forces[i] > right_forces[i]:
                ans += 'R'
            elif left_forces[i] < right_forces[i]:
                ans += 'L'
            else:
                ans += '.'
        return ans
            