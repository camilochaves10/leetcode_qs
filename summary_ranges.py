'''You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in 
the array exactly. That is, each element of nums is covered by exactly one 
of the ranges, and there is no integer x such that x is in one of the 
ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b'''

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)== 0:
            return []
        prep = [nums[0]]
        prev = nums[0]
        for i, val in enumerate(nums[1:]):
            if val - prev != 1:
                prep.append('_')
            prep.append(val)
            prev = val
        print(prep)
        left = False
        right = False
        l = 0
        r = 0
        ans = []
        st = ''
        for i, val in enumerate(prep):
            if left is False and val != '_':
                l = val
                left = True
                
            elif left and val != '_':
                right = True
                r = val
                #continue
            elif left and right and val == '_':
                left = False
                right = False
                ans.append(f'{l}->{r}')
                #continue  
            elif left and right is False and val == '_' :
                left = False
                ans.append(f'{l}')

            elif i == len(prep)-1 and val != '_' :
                ans.append(f'{val}')
        if left and right is False:
            ans.append(f'{l}')

        if left and right:
            ans.append(f'{l}->{r}')

        #print(ans, l, r, left, right)
        return ans
