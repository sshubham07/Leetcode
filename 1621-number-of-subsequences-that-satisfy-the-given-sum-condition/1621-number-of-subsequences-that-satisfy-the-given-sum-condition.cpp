#define mod 1000000007
class Solution {
public:
    int numSubseq(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
         int l=0,h=nums.size()-1;
        int c=0;
        vector<int>pows(nums.size(),1);
        for(int i=1;i<nums.size();++i)
            pows[i]=(pows[i-1]*2)%mod;
        while(l<=h)
        {
            if(nums[l]+nums[h]<=target)
            {
                c+=pows[h-l];
                c%=mod;
                ++l;
            }
            else
                --h;
        }
        return c;
    }
};