class Solution {
public:
    int areaOfMaxDiagonal(vector<vector<int>>& dim) {
        float d=0;
        int ans =0;
        for(auto i:dim)
        {
            float diagonal = sqrt(float(i[0]*i[0] + i[1]*i[1]));
            //cout<<diagonal<<endl;
            if(diagonal>=d)
            {
                if(d== diagonal)
                ans =  max(ans,i[0]*i[1]);
                else
                    ans = i[0]*i[1];
                d = diagonal;
            }
        }
        return ans;
    }
};