"""
Given a string s, find the length of the longest 
substring
without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = ''
        letters = dict()
        prop_index = 0
        maximum = 0

        for i, ch in enumerate(s):
            if (ch in letters) and (letters[ch] >= prop_index):
                maximum = max(maximum, len(string))
                prop_index = letters[ch]
                string = s[prop_index:i]
            else:
                string += ch
            letters[ch] = i
        return max(maximum, len(string))


def main(): 
    assert Solution().lengthOfLongestSubstring(s='bbtablud') == 6
    assert Solution().lengthOfLongestSubstring(s='tmmzuxt') == 5
    assert Solution().lengthOfLongestSubstring(s='dvdf') == 3
    assert Solution().lengthOfLongestSubstring(s='abcabcbb') == 3
    assert Solution().lengthOfLongestSubstring(s='bbbbb') == 1
    assert Solution().lengthOfLongestSubstring(s='pwwkew') == 3


if __name__ == '__main__':
    main()
