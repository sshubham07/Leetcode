from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        zero_indeces = {i for i in range(n) if arr[i]==0}
        if start in zero_indeces:
            return True
        q=deque([start,])
        vis = {start}
        while q:
            temp = q[0]
            q.popleft()
            if temp+arr[temp] in zero_indeces or temp-arr[temp] in zero_indeces:
                return True
            if temp+arr[temp]>=0 and temp+arr[temp]<n and temp+arr[temp] not in vis:
                q.append(temp+arr[temp])
                vis.add(temp+arr[temp])
            if temp-arr[temp]>=0 and temp-arr[temp]<n and temp-arr[temp] not in vis:
                q.append(temp-arr[temp])
                vis.add(temp-arr[temp])
        print(vis)
        return False
        