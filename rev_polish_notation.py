'''You are given an array of strings tokens that represents an arithmetic 
expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of 
the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish 
notation.
The answer and all the intermediate calculations can be represented in a 
32-bit integer.
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        ls = ['+', '-', '/', '*']
        for token in tokens:
            #print(numbers)
            if token not in ls:
                numbers.append(int(token))
            else:
                if token == '+':
                    numbers[-2] = numbers[-2] + numbers[-1]
                
                elif token == '-':
                    numbers[-2] = numbers[-2] - numbers[-1]
                
                elif token == '*':
                    numbers[-2] = numbers[-2] * numbers[-1]
                
                else:
                    if numbers[-2] / numbers[-1]>0:
                        numbers[-2]= numbers[-2] // numbers[-1]
                    else:
                        #(a+(-a%b))//b
                        numbers[-2]= 
(numbers[-2]+(-numbers[-2]%numbers[-1]))//numbers[-1]
                    #numbers[-2] = numbers[-2] // numbers[-1]
                
                numbers.pop()
        return numbers[0]

