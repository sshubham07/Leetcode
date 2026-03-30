class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)
        even1,odd1=[],[]
        even2,odd2=[],[]
        for i in range(0,n,2):
            even1.append(s1[i])
            even2.append(s2[i])
        for i in range(1,n,2):
            odd1.append(s1[i])
            odd2.append(s2[i])
        even1.sort()
        even2.sort()
        odd1.sort()
        odd2.sort()
        return even1==even2 and odd1==odd2
