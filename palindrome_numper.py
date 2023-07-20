'''Given an integer x, return true if x is a 
palindrome
, and false otherwise.'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        st = str(x)[::-1]
        if str(x) == st:
            return True
        return False
