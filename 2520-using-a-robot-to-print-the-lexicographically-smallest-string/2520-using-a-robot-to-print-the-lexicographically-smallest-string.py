class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        # Step 1: Build suffix min character array
        min_suf = [None] * n
        min_suf[-1] = s[-1]
        for i in range(n - 2, -1, -1):
            min_suf[i] = min(s[i], min_suf[i + 1])

        # Step 2: Simulate robot and stack
        stack = []
        ans = ""

        for i in range(n):
            stack.append(s[i])
            # Keep popping while top of stack <= smallest character remaining
            while stack and (i == n - 1 or stack[-1] <= min_suf[i + 1]):
                ans += stack.pop()

        return ans
