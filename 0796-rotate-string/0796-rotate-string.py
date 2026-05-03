class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        if n!=len(goal):
            return False
        for i in range(n):
            s=s[1:]+s[0]
            if s==goal:
                return True
        return False