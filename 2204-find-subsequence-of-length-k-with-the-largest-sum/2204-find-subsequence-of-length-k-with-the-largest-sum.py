import heapq
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        arr1,arr2 = [],[]
        for i in range(len(nums)):
            heapq.heappush(arr1,[-nums[i],i])
        ans = []
        for i in range(k):
            heapq.heappush(arr2,[arr1[0][1],-arr1[0][0]])
            heapq.heappop(arr1)
        for i in range(k):
            ans.append(arr2[0][1])
            heapq.heappop(arr2)
        return ans

