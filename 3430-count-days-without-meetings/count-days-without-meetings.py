class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:

        meetings.sort()
        nm=[]
        wd=0
        m=0

        for start,end in meetings:
            if m+1<start:
                wd+=start-(m+1)
            m=max(m,end)
                
        wd+=days-m
        return wd


