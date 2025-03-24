class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:

        meetings.sort()
        print(meetings)
        nm=[]
        wd=0

        for start,end in (meetings):
            if not nm or nm[-1][1]<start:
                nm.append([start,end])
            else:
                nm[-1][1]=max(nm[-1][1],end)
        print(nm)
        for start,end in nm:
            wd+=end-start+1
        return days-wd

