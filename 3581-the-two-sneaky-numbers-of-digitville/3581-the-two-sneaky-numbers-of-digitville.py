class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        s = set()
        ans = []
        for i in nums:
            if i in s:
                ans.append(i)
            s.add(i)
        return ans