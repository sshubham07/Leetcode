class Solution {
    int ans;
    vector<int>dx,dy;
public:
    void calc(vector<vector<int>>& g, vector<vector<int>>& vis, int i,int j,bool &check)
    {
          vis[i][j]=1;
          for(int k=0;k<4;++k)
          {
              if(dx[k]+i<0 || dx[k]+i>=g.size() || dy[k]+j<0 || dy[k]+j>=g[0].size())
               check=true;
              else if(vis[i+dx[k]][j+dy[k]]==0 && g[i+dx[k]][j+dy[k]]==0)
                calc(g,vis,i+dx[k],j+dy[k],check);
          }
    }
    int closedIsland(vector<vector<int>>& g) {
        ans=0;
        vector<vector<int>>vis(g.size(),vector<int>(g[0].size(),0));
        dx={1,0,-1,0};
        dy={0,1,0,-1};
        for(int i=0;i<g.size();++i)
        {
            for(int j=0;j<g[0].size();++j)
            {
                if(g[i][j]==0 && vis[i][j]==0)
                {
                    bool check=false;
                    calc(g,vis,i,j,check);
                    if(!check)
                    ++ans;
                }
            }
        }
        return ans;
        
    }
};