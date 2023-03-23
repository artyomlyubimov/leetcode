"""
Given a non-negative integer x, return the square root of x 
rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        i, count = 1, 1
        while x > i:
            x -= i
            i += 2
            count += 1
        return count if x == i else count - 1
    

def main():
    assert Solution().mySqrt(4) == 2
    assert Solution().mySqrt(8) == 2
    assert Solution().mySqrt(9) == 3
    assert Solution().mySqrt(16) == 4
    assert Solution().mySqrt(225) == 15
    assert Solution().mySqrt(230) == 15


if __name__ == '__main__':
    main()
