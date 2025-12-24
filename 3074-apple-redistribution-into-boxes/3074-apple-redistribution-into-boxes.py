class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total= sum(apple)
        capacity.sort(reverse = True)
        s,i= 0,0
        while i<len(capacity):
            s+=capacity[i]
            if s>=total:
                return i+1
            i+=1
        return -1
