'''Write a function to find the longest common prefix string amongst an 
array of strings.

If there is no common prefix, return an empty string "".'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        if prefix == '':
            return prefix
        for word in strs[1:]:
            if word == '':
                return word
            for i,letter in enumerate(word):
                print(letter, prefix)  
                if i >= len(prefix):
                    prefix = prefix[:i]
                    break
                if letter != prefix[i]:
                    prefix = prefix[:i]
                    break
                if len(word) < len(prefix):
                    strs.append(prefix)
                    prefix = word
        for word in strs:
            if word == '':
                return word
            for i,letter in enumerate(word):
                print(letter, prefix)  
                if i >= len(prefix):
                    prefix = prefix[:i]
                    break
                if letter != prefix[i]:
                    prefix = prefix[:i]
                    break
                if len(word) < len(prefix):
                    strs.append(prefix)
                    prefix = word
            print(strs)

        return prefix
