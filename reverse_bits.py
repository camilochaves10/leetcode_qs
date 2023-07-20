'''Reverse bits of a given 32 bits unsigned integer.'''
class Solution:
    def reverseBits(self, n: int) -> int:
        #print(n)
        def to_binary(number):
            if number == 0:
                return '0'
            neg = False
            if number < 0:
                neg = True
            bits = []
            while number > 0:
                remainder = number %2
                bits.append(str(remainder))
                number //=2
            pad = 32-len(bits)
            bits.extend(['0']*pad)
            #if neg:
            #    bits.append('1')
            #else:
            #    bits.append('0')
            bits = bits[::-1]
            ans = ''.join(bits)
            return ans

        def to_number(astr):
            #neg = False
            #if astr[0] == '1':
            #    neg = True
            #astr = astr[1:]
            astr = astr[::-1]
            number = 0
            idx = 0
            for digit in astr:
                if digit == '1':
                    number += 2**idx
                idx +=1
            #if neg:
            #    number = number * -1
            return number

        print(n,to_binary(n))
        rev =to_binary(n)[::-1]
        ans = to_number(rev)
        print(rev, ans)
        return ans
