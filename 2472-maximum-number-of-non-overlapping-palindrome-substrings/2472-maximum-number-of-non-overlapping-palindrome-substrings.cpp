class Solution {
    vector<vector<int>>p;
public:
    bool check(int i,int j, vector<vector<int>>&dp, string &s)
    {
        if(i>=j)
            return 1;
        if(dp[i][j]!=-1)
            return dp[i][j];
        if(s[i]==s[j])
            return dp[i][j]=check(i+1,j-1,dp,s);
        return dp[i][j]=0;
    }
    int maxPalindromes(string s, int k) {
        vector<vector<int>>dp(s.size(),vector<int>(s.size(),-1));
        for(int i=0;i<=s.size()-k;++i)
        {
            for(int j=i+k-1;j<s.size();++j)
            {
                if(check(i,j,dp,s)){
                    p.push_back({i,j});
                    break;
                }
            }
        }
        //sort(p.begin(),p.end());
        if(p.size()==0)
            return 0;
        int c=0,l=p[0][1];
        for(int i=1;i<p.size();++i)
        {
            if(l>=p[i][0]){
                ++c;
                l=min(l,p[i][1]);
            }
            else
                l=p[i][1];
        }
        return p.size()-c;
    }
};