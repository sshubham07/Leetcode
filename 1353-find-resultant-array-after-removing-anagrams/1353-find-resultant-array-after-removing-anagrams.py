class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = []
        ans.append(words[0])
        n = len(words)
        s=0
        for i in range(1,n):
            temp = words[s]
            #print(''.join(sorted(words[i])))
            if ''.join(sorted(temp)) != ''.join(sorted(words[i])):
                ans.append(words[i])
                s = i
            #print(s)
        #print(words)
        return ans
