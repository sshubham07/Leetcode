class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        count =0
        for i in nums:
            if i==0:
                count+=1
            else:
                ans += (count*(count+1))//2
                count =0
        ans += (count*(count+1))//2
        return ans
        