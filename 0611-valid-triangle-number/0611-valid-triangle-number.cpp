class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        int count=0;
        if(nums.size()<3)
            return 0;
        sort(nums.begin(),nums.end());
        int i=0;
        while(nums[i]==0)
            ++i;
        for( ;i<nums.size()-2;++i)
        {
            for(int j=i+1;j<nums.size()-1;++j)
            {
                int l=j+1,h=nums.size()-1,mid,k=nums[i]+nums[j];
                while(l<=h)
                {
                    mid=l+(h-l)/2;
                    if(nums[mid]>=k)
                        h=mid-1;
                    else 
                        l=mid+1;
                }
                count=count+(h-j);
            }
        }
        return count;
    }
};