class Solution:
    def calc(self, temp, n):
        if self.ans!="":
            return
        if len(temp)==n:
            if temp not in self.nums:
                self.ans= temp
            return
        self.calc(temp+"1",n)
        self.calc(temp+"0",n)
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        self.nums = set(nums)
        self.ans = ""
        n = len(nums[0])
        temp = ""
        self.calc(temp,n)
        return self.ans