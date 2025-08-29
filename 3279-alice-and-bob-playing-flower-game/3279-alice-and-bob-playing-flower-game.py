class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        temp1=n//2
        temp2=m//2
        ans =0
        if n%2!=0:
            ans += (temp1+1)*temp2
        else:
            ans += temp1*temp2
        if m%2!=0:
            ans += temp1*(temp2+1)
        else:
            ans += temp1*temp2
        return ans