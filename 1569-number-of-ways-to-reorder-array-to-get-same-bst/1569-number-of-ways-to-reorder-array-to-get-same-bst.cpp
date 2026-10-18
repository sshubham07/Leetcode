class Solution {
    long long calc(vector<int> nums,vector<vector<long long>>&p)
    {
        if(nums.size()<=2)
         return 1;
        vector<int>left,right;
        for(int i=1;i<nums.size();++i)
        {
            if(nums[i]>nums[0])
             right.push_back(nums[i]);
            else
             left.push_back(nums[i]);
        }
        long long n=nums.size()-1,r=left.size();
        long long res=p[n][r]%1000000007;
        return ((res*(calc(left,p)%1000000007)%1000000007)*(calc(right,p)%1000000007))%1000000007;
    }
public:
    int numOfWays(vector<int>& nums) {
        vector<vector<long long>>p(1001,vector<long long>(1001,0));
        for(int i=0;i<p.size();++i)
        {
            p[i][0]=1;
            for(int j=1;j<=i;++j)
             p[i][j]=(p[i-1][j-1]+p[i-1][j])%1000000007;
        }
        return calc(nums,p)-1;
        
    }
};