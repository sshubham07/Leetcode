class Solution {
public:
    int minScore(int n, vector<vector<int>>& r) {
        unordered_map<int,vector<vector<int>>>mp;
        for(int i=0;i<r.size();++i)
        {
            mp[r[i][0]].push_back({r[i][1],r[i][2]});
            mp[r[i][1]].push_back({r[i][0],r[i][2]});
        }
        queue<int>q;
        vector<int>vis(n+1,0);
        vis[1]=1;
        int d=INT_MAX;
        q.push(1);
        while(q.size())
        {
            int a=q.front();
            //cout<<q.front()<<endl;
            q.pop();
            //vis[a]=1;
            for(int i=0;i<mp[a].size();++i)
            {
                d=min(d,mp[a][i][1]);
                if(vis[mp[a][i][0]]==0){
                vis[mp[a][i][0]]=1;
                q.push(mp[a][i][0]);
                }
            }
        }
        //if(vis[n])
        return d;
        //return INT_MAX;
    }
};