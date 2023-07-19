'''Given a roman numeral, convert it to an integer.'''

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000,
                'P': 0}
        s = s + 'P'
        idx = 0 
        total = 0       
        while idx < len(s)-1:
            nxt = idx + 1
            if s[idx] == 'I' and (s[nxt] == 'V' or s[nxt] == 'X'):
                total = total + roman[s[nxt]] - roman[s[idx]]
                idx += 2
            
            elif s[idx] == 'X' and (s[nxt] == 'L' or s[nxt] == 'C'):
                total = total + roman[s[nxt]] - roman[s[idx]]
                idx += 2
            
            elif s[idx] == 'C' and (s[nxt] == 'D' or s[nxt] == 'M'):
                total = total + roman[s[nxt]] - roman[s[idx]]
                idx += 2
            
            else:
                total = total + roman[s[idx]]
                idx += 1
        return total
