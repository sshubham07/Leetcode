class Solution {
public:
    bool winner(int a,int b,int initial,int last,bool check,vector<int> &nums)
    {
        if(initial>last)
        {
            if(a>=b)
                return true;
            return false;
        }
        if(check)
            return(winner(a+nums[initial],b,initial+1,last,false,nums) || winner(a+nums[last],b,initial,last-1,false,nums));
         return(winner(a,b+nums[initial],initial+1,last,true,nums) && winner(a,b+nums[last],initial,last-1,true,nums));
    }
    bool predictTheWinner(vector<int>& nums) {
        int a=0,b=0,initial=0, last=nums.size()-1;
        bool check=true;
        return winner(a,b,initial,last,check,nums);
    }
};