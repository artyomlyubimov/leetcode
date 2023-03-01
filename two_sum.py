"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, v1 in enumerate(nums):
            for j, v2 in enumerate(nums[i+1:]):
                if v1 + v2 == target:
                    return [i, j+i+1]
                

def main():
    test1 = Solution().twoSum([3, 2, 4], 6)
    assert test1 == [1, 2], test1

    test2 = Solution().twoSum([3, 3], 6)
    assert test2 == [0, 1], test2

    test3 = Solution().twoSum([2, 7, 11, 15], 9)
    assert test3 == [0, 1], test3


if __name__ == '__main__':
    main()
