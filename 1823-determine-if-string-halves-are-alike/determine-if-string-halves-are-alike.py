class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        z = len(s) // 2
        a = s[:z]
        print(a)
        b = s[z:]
        print(b)
        
        vowels = 'aeiouAEIOU'
        v = list(vowels)  
        
        c, d = 0, 0
        
        for char in a:
            if char in v:
                c += 1
                
        for char in b:
            if char in v:
                d += 1
                
        print(c, d)
        
        return c == d