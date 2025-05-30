class Solution {
public:
    int closestMeetingNode(vector<int>& e, int n1, int n2) {
        vector<int>d1(e.size(),INT_MAX),d2(e.size(),INT_MAX);
        queue<int>q;
        //vector<int>vis1(e.size(),0),vis2(e.size(),0);
        d1[n1]=0;
        d2[n2]=0;
        q.push(n1);
        int dis=1;
        while(q.size())
        {
            if(e[q.front()]!=-1 && d1[e[q.front()]]==INT_MAX){
            d1[e[q.front()]]=dis;
            q.push(e[q.front()]);
            }
            q.pop();
            ++dis;
        }
        q.push(n2);
        dis=1;
        while(q.size())
        {
            if(e[q.front()]!=-1 && d2[e[q.front()]]==INT_MAX){
            d2[e[q.front()]]=dis;
            q.push(e[q.front()]);
            }
            q.pop();
            ++dis;
        }
        dis=INT_MAX;
        int ans=-1;
        /*for(int i=0;i<e.size();++i)
         cout<<d1[i]<<" ";
        cout<<endl;
        for(int i=0;i<e.size();++i)
         cout<<d2[i]<<" ";*/
        for(int i=0;i<e.size();++i)
        {
            if(d1[i]!=INT_MAX && d2[i]!=INT_MAX && max(d1[i],d2[i])<dis)
            {
               dis=max(d1[i],d2[i]);
               ans=i;
            }
        }
        return ans;
        
    }
};