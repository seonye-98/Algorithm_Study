"""
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

import itertools

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        iter = itertools.combinations(nums, 2)
        answer = []
        for item in iter:
            if sum(item) == target:
                for _item in list(item):
                    if nums.count(_item) > 1:
                        answer.append(nums.index(_item))
                        nums.remove(_item)
                        answer.append(nums.index(_item)+1)
                        break
                    else:
                        answer.append(nums.index(_item))
                break
                
        return answer


'''
모범답안: Hash
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        
        for idx, val in enumerate(nums):
            diff = target - val
            
            if diff in seen:
                return [seen[diff], idx]
            else:
                seen[val] = idx
                
        return [-1, 1]
'''