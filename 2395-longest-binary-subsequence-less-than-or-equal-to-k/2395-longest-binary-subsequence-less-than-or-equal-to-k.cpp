class Solution {
public:
    int longestSubsequence(string s, int k) {
        int res=0;
        for(int i=0;i<s.size();++i)
            if(s[i]=='0')
                ++res;
        int p=0,sum;
        for(int i=s.size()-1;i>=0;--i)
        {
            if(s[i]=='1')
            {
                auto s=pow(2,p);
                if(s>k)
                    break;
                else
                {
                    k-=s;
                    ++res;
                }
            }
            ++p;
        }
        return res;
        
    }
};