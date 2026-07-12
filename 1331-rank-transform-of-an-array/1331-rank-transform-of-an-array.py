class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp=[]
        s=set()
        for i in arr:
            if i not in s:
                s.add(i)
                temp.append(i)
        temp.sort()
        pos={}
        for i in range(len(temp)):
            pos[temp[i]]=i+1
        ans=[]
        for i in range(len(arr)):
            ans.append(pos[arr[i]])
        return ans
        