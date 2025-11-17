class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last=-1
        for i in range(len(nums)):
            if nums[i]==1 and last!=-1 and i-last-1<k:
                return False
            if nums[i]==1:
                last=i
        print(last)
        # if nums[-1]==1 and last!=-1 and len(nums)-1-last-1<k:
        #     return False
        return True
        