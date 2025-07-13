class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        p = [0]
        for i in range(len(gain)):
            p.append(p[i] + gain[i])
        return max(p)
