class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "")
        r = []
        a = len(s) % k
        if len(s)==1:
            return s.upper()
        if a:
            r.append(s[:a].upper())
            r.append("-")

        c = 0
        for i in range(a, len(s)):
            r.append(s[i].upper())
            c += 1
            if c == k and i!=len(s)-1:
                r.append("-")
                c = 0
        return ''.join(r)
