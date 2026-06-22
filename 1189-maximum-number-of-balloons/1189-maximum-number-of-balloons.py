class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        #ans=0
        mp={}
        for i in text:
            mp[i]=mp.get(i,0)+1
        count = len(text)
        for i in 'balon':
            if i in 'lo':
                count = min(count,mp.get(i,0)//2)
            else:
                count = min(count,mp.get(i,0))
        return count