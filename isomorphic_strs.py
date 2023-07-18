'''Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced 
to get t.

All occurrences of a character must be replaced with another character 
while preserving the order of characters. No two characters may map to the 
same character, but a character may map to itself.'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        dic2 = {}
        for i, ch in enumerate(s):
            if ch not in dic:
                dic[ch] = t[i]
            else:
                if dic[ch] != t[i]:
                    return False
        for i, ch in enumerate(t):
            if ch not in dic2:
                dic2[ch] = s[i]
            else:
                if dic2[ch] != s[i]:
                    return False
                #else:
        ans = ''
        ans2 = ''
        #print(dic, dic2)
        for i in s:
            ans += dic[i]
        for i in t:
            ans2 += dic2[i]

        if ans == t and ans2 == s:
            return True
        return False
