class Solution {
    vector<string>temp;
public:
    void calc(string &t, int n, vector<char>&c)
    {
        if(n==0)
        {
            temp.push_back(t);
            return;
        }
        for(int i=0;i<3;++i)
        {
            if(t[t.size()-1]!=c[i])
            {
                t+=c[i];
                calc(t,n-1,c);
                t.pop_back();
            }
        }

    }
    string getHappyString(int n, int k) {
        string t="";
        vector<char> c = {'a', 'b', 'c'};
        for(int i=0;i<3;++i)
        {
             t+=c[i];
                calc(t,n-1,c);
                t.pop_back();
        }
        if(temp.size()<k)
            return "";
        sort(temp.begin(),temp.end());
        return temp[k-1];
    }
};