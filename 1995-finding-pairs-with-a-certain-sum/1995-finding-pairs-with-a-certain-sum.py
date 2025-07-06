from collections import Counter
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        nums1.sort()
        self.nums1=nums1
        self.nums2=nums2
        self.d=Counter(nums2)

    def add(self, i: int, val: int) -> None:
        self.d[self.nums2[i]] -=1
        if self.d[self.nums2[i]]==0:
            self.d.pop(self.nums2[i])
        self.nums2[i]+=val
        self.d[self.nums2[i]]+=1

    def count(self, tot: int) -> int:
        ans =0
        for i in self.nums1:
            if i>=tot:
                break
            ans += self.d.get(tot-i,0)
        return ans
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)