class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        c=0
        if ruleKey=="type":
            k=0
        
        elif ruleKey=="color":
            k=1
        else:
            k=2    

        for i in items:
            if i[k]==ruleValue:
                c+=1
        return c
        