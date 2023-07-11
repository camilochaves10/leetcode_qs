'''Given two strings needle and haystack, return the index of the first 
occurrence of needle in haystack, or -1 if needle is not part of 
haystack.'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ans = -1
        idx = len(needle)
        for i, letter in enumerate(haystack):
            if haystack[i:i+idx] == needle:
                return i
        return ans
