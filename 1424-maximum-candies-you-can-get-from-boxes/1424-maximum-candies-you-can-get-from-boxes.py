class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        ans = 0
        q = set()
        av_boxes = set()
        while initialBoxes:
            i = initialBoxes[-1]
            initialBoxes.pop()
            if status[i]:
                q.add(i)
            else:
                av_boxes.add(i)
            for k in keys[i]:
                status[k] = 1
                if k in av_boxes and k!=i:
                    q.add(k)
            for b in containedBoxes[i]:
                if b not in q and b not in av_boxes and b not in initialBoxes:
                    initialBoxes.append(b)
        for b in q:
            ans += candies[b]
        return ans
