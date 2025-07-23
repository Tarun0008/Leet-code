class Solution:
    def climbStairs(self, n: int) -> int:
        def fib(k):
            a, b = 0, 1
            for _ in range(k):
                a, b = b, a + b
            return a
        return fib(n + 1)
