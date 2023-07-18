'''Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a 
letter in pattern and a non-empty word in s.'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ls = s.split(' ')
        if len(ls) != len(pattern):
            return False
        dic = {}
        dic2 = {}
        for i, ch in enumerate(pattern):
            if ch not in dic:
                dic[ch] = ls[i]
            else:
                if ch in dic and dic[ch] != ls[i]:
                    return False
        #
        for i, ch in enumerate(ls):
                if ch not in dic2:
                    dic2[ch] = pattern[i]
                else:
                    if ch in dic2 and dic2[ch] != pattern[i]:
                        return False
        
        ans = []
        ans2 = ''
        print(dic, dic2)
        for i in pattern:
            ans.append(dic[i])
        for i in ls:
            ans2 += dic2[i]
        if ans == ls and ans2 == pattern:
            return True
        
        return False
