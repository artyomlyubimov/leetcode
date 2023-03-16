"""
You are given a large integer represented as an integer array digits, where each digits[i]
is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        count = -1
        while count + len(digits) != -1:
            digits[count] += 1
            if digits[count] == 10:
                digits[count] = 0
                count -= 1
                continue
            return digits
        digits.insert(0, 1)
        return digits
    

def main():
    assert Solution().plusOne([1,2,3]) == [1, 2, 4]
    assert Solution().plusOne([9]) == [1, 0]
    assert Solution().plusOne([4,3,2,1]) == [4,3,2,2]


if __name__ == '__main__':
    main()