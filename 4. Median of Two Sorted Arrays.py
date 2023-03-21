"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log(m+n)).
"""

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        first = 0
        second = 0

        i = 0
        j = 0

        l1 = len(nums1)
        l2 = len(nums2)

        while i + j != (l1 + l2) // 2 + 1:
            if l1 > i and l2 > j:
                if nums1[i] < nums2[j]:
                    first, second = second, nums1[i]
                    i += 1
                else:
                    first, second = second, nums2[j]
                    j += 1
            elif l1 > i:
                first, second = second, nums1[i]
                i += 1
            else:
                first, second = second, nums2[j]
                j += 1

        res = second if (l1 + l2) % 2 else (first + second) / 2
        print(res)
        return  res



def main():
    assert Solution().findMedianSortedArrays([], [2]) == 2.0
    assert Solution().findMedianSortedArrays([], [2, 3, 4]) == 3.0
    assert Solution().findMedianSortedArrays([1, 3], [2]) == 2.0
    assert Solution().findMedianSortedArrays([1, 3], [2, 4]) == 2.5
    assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert Solution().findMedianSortedArrays([1, 2, 4, 7, 9, 90], [3, 4, 45, 46]) == 5.5


if __name__ == '__main__':
    main()
