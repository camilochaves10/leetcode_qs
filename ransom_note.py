'''Given two strings ransomNote and magazine, return true if ransomNote 
can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = {}
        for ch in magazine:
            if ch in mag:
                mag[ch] += 1
            else:
                mag[ch] = 1
        for ch in ransomNote:
            if ch in mag:
                if mag[ch] > 0:
                    mag[ch] -= 1
                else:
                    return False

            else:
                return False
        return True
