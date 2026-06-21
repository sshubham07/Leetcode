import java.util.Arrays;
class Solution {

    public int maxIceCream(int[] costs, int coins) {
        int ans = 0;
        int i=0;
        Arrays.sort(costs);
        while(i<costs.length && costs[i]<=coins)
        {
            ans+=1;
            coins-=costs[i];
            i+=1;
        }
        return ans;

    }
}