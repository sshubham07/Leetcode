class Solution {
public:
    bool calc(int s,int e, vector<int>& p, vector<vector<vector<int>>>&dp,int c1,int c2,int chance)
    {
        if(s>e)
        {
            if(c1>c2)
                return 1;
            return 0;
        }
        if(dp[s][e][chance]!=-1)
            return dp[s][e][chance];
        if(chance==0)
            return dp[s][e][chance]=calc(s+1,e,p,dp,c1,c2+p[s],1)
            |calc(s,e-1,p,dp,c1,c2+p[e],1);
        return dp[s][e][chance]=calc(s+1,e,p,dp,c1+p[s],c2,0)|calc(s,e-1,p,dp,c1+p[e],c2,0);
    }
    bool stoneGame(vector<int>& p) {
        vector<vector<vector<int>>>dp(p.size()+1,vector<vector<int>>(p.size()+1,vector<int>(2,-1)));
        return calc(0,p.size()-1,p,dp,0,0,1);
    }
};
