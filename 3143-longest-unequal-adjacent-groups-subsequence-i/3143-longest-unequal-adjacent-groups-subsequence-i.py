class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans,idx =[],groups[0]
        ans.append(words[0])
        for i in range(1,len(groups)):
            if groups[i] !=idx:
                ans.append(words[i])
                idx = groups[i]
        return ans