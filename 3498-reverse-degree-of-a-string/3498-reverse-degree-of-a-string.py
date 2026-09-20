class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i,chr in enumerate(s):
            #print(f"{i}---{chr}---{26-(ord(chr)-ord('a'))}")
            ans+= (i+1)*(26-(ord(chr)-ord('a')))
        return ans