class Solution:
    def calc(self,s1,d1,s2,d2):
        t1 = float('inf')
        for i in range(len(s1)):
            t1= min(t1,s1[i]+d1[i])
        ans = float('inf')
        for i in range(len(s2)):
            ans = min(ans,max(t1,s2[i])+d2[i])
        return ans


    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        t1 = self.calc(landStartTime,landDuration,waterStartTime,waterDuration)
        t2 = self.calc(waterStartTime,waterDuration,landStartTime,landDuration)
        return min(t1,t2)