class Solution {
    unordered_map<int,vector<int>>mp;
public:
    bool reorderedPowerOf2(int n) {
        int p=1;
        while(p<=1000000000)
        {
            vector<int>temp(10,0);
            int a=p;
            while(a)
            {
                temp[a%10]++;
                a/=10;
            }
            mp[p]=temp;
            p*=2;
        }
        vector<int>temp(10,0);
        while(n)
            {
                temp[n%10]++;
                n/=10;
            }
        for(auto i:mp)
            if(i.second==temp)
                return true;
        return false;
        
    }
};