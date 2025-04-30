class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            count =0
            while i:
                i //=10
                count += 1
            if count%2==0:
                ans += 1
        return ans