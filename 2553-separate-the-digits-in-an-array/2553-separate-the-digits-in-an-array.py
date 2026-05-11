class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)-1,-1,-1):
            temp = nums[i]
            while temp:
                res.append(temp%10)
                temp//=10
        res.reverse()
        return res