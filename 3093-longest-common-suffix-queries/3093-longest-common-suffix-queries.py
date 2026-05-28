import heapq
class Trie:
    def __init__(self):
        self.children = [None]*26
        self.properties=[]  #lenth,index
        self.end=False
    def insert(self,index,word,word_index):
        if index==len(word):
            self.end=True
            return
        if self.children[ord(word[index])-97] is None:
            temp = Trie()
            self.children[ord(word[index])-97] = temp
        temp = self.children[ord(word[index])-97]
        heapq.heappush(temp.properties,(len(word),word_index))
        temp.insert(index+1,word,word_index)
    def find_common_index(self,index,word):
        if index==len(word) or self.children[ord(word[index])-97] is None:
            if len(self.properties)==0:
                return -1
            print(self.properties[0][1])
            return self.properties[0][1]
        return self.children[ord(word[index])-97].find_common_index(index+1,word)
        
class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        ans = []
        t = Trie()
        short=len(wordsContainer[0])
        short_index=0
        for i in range(1,len(wordsContainer)):
            if len(wordsContainer[i])<short:
                short = len(wordsContainer[i])
                short_index = i

        for i in range(len(wordsContainer)):
            t.insert(0,wordsContainer[i][::-1],i)
        for i in range(len(wordsQuery)):
            temp = t.find_common_index(0,wordsQuery[i][::-1])
            if temp==-1:
                ans.append(short_index)
            else:
                ans.append(temp)
        return ans
        