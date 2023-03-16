"""
Given two binary strings a and b, return their sum as a binary string.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return "{0:b}".format(int(a, 2) + int(b, 2))
# or
#     def addBinary(self, a: str, b: str) -> str:
#         return bin(int(a, 2) + int(b, 2))[2:]


def main():
    assert Solution().addBinary('11', '1') == '100'
    assert Solution().addBinary('1010', '1011') == '10101'


if __name__ == '__main__':
    main()
