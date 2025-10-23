class Solution:
    def hasSameDigits(self, s: str) -> bool:
        if len(s)==2:
            return True if s[0]==s[1] else False
        temp = ""
        n = len(s)
        for i in range(1,n):
            #print(str(int(s[i-1])+(int(s[i])))%10)
            temp+= str((int(s[i-1])+(int(s[i])))%10)
        #print(temp)
        return self.hasSameDigits(temp)
        