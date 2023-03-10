"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ''
        for i in min(strs):
            if not all([w.startswith(result+i) for w in strs]):
                break
            result += i
        return result


def main():
    assert Solution().longestCommonPrefix(['flower', 'fly', 'flow']) == 'fl'
    assert Solution().longestCommonPrefix(['car', 'cat']) == 'ca'
    assert Solution().longestCommonPrefix(['coffee', 'tea', 'bomb']) == ''


if __name__ == '__main__':
    main()
