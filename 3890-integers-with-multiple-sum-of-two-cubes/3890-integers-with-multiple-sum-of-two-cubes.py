class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        s = set()
        d = {}
        i=1
        ans = []
        while i*i*i<=n:
            s.add(i*i*i)
            i+=1
        for i in s:
            for j in s:
                if i!=j and i<j and i+j<=n:
                    d[i+j] = d.get(i+j,0)+1
        for key,val in d.items():
            if val>=2:
                ans.append(key)
        ans.sort()
        return ans