'''Given two strings s and t, return true if t is an anagram of s, and 
false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase, typically using all the original letters exactly 
once.'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        dic2 = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in t:
                if i in dic2:
                    dic2[i] += 1
                else:
                    dic2[i] = 1
        if dic == dic2:
            return True
        return False
