"""
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring
consisting of non-space characters only.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        s = s.strip().split()
        return len(s[-1])
        """
        flag = False
        i = -1
        res = 0
        while len(s) + i != -1:
            if s[i].isalpha():
                flag = True
            elif s[i].isspace() and flag:
                return res
            if flag:
                res += 1
            i -= 1
        return res
            


def main():
    assert Solution().lengthOfLastWord('hello world') == 5
    assert Solution().lengthOfLastWord('   fly me   to   the moon  ') == 4
    assert Solution().lengthOfLastWord('a') == 1
    assert Solution().lengthOfLastWord('a ') == 1
    assert Solution().lengthOfLastWord(' a ') == 1
    assert Solution().lengthOfLastWord('a a') == 1
    assert Solution().lengthOfLastWord('  ') == 0


if __name__ == '__main__':
    main()
