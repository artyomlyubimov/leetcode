"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
import math

class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0
        k = 1 if n%2 else 0
        for i in range(math.ceil(n/2), n+1):
            res += (math.factorial(i)) // (math.factorial(k) * math.factorial(i-k))
            k += 2
        return res


def main():
    assert Solution().climbStairs(1) == 1
    assert Solution().climbStairs(2) == 2
    assert Solution().climbStairs(3) == 3
    assert Solution().climbStairs(4) == 5


if __name__ == '__main__':
    main()
