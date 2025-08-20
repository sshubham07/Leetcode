class Solution {
public:
    int calc(vector<vector<int>>&dp,vector<vector<int>>& matrix,int r,int c)
    {
        if(r==matrix.size()||c==matrix[0].size() || matrix[r][c]==0)
            return 0;
        if(dp[r][c]!=-1)
            return dp[r][c];
        return dp[r][c]=1+min({calc(dp,matrix,r,c+1),calc(dp,matrix,r+1,c+1),calc(dp,matrix,r+1,c)});
        
    }
    int countSquares(vector<vector<int>>& matrix) {
        vector<vector<int>>dp(matrix.size(),vector<int>(matrix[0].size(),-1));
        int square=0;
        for(int i=0;i<matrix.size();++i)
        {
            for(int j=0;j<matrix[0].size();++j)
            {
                if(matrix[i][j]==1)
                square+=calc(dp,matrix,i,j);
            }
        }
        return square;
    }
};