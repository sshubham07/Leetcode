class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans,n = set(),len(digits)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if digits[i]%2==0:
                        if digits[j]!=0:
                            ans.add(100*digits[j]+10*digits[k]+digits[i])
                        if digits[k]!=0:
                            ans.add(100*digits[k]+10*digits[j]+digits[i])
                    if digits[j]%2==0:
                        if digits[i]!=0:
                            ans.add(100*digits[i]+10*digits[k]+digits[j])
                        if digits[k]!=0:
                            ans.add(100*digits[k]+10*digits[i]+digits[j])
                    if digits[k]%2==0:
                        if digits[j]!=0:
                            ans.add(100*digits[j]+10*digits[i]+digits[k])
                        if digits[i]!=0:
                            ans.add(100*digits[i]+10*digits[j]+digits[k])
        ans = list(ans)
        ans.sort()
        return ans