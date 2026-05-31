class Solution:
    def asteroidsDestroyed(self, mass: int, a: List[int]) -> bool:
        a.sort()
        for i in a:
            if mass<i:
                return False
            mass+=i
        return True