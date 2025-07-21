class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = ""
        prev='-'
        count=0
        for i in s:
            if prev==i and count==2:
                continue
            elif prev==i:
                count+=1
                ans +=i
            else:
                count =1
                ans +=i
                prev = i
        return ans
        