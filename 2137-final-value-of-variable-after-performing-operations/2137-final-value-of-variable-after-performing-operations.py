class Solution:
    def finalValueAfterOperations(self, o: List[str]) -> int:
        ans = 0
        for i in o:
            if '+' in i:
                ans +=1
            else:
                ans -=1
        return ans