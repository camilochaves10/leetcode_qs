'''You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. The digits are 
ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of 
digits.'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        end = False
        carry = False
        while end is False:
            for i, val in enumerate(digits):
                if val != 9:
                    digits[i] = val+1
                    end = True  
                    break          
                else:
                    digits[i] = 0
                    #carry = True
            if end is False:
                digits.append(1)
                end = True
        return digits[::-1]
