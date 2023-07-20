'''A phrase is a palindrome if, after converting all uppercase letters 
into lowercase letters and removing all non-alphanumeric characters, it 
reads the same forward and backward. Alphanumeric characters include 
letters and numbers.

Given a string s, return true if it is a palindrome, or false 
otherwise.'''

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'\W+', '', s)
        s = re.sub(r'_', '', s)
        l = 0
        r = len(s)-1
        print(s)
        while l < r:
            if s[l] == s[r]:
                l +=1
                r -= 1
            else:
                return False
        return True 
