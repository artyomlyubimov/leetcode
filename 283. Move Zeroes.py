"""
Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""


class Solution:
    def moveZeroes(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.append(0)
                nums.remove(0)
        return nums


def main():
    assert Solution().moveZeroes([0, 0, 1, 2, 3, 0, 1]) == [1, 2, 3, 1, 0, 0, 0]


if __name__ == '__main__':
    main()
