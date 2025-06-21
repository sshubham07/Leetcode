class Solution {
public:
    int minimumDeletions(string word, int k) {
        vector<int>c(26,0);
        //int maxi =0;
        for(int i=0;i<word.size();++i)
        {
            c[int(word[i])-int('a')]++;
            //maxi = max(maxi,c[int(word[i])-int('a')]);
        }
        sort(c.begin(),c.end());
        vector<int>temp;
        for(int i=0;i<26;++i)
            if(c[i] != 0)
                temp.push_back(c[i]);
        int ans = INT_MAX, maxi = temp.back();
        for(int i=0;i<= maxi;++i)
        {
            int count = 0;
            for(int j=0;j<temp.size();++j)
            {
                if(temp[j]>i+k)
                    count += temp[j]-i-k;
                else if(temp[j]<i)
                    count += temp[j];
            }
            ans = min(ans, count);
        }
        return ans;
    }
};