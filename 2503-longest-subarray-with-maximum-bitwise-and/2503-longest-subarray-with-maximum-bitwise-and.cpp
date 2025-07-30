class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int a=nums[0],res=0;
        for(int i=1;i<nums.size();++i)
            a=max(a,nums[i]);
        for(int i=0;i<nums.size();++i)
        {
            if(nums[i]==a){
            int j=i;
            while(i<nums.size() && nums[i]==a)
                ++i;
            res=max(i-j,res);
            }
        }
        return res;
    }
};