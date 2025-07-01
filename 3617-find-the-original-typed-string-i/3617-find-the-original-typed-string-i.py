class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans =0
        prev = '#'
        count =0
        for i in word:
            if i==prev:
                count+=1
            else:
                if count>1:
                    ans += count-1
                prev = i
                count = 1
        if count>1:
            ans += count-1
        return ans+1
            
