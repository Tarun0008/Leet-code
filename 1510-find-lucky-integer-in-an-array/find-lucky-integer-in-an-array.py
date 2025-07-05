class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c={}
        m=[]
        for i in arr:
            if i in c:
                c[i]+=1
            else:
                c[i]=1
        for key,value in c.items():
            if key==value:
                m.append(key)
        if m:
            return max(m)
        else:
            return -1
        # m=max(c[key])
        # if(c[key]==c[value])
        # print(c)