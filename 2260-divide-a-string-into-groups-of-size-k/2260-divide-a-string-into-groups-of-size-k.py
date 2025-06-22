class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        temp=""
        for i in s:
            temp+=i
            if len(temp)==k:
                ans.append(temp)
                temp=""
        if len(temp):
            while len(temp)<k:
                temp+=fill
            ans.append(temp)
        return ans
        