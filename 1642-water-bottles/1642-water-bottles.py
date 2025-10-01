class Solution:
    def numWaterBottles(self, n: int, e: int) -> int:
        ans = 0
        rem=0
        while n:
            ans +=n
            rem+=n
            n = rem//e
            # print(rem)
            # n+=rem//e
            rem = rem%e
            #print(f"rem=={rem}     n={n}.    ans={ans}")
        return ans