class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in range(len(asteroids)):
            curr = asteroids[i]

            while stack and curr < 0 and stack[-1] > 0:
                if stack[-1] < -curr:
                    stack.pop()  
                    continue
                elif stack[-1] == -curr:
                    stack.pop() 
                break
            else:
                stack.append(curr)

        return stack
