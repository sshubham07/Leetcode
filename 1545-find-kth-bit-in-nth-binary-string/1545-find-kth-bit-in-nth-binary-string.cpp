class Solution {
public:
    char calc(string s, int n,int k)
    {
        if(n==0 || s.size()>=k)
        {
            cout<<s<<endl;
            return s[k-1];
        }
        string t = s+"1";
        for(int i=s.size()-1;i>=0;--i)
        {
            if(s[i]=='1')
                t+='0';
            else
                t+='1';
        }
        return calc(t,n-1,k);
    }
    char findKthBit(int n, int k) {
        string s= "0";
        return calc(s,n-1,k);
    }
};