class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        def helper(s: str, f: str, se: str, v: int):
            stack=[]
            t=0
            for ch in s:
                if stack and stack[-1]==f and ch==se:
                    stack.pop()
                    t+=v
                else:
                    stack.append(ch)
            return "".join(stack),t
        
        if x>y:
            s,score_1= helper(s,'a','b',x)
            s,score_2=helper(s,'b','a',y)
        else:
        
            s,score_1= helper(s,'b','a',y)
            s,score_2=helper(s,'a','b',x)
        return score_1+score_2


