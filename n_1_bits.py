'''Write a function that takes the binary representation of an unsigned 
integer and returns the number of '1' bits it has (also known as the 
Hamming weight).'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        def to_binary(n):
            bits = []
            while n > 0:
                remainder = n%2
                bits.append(str(remainder))
                n //= 2
            bits = bits[::-1]
            ans = ''.join(bits)
            return ans
        binary = to_binary(n)
        hamming = 0
        for digit in binary:
            if digit == '1':
                hamming += 1
        return hamming
