class Solution:
    def calc(self,num):
        n=0
        while num:
            n+=num%10
            num//=10
        return n
    def minSwaps(self, nums: List[int]) -> int:
        temp=[]
        n = len(nums)
        for i in range(n):
            temp.append((self.calc(nums[i]),nums[i],i))
        temp.sort()
        swaps = 0
        vis = [False]*n
        for i in range(n):
            if temp[i][2]==i or  vis[i]:
                continue
            cycle = 0
            j=i
            while not vis[j]:
                vis[j]=True
                cycle+=1
                j = temp[j][2]
            swaps+=cycle-1
        return swaps

        