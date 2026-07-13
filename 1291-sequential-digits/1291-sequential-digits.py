class Solution:
    def calc(self,low,high,num,last):
        if low<=num<=high:
            self.ans.append(num)
        if num>high or last==9:
            return
        self.calc(low,high,(num*10)+(last+1),last+1)
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        self.ans=[]
        for i in range(0,10):
            self.calc(low,high,0,i)
        return sorted(self.ans)