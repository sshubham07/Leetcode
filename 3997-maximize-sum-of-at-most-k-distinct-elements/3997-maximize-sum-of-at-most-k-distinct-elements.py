class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        ans = []
        nums.sort(reverse = True)
        for index,num in enumerate(nums):
            if num not in ans and len(ans)<k and num>0:
                ans.append(num)
        return ans