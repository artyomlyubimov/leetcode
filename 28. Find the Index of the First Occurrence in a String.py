"""
Given two strings needle and haystack, return the index of the first occurrence of 
needle in haystack, or -1 if needle is not part of haystack.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    

def main():
    assert Solution().strStr('sadsfgsdfgsad', 'sad') == 0
    assert Solution().strStr('sasfgsdfgsd', 'sad') == -1


if __name__ == '__main__':
    main()
