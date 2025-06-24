class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = set()
        n = len(nums)
        for i in range(n):
            if nums[i]==key:
                # print(f"{i}---{max(0,i-k)}----{min(n,i+k+1)}")
                # l = 
                for j in range(max(0,i-k),min(n,i+k+1)):
                    ans.add(j)
        ans = list(ans)
        ans.sort()
        return ans