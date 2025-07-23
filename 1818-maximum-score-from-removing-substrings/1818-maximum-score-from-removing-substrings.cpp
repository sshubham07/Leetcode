class Solution {
public:
    int maximumGain(string s, int x, int y) {
        int res=0;
        stack<char>st;
        if(x>=y)
        {
            for(int i=0;i<s.size();++i)
            {
                if(st.size()==0)
                    st.push(s[i]);
                else if(st.top()=='a' && s[i]=='b')
                {
                    st.pop();
                    res+=x;
                }
                else
                    st.push(s[i]);
            }
            s="";
            while(st.size())
            {
                s+=st.top();
                st.pop();
            }
            reverse(s.begin(),s.end());
             for(int i=0;i<s.size();++i)
            {
                if(st.size()==0)
                    st.push(s[i]);
                else if(st.top()=='b' && s[i]=='a')
                {
                    st.pop();
                    res+=y;
                }
                else
                    st.push(s[i]);
            }
        }
        else
        {
            for(int i=0;i<s.size();++i)
            {
                if(st.size()==0)
                    st.push(s[i]);
                else if(st.top()=='b' && s[i]=='a')
                {
                    st.pop();
                    res+=y;
                }
                else
                    st.push(s[i]);
            }
            s="";
            while(st.size())
            {
                s+=st.top();
                st.pop();
            }
            reverse(s.begin(),s.end());
             for(int i=0;i<s.size();++i)
            {
                if(st.size()==0)
                    st.push(s[i]);
                else if(st.top()=='a' && s[i]=='b')
                {
                    st.pop();
                    res+=x;
                }
                else
                    st.push(s[i]);
            }
        }
        return res;
    }
};