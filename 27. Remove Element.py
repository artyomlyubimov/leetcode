"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have
the result be placed in the first part of the array nums. More formally, if there are k elements
after removing the duplicates, then the first k elements of nums should hold the final result.
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        res = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums[i], nums[-1] = nums[-1], nums[i]
                nums.pop()
            else:
                res += 1
                i += 1
        print((res, nums))
        return (res, nums)


def main():
    assert Solution().removeElement([3, 2, 2, 3], 3) == (2, [2, 2])
    assert Solution().removeElement([3, 2, 2, 3], 2) == (2, [3, 3])
    assert Solution().removeElement([0,1,2,2,3,0,4,2], 2) == (5, [0, 1, 4, 0, 3])


if __name__ == '__main__':
    main()
