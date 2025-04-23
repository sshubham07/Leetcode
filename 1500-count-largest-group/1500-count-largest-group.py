class Solution:
    def calc(self,i):
        count =0
        #k = i
        while i>0:
            count += i%10
            i = i//10
        #print(f"For {k} count is {count}")
        return count
    def countLargestGroup(self, n: int) -> int:
        maxi,ans =0,0
        d = {}
        for i in range(1,n+1):
            a = self.calc(i)
            d[a] = d.get(a,0)+1
            maxi = max(maxi,d[a])
        for key,val in d.items():
            if val == maxi:
                ans += 1
        return ans
        
