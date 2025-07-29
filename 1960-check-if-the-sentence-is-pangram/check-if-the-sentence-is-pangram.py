class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s=set(sentence)
        if len(s)==26:
            return True
        else:
            return False
        
        # return set('abcdefghijklmnopqrstuvwxyz').issubset(set(sentence.lower()))