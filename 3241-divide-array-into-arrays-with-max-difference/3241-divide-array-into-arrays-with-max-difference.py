class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        temp = []
        for i in nums:
            temp.append(i)
            if len(temp) == 3:
                if temp[2]-temp[0]>k:
                    return []
                ans.append(temp[:])
                temp = []
        return ans

