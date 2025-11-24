class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        temp=0
        for i in nums:
            temp*=2
            temp+=i
            ans.append(temp%5==0)
        return ans
