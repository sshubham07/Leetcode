from heapq import heappush, heappop
from collections import defaultdict
class Solution:
    def mostBooked(self, n: int, m: List[List[int]]) -> int:
        m.sort()
        unused=[]
        used=[]
        total = defaultdict(int)
        for i in range(0,n):
            heappush(unused,i)
        for i in m:
            s = i[0]
            e = i[1]
            while len(used) and used[0][0]<=s:
                room = used[0][1]
                heappop(used)
                heappush(unused,room)
            if len(unused)>0:
                room = unused[0]
                heappop(unused)
                heappush(used,[e,room])
                total[room]+=1
                print(f"{i} inserted in {room}")
            else:
                t = used[0][0]
                room = used[0][1]
                heappop(used)
                total[room]+=1
                heappush(used,[e+(t-s),room])
                print(f"{i} inserted in {room}")
        ans = -1
        c=0
        print("-------------------------------------")
        for i in range(0,n):
            print(f"Room == {i} and Count ={total[i]}")
            if total[i]>c:
                c = total[i]
                ans = i
        return ans



        