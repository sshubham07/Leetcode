from collections import deque
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1]=='1':
            return False
        q=deque()
        n = len(s)
        q.append(0)
        vis=set()
        vis.add(0)
        covered=0
        while q:
            temp = q.popleft()
            c1 =covered
            if temp+minJump>=n:
                continue
            for i in range(max(covered+1,temp+minJump),min(n,temp+maxJump+1)):
                if i==n-1:
                    return True
                if i not in vis and s[i]=='0':
                    vis.add(i)
                    q.append(i)
                c1 = max(covered,i)
            covered=c1
        return False

        