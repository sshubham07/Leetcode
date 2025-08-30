class Solution {
public:
    bool calc(int r, int c,vector<vector<char>>& board)
    {
        for(int i=0;i<9;++i)
        {
            if(i!=c)
            {
                if(board[r][i]==board[r][c])
                    return false;
            }  
            if(i!=r)
            {
                if(board[i][c]==board[r][c])
                    return false;
            } 
            if(((3 * (r / 3) + i / 3)!=r) || ((3 * (c / 3) + i % 3)!=c))
            {
                if(board[3 * (r / 3) + i / 3][3 * (c / 3) + i % 3] ==board[r][c])
                    return false;
            }
        }
        return true;
        
    }
    bool isValidSudoku(vector<vector<char>>& board) {
        for(int i=0;i<9;++i)
        {
            for(int j=0;j<9;++j)
            {
                if(board[i][j]!='.')
                {
                    if(!calc(i,j,board))
                        return false;
                }
            }
        }
        return true;
    }
};