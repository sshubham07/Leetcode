class Solution {
public:
    int longestPalindrome(vector<string>& w) {
        int res=0;
        unordered_map<string,int>mp;
        bool flag=false;
        for(int i=0;i<w.size();++i)
        {
            mp[w[i]]++;
        }
        for(auto i:w)
        {
            string s=i;
            swap(s[0],s[1]);
            if(mp[s]>0 && mp[i]>0 && s[0]!=s[1])
            {
                mp[s]--;
                mp[i]--;
                res+=4;
            }
            else if(mp[s]>=2 && s[0]==s[1] &&mp[s]%2==0)
            {
                res+=(2*mp[s]);
                mp[s]=0;
            }
            else if(mp[s]>=1 && s[0]==s[1] && mp[s]%2==1)
            {
                res+=(2*(mp[s]-1));
                mp[s]=1;
                flag=true;
            }
        }
        if(flag)
            return res+2;
        return res;
    }
};