'''Given two binary strings a and b, return their sum as a binary 
string.'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def to_decimal(astr):
            astr = astr[::-1]
            pos = 0
            number = 0
            for digit in astr:
                if digit == '1':
                    number += 2**pos
                pos +=1
            return number
        def number_to_binary(number):
            if number == 0:
                return "0"

            binary_digits = []
            while number > 0:
                remainder = number % 2
                binary_digits.append(str(remainder))
                number //= 2
            binary_representation = ''.join(binary_digits[::-1])
            return binary_representation
        
        n1 = to_decimal(a)
        n2 = to_decimal(b)
        n = n1+n2
        return number_to_binary(n)
