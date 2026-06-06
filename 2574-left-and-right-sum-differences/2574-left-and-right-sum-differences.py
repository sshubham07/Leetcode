class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        s=sum(nums)
        temp=0
        ans=[]
        for i in nums:
            ans.append(abs(temp-(s-i)))
            temp+=i
            s-=i
        return ans