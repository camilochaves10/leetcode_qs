'''Given an integer array nums, rotate the array to the right by k steps, 
where k is non-negative.'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k
        idx = []
        ans = [0]*len(nums)
        for i,num in enumerate(nums):
            if i+k < len(nums):
                idx.append(i+k)
            else:
                idx.append((i+k)%len(nums))

        for i,num in enumerate(nums):
            ans[idx[i]] = num
            #print(ans)
        for i, num in enumerate(nums):
            nums[i] = ans[i]

        #print(nums)
        return nums
