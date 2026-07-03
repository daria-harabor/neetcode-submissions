class Solution:
    def climbStairs(self, n: int) -> int:
        current = 0
        prev2 = 1       # only one way to get to step 1
        prev1 = 2       # two ways to get to step 2 (climb 1+1 or just climb 2)
        for i in range(3,n+1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        if n <= 2:
            return n
        else:
            return current