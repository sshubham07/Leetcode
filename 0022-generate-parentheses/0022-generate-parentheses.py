class Solution:
    def calc(self,temp,pos,neg):
        if pos==neg==0:
            self.ans.append(temp)
            return
        if neg>pos:
            self.calc(temp+')',pos,neg-1)
        if pos:
            self.calc(temp+'(',pos-1,neg)
    def generateParenthesis(self, n: int) -> list[str]:
        self.ans = []
        temp =""
        self.calc(temp,n,n)
        return self.ans
        