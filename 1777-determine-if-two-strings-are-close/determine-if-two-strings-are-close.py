class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        wrd1=Counter(word1)
        wrd2=Counter(word2)

        if sorted(wrd1.values())==sorted(wrd2.values()) and wrd1.keys()==wrd2.keys():
            print(wrd1.values())
            return True
        else:
            return False
        