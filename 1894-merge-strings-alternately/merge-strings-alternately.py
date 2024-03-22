class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1=list(word1)
        w2=list(word2)
        res=""
        for i in range(min(len(word1),(len(word2)))):
            res+=word1[i]
            res+=word2[i]
        if len(word1)>len(word2):
            res+=word1[i+1:]
        else:
            res+=word2[i+1:]    
        return res