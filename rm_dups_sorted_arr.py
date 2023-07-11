'''Given an integer array nums sorted in non-decreasing order, remove the 
duplicates in-place such that each unique element appears only once. The 
relative order of the elements should be kept the same. Then return the 
number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, 
you need to do the following things:

Change the array nums such that the first k elements of nums contain the 
unique elements in the order they were present in nums initially. The 
remaining elements of nums are not important as well as the size of nums.
Return k.'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr = nums[0]
        count = 1
        l = len(nums)
        for i, num in enumerate(nums):
            #print(nums)
            if i == 0:
                continue
            elif curr == nums[i]:
                nums[i] = '_'
            else:
                curr = num
                count += 1
        count2 = 0
        while count2 < l:
            if nums[count2] == '_':
                nums.pop(count2)
                l -= 1
            else:
                count2 +=1
        #print(nums, count)
        return count
