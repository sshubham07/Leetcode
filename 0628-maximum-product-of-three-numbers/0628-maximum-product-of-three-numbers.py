class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        neg=[i for i in nums if i<0]
        pos=[i for i in nums if i>=0]
        neg.sort()
        pos.sort()
        #print(neg,pos)
        if len(neg)>=2:
            if len(pos)>=3:
                return max(neg[0]*neg[1]*pos[-1],pos[-1]*pos[-2]*pos[-3])
            if len(pos)>0:
                return neg[0]*neg[1]*pos[-1]
            return neg[-1]*neg[-2]*neg[-3]
        #if len(pos)>=3:
        return pos[-1]*pos[-2]*pos[-3]
        #return neg[0]*neg[1]*neg[2]
