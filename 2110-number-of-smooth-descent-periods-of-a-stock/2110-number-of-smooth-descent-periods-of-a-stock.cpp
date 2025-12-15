class Solution {
public:
    long long getDescentPeriods(vector<int>& p) {
        long long c=0;
        for(int i=0;i<p.size();++i)
        {
            int k=i;
            while(i+1<p.size() && p[i+1]+1==p[i])
                ++i;
            long long n=i-k+1;
            long long temp=0;
            if(n%2==0)
            {
             temp=n;
            temp/=2;
                ++n;
            temp*=n;
            }
            else
            {
            temp=n+1;
            temp/=2;
                n;
            temp*=n; 
            }
            c+=temp;
        }
        return c;
    }
};