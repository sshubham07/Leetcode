class Solution:
    def calc(self,bloomDay,mid,m,k):
        total = 0
        count = 0
        start=-1
        for i in range(len(bloomDay)):
            if bloomDay[i]>mid:
                start=-1
                count = 0
                continue
            if bloomDay[i]<=mid and start==-1:
                start = i
                count=1
            elif bloomDay[i]<=mid:
                count+=1
            if count == k:
                total+=1
                start=-1
                count = 0
        return total>=m
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n<m*k:
            return -1
        l=min(bloomDay)
        h = max(bloomDay)
        ans = h
        while l<=h:
            mid = h-(h-l)//2
            if self.calc(bloomDay, mid,m,k):
                ans = mid
                h=mid-1
            else:
                l=mid+1
        return ans