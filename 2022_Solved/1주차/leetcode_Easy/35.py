'''
35. Search Insert Position
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if target not in nums:
            nums.append(target)
            nums.sort()
        

        index = nums.index(target)
        
        
        return index

'''
Binary Search 사용
class Solution:
    def searchInsert(self, nums, target):
        
        # nums(Ascending order) 
        left=0
        right=len(nums)-1
        
        while left<=right:
            mid=(left+right)//2
            if nums[mid]>target: # Search to left
                right=mid-1
            elif nums[mid]<target: # Search to right 
                left=mid+1   
            else: # Correct
                return mid
        # Incorrect
        return left 
'''