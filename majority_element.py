'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ 
times. You may assume that the majority element always exists in the 
array.'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums)//2 +1
        dic = {}
        if len(nums) == 1:
            return nums[0]
        for num in nums:
            if num in dic:
                dic[num]+= 1
                if dic[num] == majority:
                    return num
            else:
                dic[num] = 1
