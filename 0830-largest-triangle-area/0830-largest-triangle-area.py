class Solution:
    def calc(self, i,j,k):
        ans = i[0]*(j[1]-k[1]) + j[0]*(k[1]-i[1]) + k[0]*(i[1]-j[1])
        return abs(ans) / 2   
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        ans = 0.00
        n = len(points)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    ans = max(ans, self.calc(points[i],points[j],points[k]))
        return ans