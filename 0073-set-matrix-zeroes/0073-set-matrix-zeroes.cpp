class Solution {
public:
    void calc(vector<vector<int>>&zeros, vector<vector<int>>& matrix)
    {
        for(int i=0;i<zeros.size();++i)
        {
            int row=zeros[i][0],col=zeros[i][1];
            for(int k=0;k<matrix[0].size();++k)
                matrix[row][k]=0;
            for(int k=0;k<matrix.size();++k)
                matrix[k][col]=0;
        }
    }
    void setZeroes(vector<vector<int>>& matrix) {
        vector<vector<int>>zeros;
        for(int i=0;i<matrix.size();++i)
        {
            for(int j=0;j<matrix[i].size();++j)
            {
                if(matrix[i][j]==0)
                    zeros.push_back({i,j});
            }
        }
        calc(zeros,matrix);
    }
};