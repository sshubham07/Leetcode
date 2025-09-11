class Solution:
    def sortVowels(self, s: str) -> str:
        arr=[]
        for i in s:
            if i in 'aeiouAEIOU':
                arr.append(i)
        arr.sort()
        start=0
        ans =""
        for i in s:
            if i in 'aeiouAEIOU':
                ans+=arr[start]
                start+=1
            else:
                ans +=i
        return ans