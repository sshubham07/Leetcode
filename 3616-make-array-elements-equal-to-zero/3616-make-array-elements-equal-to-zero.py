class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        s = sum(nums)
        print(f"sum == {s}")
        curr=0
        n = len(nums)
        ans = 0
        for i in range(n):
            if curr*2==s and nums[i]==0:
                ans +=2
            elif abs(s-curr-curr)==1 and nums[i]==0:
                ans +=1
            curr+=nums[i]
        return ans
        
        