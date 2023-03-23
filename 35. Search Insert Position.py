"""
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the index 
where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] >= target else 1
        if nums[0] >= target:
            return 0
        elif nums[-1] < target:
            return len(nums)
        
        start = 0
        end = len(nums) - 1

        while end - start > 1:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid
        
        if nums[start] == target:
            return start
        return end if nums[end] == target else start + 1


def main():
    assert Solution().searchInsert([0, 1, 3, 5, 6], 0) == 0
    assert Solution().searchInsert([0, 1, 3, 5, 6], 1) == 1
    assert Solution().searchInsert([0, 1, 3, 5, 6], 3) == 2
    assert Solution().searchInsert([0, 1, 3, 5, 6], 5) == 3
    assert Solution().searchInsert([0, 1, 3, 5, 6], 6) == 4

    assert Solution().searchInsert([0, 1, 3, 5], 3) == 2
    assert Solution().searchInsert([0, 1, 3, 5], 5) == 3

    assert Solution().searchInsert([0, 1, 3, 5], 4) == 3
    assert Solution().searchInsert([0, 1, 3, 5], 6) == 4


if __name__ == '__main__':
    main()
