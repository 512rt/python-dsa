



from math import inf
from typing import List


class Drive:
    def __init__(self):
        pass

    # [[2,6] [12, 16]]
    def canDrive(self, history: List[List[int]], currentTime: int) -> bool:
        
        work_hours = history[0][1] - history[0][0]
        break_hours = 0
        last_worked = history[0][1]
        for i in range(1, len(history)):
            work_interval = history[i]
            if work_interval[0] - last_worked >=8:
                work_hours = 0
            else:
                work_hours += work_interval[1] - work_interval[0]
            
            last_worked = work_interval[1]
            


class Rough:
    def __init__(self):
        pass
    

    # Check if array contains a pair of duplicate values,
    # where the two duplicates are no farther than k positions from 
    # eachother (i.e. arr[i] == arr[j] and abs(i - j) + 1 <= k).
    # O(n * k)
    # sliding window
    def contains_duplicates(self)-> bool:
        nums = [1,2,3,1,4,1]
        k = 3
        
        for L in range(len(nums)):

            for R in range(L+1, min(len(nums), L+k)):
                if nums[L] == nums[R]:
                    return True

        return False

    def contains_dups2(self) -> bool:
        nums = [1,2,3,5,4,1]
        k = 3

        window = set()
        L = 0
        for R in range(len(nums)):

            if R - L + 1 > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])

        print(window)
        return False        

    # Maximum Subarray
    # Solved 
    # Given an array of integers nums, find the subarray with the largest sum and return the sum.
    # A subarray is a contiguous non-empty sequence of elements within an array.

    def max_subarry_sum(self):
        nums = [1,2,-3,-2,4,5,1,-2]
        maxSum = float(-inf)

        for i in range(len(nums)):
            curSum = 0
            for j in range(i, len(nums)):
                curSum += nums[j]
                maxSum = max(maxSum, curSum)
        
        return maxSum
    
    def max_subarry_sum2(self):
        #nums = [1,2,-3,-2,4,-5,-1,-2]
        nums = [-1,-2,-3,-2,-4,-5,-1,-2]
        maxSum = float(-inf)
        curSum = float(-inf)
        for n in nums:
            curSum = max(curSum, 0)
            curSum += n
            maxSum = max(curSum, maxSum)
        
        return maxSum