class Solution:
    def evaluate(self, s: str, k: list[list[str]]) -> str:
        ans=""
        d={}
        for i in k:
            d[i[0]]=i[1]
        temp=""
        start = 0
        for i in range(len(s)):
            if s[i]=='(':
                start=1
            elif s[i]==')':
                if d.get(temp) is not None:
                    ans +=d[temp]
                else:
                    ans+='?'
                start = 0
                temp=""
            else:
                if start:
                    temp+=s[i]
                else:
                    ans+=s[i]
        if temp:
            if d.get(temp) is not None:
                ans +=d[temp]
            else:
                ans+='?'
        return ans

        
