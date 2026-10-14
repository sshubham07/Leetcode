class Solution:
    def maxSumOfSquares(self, num: int, s: int) -> str:
        if num*9<s:
            return ""
        arr = [0]*num
        arr[0]=1
        s-=1
        for i in range(num):
            if i==0:
                arr[i]+=min(8,s)
                s-=min(8,s)
            else:
                arr[i]+=min(9,s)
                s-=min(9,s)
            if s==0:
                break
        ans = ""
        for i in range(num):
            ans+=str(arr[i])
        return ans
