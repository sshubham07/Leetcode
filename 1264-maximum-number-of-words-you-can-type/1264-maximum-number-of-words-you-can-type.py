class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        arr = text.split(' ')
        print(arr)
        ans =0
        for i in arr:
            check =False
            for j in i:
                if j in brokenLetters:
                    check = True
                    break
            if not check:
                ans +=1
        return ans