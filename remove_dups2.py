'''Given an integer array nums sorted in non-decreasing order, remove some 
duplicates in-place such that each unique element appears at most twice. 
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some 
languages, you must instead have the result be placed in the first part of 
the array nums. More formally, if there are k elements after removing the 
duplicates, then the first k elements of nums should hold the final 
result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by 
modifying the input array in-place with O(1) extra memory.'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dictionary = {}
        remove = []
        for i,num in enumerate(nums):
            if num not in dictionary:
                dictionary[num] = 1
                #print(dictionary)
            else:
                if dictionary[num] < 2:
                    dictionary[num] +=1
                    #count +=1
                else:
                    #print(i)
                    #nums.pop(i)
                    #nums.append('_')
                    #count +=1
                    remove.append(i)
        for i, num in enumerate(remove):
            remove[i] = num - i
        for num in remove:
            nums.pop(num)            
        #print(dictionary)
        #print(nums)
        return len(nums)
