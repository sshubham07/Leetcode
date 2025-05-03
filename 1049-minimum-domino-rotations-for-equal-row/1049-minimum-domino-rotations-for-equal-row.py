import copy
class Solution:
    def calc(self,t,b, item):
        count =0
        for i in range(len(t)):
            if t[i] != item and b[i]!=item:
                return len(t)+1
            elif t[i] != item:
                count +=1
        return count

    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        ans = len(tops)+1
        i,j =set(),set()
        for items in tops:
            i.add(items)
        for items in bottoms:
            j.add(items)
        for items in i:
            #t,b = copy.deepcopy(tops),copy.deepcopy(bottoms)
            ans = min(ans,self.calc(tops,bottoms,items))
        for items in j:
            #t,b = copy.deepcopy(tops),copy.deepcopy(bottoms)
            ans = min(ans,self.calc(bottoms,tops,items))
        if ans == len(tops)+1:
            ans = -1
        return ans