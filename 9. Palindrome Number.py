"""
Given an integer x, return true if x is a 
palindrome, and false otherwise.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]
    

def main():
    assert Solution().isPalindrome(121) == True
    assert Solution().isPalindrome(-121) == False
    assert Solution().isPalindrome(10) == False


if __name__ == '__main__':
    main()
