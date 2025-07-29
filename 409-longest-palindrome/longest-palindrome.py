class Solution:
    def longestPalindrome(self, s: str) -> int:

        ans=Counter(s)
        length=0
        od=False

        for freq in ans.values():
            if freq%2==0:
                length+=freq
            else:
                length+=freq-1
                od=True
        if od:
            length+=1
        return length