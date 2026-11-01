class Solution {
public:
    int minMoves(vector<int>& nums) {
        int n=nums.size(),mini=INT_MAX,sum=0;
        for(int i=0;i<nums.size();++i)
        {
            sum+=nums[i];
            mini=min(mini,nums[i]);
        }
        return sum-(mini*n);

    }
};