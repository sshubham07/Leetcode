class Solution {
public:
    int minInsertions(string s) {
        int count=0,stack=0;
        for(int i=0;i<s.size();++i)
        {
            if(s[i]=='(')
                stack++;
            else
            {
                if(stack>0 && i+1<s.size() && s[i+1]==')')
                    ++i;
                else if(stack==0 && i+1<s.size() && s[i+1]==')')
                {
                    ++i;
                    count+=1;
                }
                else if(stack>0 &&(i+1==s.size()|| s[i+1]=='('))
                {
                    count+=1;
                }
                 else if(stack==0 &&(i+1==s.size()|| s[i+1]=='('))
                {
                    count+=2;
                }
                if(stack>0)
                    --stack;
            }
        }
        count+=(2*stack);
        return count;
    }
};