class Solution {
public:
    int find(int a, vector<int>&p)
    {
        if(p[a]==a)
         return a;
        return find(p[a],p);
    }
    void make(char a, char b, vector<int>&p)
    {
        if(a>b)
         swap(a,b);
        int p1=find(int(a-'a'),p);
        int p2=find(int(b-'a'),p);
        if(p1!=p2)
        {
            p[max(p1,p2)]=min(p1,p2);
        }
    }
    string smallestEquivalentString(string s1, string s2, string b) {
        vector<int>p(26,0);
        for(int i=0;i<26;++i)
        {
            p[i]=i;
        }
        for(int i=0;i<s1.size();++i)
        {
            make(s1[i],s2[i],p);
        }
        string res="";
        unordered_map<char,char>mp;
        for(int i=0;i<b.size();++i)
        {
            int a=find(int(b[i]-'a'),p);
            res+=char(a+'a');
        }
        return res;
    }
};