class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        ans=[]
        for i,j in zip(word1,word2):
            ans.append(i)
            ans.append(j)
        
        ans.append(word1[len(word2):])
        ans.append(word2[len(word1):])

        return "".join(ans)

        