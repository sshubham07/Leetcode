from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        total = 0
        left = 0
        
        for right in range(n):
            total += nums[right]
            
            # Shrink window from left while score is >= k
            while total * (right - left + 1) >= k:
                total -= nums[left]
                left += 1
                
            ans += (right - left + 1)
        
        return ans
