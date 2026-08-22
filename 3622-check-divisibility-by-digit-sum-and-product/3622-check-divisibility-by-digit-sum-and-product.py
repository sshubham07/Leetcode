class Solution:
    def checkDivisibility(self, n: int) -> bool:
        prod=1
        count=0
        temp = n
        while temp:
            count+=temp%10
            prod*=temp%10
            temp//=10
        print(count,prod)
        return n%(count+prod)==0