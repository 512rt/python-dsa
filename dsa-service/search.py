

from typing import List


class Search:
    def __init__(self):
        pass


    def load_run_search(self):
        nums = [1,2,3,4,5,6,7,8,9]
        
        result = self.binary_search(nums, 7)

        print(f"binary search target is {result}")

        pass

    #region 704. Binary Search - Easy
    
    # Given an array of integers nums which is sorted in ascending order, 
    # and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
    # You must write an algorithm with O(log n) runtime complexity.
    # Example 1:
    # Input: nums = [-1,0,3,5,9,12], target = 9
    # Output: 4
    # Explanation: 9 exists in nums and its index is 4
    # Example 2:

    # Input: nums = [-1,0,3,5,9,12], target = 2
    # Output: -1
    # Explanation: 2 does not exist in nums so return -1
    # Constraints: 
    # 1 <= nums.length <= 104
    # -104 < nums[i], target < 104
    # All the integers in nums are unique.
    # nums is sorted in ascending order.
    
    #endregion
    def binary_search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)

        while left <= right:

            mid = left + (right - left)//2

            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    


        