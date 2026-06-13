class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans=""
        for i in words:
            temp=0
            for j in i:
                #print(f"{j}       {weights[ord(j)-97]}")
                temp+=weights[ord(j)-97]
            temp%=26
            temp = abs(25-temp)
            temp+=97
            print(temp)
            ans+=chr(temp)
        return ans