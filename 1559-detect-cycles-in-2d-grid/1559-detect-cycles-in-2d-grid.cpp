class Solution {
public:
    void calc(bool &check,int i,int j, vector<vector<char>>& g, vector<vector<int>>& vis,char &c,int p1,int p2)
    {
        vis[i][j]=1;
        if(check)
            return;
        if((i-1>=0 && vis[i-1][j]==1 && g[i-1][j]==c &&((i-1)!=p1 || j!=p2)) ||(i+1<g.size() && vis[i+1][j]==1 && g[i+1][j]==c &&((i+1)!=p1 || j!=p2)) ||(j-1>=0 && vis[i][j-1]==1 && g[i][j-1]==c &&(i!=p1 || (j-1)!=p2)) ||(j+1<g[0].size() && vis[i][j+1]==1 && g[i][j+1]==c &&(i!=p1 ||(j+1)!=p2)))
        {
            check=true;
            //cout<<c<<endl;
            return;
        }
        if(i-1>=0 && vis[i-1][j]==0 && g[i-1][j]==c)
            calc(check,i-1,j,g,vis,c,i,j);
        if(i+1<g.size() && vis[i+1][j]==0 && g[i+1][j]==c)
            calc(check,i+1,j,g,vis,c,i,j);
        if(j-1>=0 && vis[i][j-1]==0 && g[i][j-1]==c)
            calc(check,i,j-1,g,vis,c,i,j);
        if(j+1<g[0].size() && vis[i][j+1]==0 && g[i][j+1]==c)
            calc(check,i,j+1,g,vis,c,i,j);
    }
    bool containsCycle(vector<vector<char>>& g) {
        vector<vector<int>>vis(g.size(),vector<int>(g[0].size(),0));
        for(int i=0;i<g.size() ;++i)
        {
            for(int j=0;j<g[0].size();++j)
            {
                if(vis[i][j]==0)
                {
                    bool check =false;
                    calc(check,i,j,g,vis,g[i][j],INT_MIN,INT_MIN);
                    if(check)
                        return true;
                }
            }
        }
        return false;
    }
};