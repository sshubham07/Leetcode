bool comp(int a, int b)
{
 return (a < b);
}
class Solution {
public:
    int minimumDeletions(vector<int>& nums) {
        int i1=0,i2=0;
        for(int i=1;i<nums.size();++i)
        {
            if(nums[i1]>nums[i])
                i1=i;
            if(nums[i2]<nums[i])
                i2=i;
        }
        int b=max(i1,i2)+1;
        int c=nums.size()-min(i1,i2);
        int a=min(b,c);
        int d=min(i1,i2)+1+(nums.size()-max(i1,i2));
        return min(a,d);
    }
};