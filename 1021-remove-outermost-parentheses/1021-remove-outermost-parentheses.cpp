class Solution {
public:
    string removeOuterParentheses(string s) {
        stack<char>a;
        
        int index=0;
        for(int i=0;i<s.length();i++)
        {
            if(a.size()==0)
            {
                a.push(s[i]);
            }
           else if((a.size()>0) && (a.top()=='(' && s[i]==')'))
            {
                a.pop();
                if(a.size()==0)
                {
                    s.erase(i,1);
                    s.erase(index,1);
                    index=i-1;
                    if(i==0 || i==1)
                    {
                        i=-1;
                    }
                    else
                    {
                        i=i-2;
                    }
                }
            }
            else
            {
                a.push(s[i]);
            }
        }
        return s;
        
    }
};