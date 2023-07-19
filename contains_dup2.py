'''Given an integer array nums and an integer k, return true if there are 
two distinct indices i and j in the array such that nums[i] == nums[j] and 
abs(i - j) <= k.'''

import numpy as np
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ans = np.array([])
        for i, val in enumerate(nums):
            if len(ans)> k:
                ans = np.delete(ans, 0)
            if val in ans:
                return True
            ans = np.append(ans,val)
            
        return False
