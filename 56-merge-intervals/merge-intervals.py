class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        merged=[intervals[0]]

        for start,end in intervals[1:]:
            last_s,last_e=merged[-1]
            if start<=last_e:
                merged[-1][1]=max(end,last_e)
            else:
                merged.append([start,end])
        return merged
        