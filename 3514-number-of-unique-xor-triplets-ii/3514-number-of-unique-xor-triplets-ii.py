class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        max_xor = 2048
        n = len(nums)
        pair_xor = [False]*max_xor
        triplet_xor = [False]*max_xor
        for i in range(n):
            for j in range(i,n):
                pair_xor[nums[i]^nums[j]]=True
        for i in range(max_xor):
            if pair_xor[i]:
                for v in nums:
                    triplet_xor[i^v]=True
        return sum(triplet_xor)