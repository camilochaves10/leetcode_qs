'''Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s 
will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single 
space.

Note that s may contain leading or trailing spaces or multiple spaces 
between two words. The returned string should only have a single space 
separating the words. Do not include any extra spaces.'''

import re
class Solution:
    def reverseWords(self, s: str) -> str:
        ans = s.split(' ')
        ans = ans[::-1]
        ans = [re.sub('\W+', '', s) for s in ans]
        ans_str = ''
        for word in ans:
            if len(word)>0:
                ans_str += word + ' '
        ans_str = ans_str.strip()
        return ans_str
