from collections import Counter

class Solution:
    def secondHighest(self, s: str) -> int:
        digits = [int(char) for char in s if char.isdigit()]
        
        unique_digits = sorted(set(digits), reverse=True)
        if len(unique_digits) < 2:
            return -1
        
  
        return unique_digits[1]
