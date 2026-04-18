class Solution:
    def mirrorDistance(self, n: int) -> int:
        temp = n
        rev=0
        while temp:
            rev*=10
            rev+=temp%10
            temp//=10
        print(rev)
        return abs(n-rev)