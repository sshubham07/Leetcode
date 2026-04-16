class Solution:
    def calc(self, temp, i):
        ans = len(temp) - 1
        l, h = 0, len(temp) - 1
        while l <= h:
            mid = h - (h - l) // 2
            if temp[mid] >= i:
                ans = mid
                h = mid - 1
            else:
                l = mid + 1
        return ans

    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        d = {}
        n = len(nums)

        for i in range(n):
            if nums[i] not in d:
                d[nums[i]] = []
            d[nums[i]].append(i)

        ans = []

        for i in queries:
            temp = d[nums[i]]

            if len(temp) == 1:
                ans.append(-1)
                continue

            index = self.calc(temp, i)

            # circular neighbors
            left = temp[index - 1] if index > 0 else temp[-1]
            right = temp[index] if temp[index] != i else (
                temp[index + 1] if index + 1 < len(temp) else temp[0]
            )

            # distance function for circular array
            def dist(a, b):
                return min(abs(a - b), n - abs(a - b))

            if dist(i, left) <= dist(i, right):
                ans.append(dist(i, left))
            else:
                ans.append(dist(i, right))

        return ans