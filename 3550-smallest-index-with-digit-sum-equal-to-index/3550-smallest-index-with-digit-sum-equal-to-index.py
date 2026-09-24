class Solution:
    def calc(self, i):
        total=0
        while i:
            total+=i%10
            i//=10
        return total
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if self.calc(nums[i])==i:
                return i
        return -1