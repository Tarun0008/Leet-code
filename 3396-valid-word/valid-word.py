class Solution:
    def isValid(self, word: str) -> bool:
        c=0
        vowels = 'aeiouAEIOU'
        hc,hv=False,False
        if len(word)<3:
            return False
        
        for char in word:
            if not char.isalnum():
                return False
            if char.isalpha():
                if char in vowels:
                    hv=True
                else:
                    hc=True
        return hv and hc
            
