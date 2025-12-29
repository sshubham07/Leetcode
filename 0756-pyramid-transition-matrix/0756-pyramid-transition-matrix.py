class Solution:
    def make(self,bottom,d,temp,all_possibles,pos):
        if pos==len(bottom)-1:
            all_possibles.append(temp)
            return
        t = bottom[pos:pos+2]
        for i in d.get(t,[]):
            self.make(bottom,d,temp+i,all_possibles,pos+1)
    def calc(self,bottom,d):
        if len(bottom)==1:
            return True
        check = False
        temp=""
        all_possibles =[]
        self.make(bottom,d,temp,all_possibles,0)
        for i in all_possibles:
            check = check | self.calc(i,d)
            if check:
                return True
        return check
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        d={}
        for a in allowed:
            if d.get(a[0:2]) is None:
                d[a[0:2]]=[]
            d[a[0:2]].append(a[-1])
        return self.calc(bottom,d)
