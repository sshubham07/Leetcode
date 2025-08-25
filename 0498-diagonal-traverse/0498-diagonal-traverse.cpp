class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        vector<int>res;
        int r=0,c=0,m=mat.size(),n=mat[0].size();
        bool f=true;
        while(r<m && c<n){
        if(f)
        {
           while(r>0 && c<n-1) 
           {
               res.push_back(mat[r][c]);
               --r;
               ++c; 
           }
            res.push_back(mat[r][c]);
            if(c==n-1)
                ++r;
            else
                ++c;
        }
        else
        {
            while(c>0 && r<m-1)
            {
                res.push_back(mat[r][c]);
               ++r;
               --c; 
            }
            res.push_back(mat[r][c]);
            if(r==m-1)
                ++c;
            else
                ++r;
        }
            f=!f;
        }
        return res;
    }
};