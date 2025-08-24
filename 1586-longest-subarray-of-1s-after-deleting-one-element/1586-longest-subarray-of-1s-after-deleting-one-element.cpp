class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int zero=0,ans=0,s=0;
        for(int i=0;i<nums.size();++i)
        {
            if(nums[i]==0)
             zero+=1;
            while(zero>1)
            {
                if(nums[s]==0)
                 --zero;
                ++s;
            }
            if(zero==1 || zero==0)
             ans=max(ans,i-s);
        }
        return ans;
    }
};
