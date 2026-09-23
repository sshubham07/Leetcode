class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        int res=INT_MAX,sum=0,a=0;
        for(int i=0;i<nums.size();++i)
            sum+=nums[i];
        if(sum<x)
            return -1;
        if(sum==x)
            return nums.size();
        int i=0;
        while(a<x && i<nums.size())
        {
            a+=nums[i++];
        }
        if(a==x)
            res=i;
        --i;
        int j=nums.size()-1;
        while(i>=0)
        {
            a-=nums[i--];
            while(j>i && a<x)
            {
                a+=nums[j--];
            }
            if(a==x)
            {
                res=min(res,(int)(i+nums.size()-j));
            }
        }
        if(res==INT_MAX)
            return -1;
        return res;
        
    }
};