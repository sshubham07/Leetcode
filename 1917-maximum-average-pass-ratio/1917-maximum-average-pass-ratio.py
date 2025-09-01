from heapq import heappush,heappop
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        arr=[]
        for i in classes:
            pas,total=i[0],i[1]
            impact = (pas+1)/(total+1)-(pas/total)
            heappush(arr,(-impact,i[0],i[1]))
        for i in range(extraStudents):
            pas,total = arr[0][1],arr[0][2]
            heappop(arr)
            pas,total=pas+1,total+1
            impact = (pas+1)/(total+1)-(pas/total)
            heappush(arr,(-impact,pas,total))
        s=0.0
        for i in range(len(arr)):
            s+=arr[i][1]/arr[i][2]
        return s/len(classes)




        