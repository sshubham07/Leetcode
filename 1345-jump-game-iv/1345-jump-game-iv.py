from collections import deque

class Solution:
    def minJumps(self, arr: List[int]):

        n = len(arr)
        if n == 1:
            return 0

        mp = {}

        for i, val in enumerate(arr):
            if val not in mp:
                mp[val] = []
            mp[val].append(i)

        q = deque([0])
        vis = {0}

        steps = 0

        while q:

            size = len(q)

            for _ in range(size):

                temp = q.popleft()

                if temp == n-1:
                    return steps

                # left
                if temp-1 >= 0 and temp-1 not in vis:
                    vis.add(temp-1)
                    q.append(temp-1)

                # right
                if temp+1 < n and temp+1 not in vis:
                    vis.add(temp+1)
                    q.append(temp+1)

                # same value
                for j in mp[arr[temp]]:
                    if j not in vis:
                        vis.add(j)
                        q.append(j)

                # avoid reprocessing same value
                mp[arr[temp]] = []

            steps += 1

        return -1