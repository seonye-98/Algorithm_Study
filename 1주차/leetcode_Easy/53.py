'''
53.Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

'''

class Solution:
   def maxSubArray(self, nums):
       for i in range(1, len(nums)):
           # 부분합
           nums[i] = nums[i] + (nums[i - 1] if nums[i - 1] > 0 else 0)
       # 부분합들의 최대값
       return max(nums)

'''
nums  =  [-2,  1,  -3,  4,  -1,  2,  1,  -5,  4]
부분합  =  [-2,  1,  -2,  4,   3,  5,  6,  1,   5]
0번째 인덱스의 값 -2 : -2가 최대값
1번째 인덱스의 값 1 : 이전의 값이 음수이기때문에 해당요소가 최대값 -> 1
2번째 인덱스의 값 -3 : 이전의 부분합 + 해당요소가 최대값 -> -2
3번째 인덱스의 값 4 : 이전의 값이 음수이기때문에 해당요소가 최대값 -> 4
4번째 인덱스의 값 -1 : 이전의 부분합 + 해당요소가 최대값 -> 3
5번째 인덱스의 값 2 : 이전의 부분합 + 해당요소가 최대값 -> 5
6번째 인덱스의 값 1 : 이전의 부분합 + 해당요소가 최대값 -> 6
7번째 인덱스의 값 -5 : 이전의 부분합 + 해당요소가 최대값 -> 1
8번째 인덱스의 값 4 : 이전의 부분합 + 해당요소가 최대값 -> 5
이렇게 이전의 부분합이 음수이면 버리고 음수가 아니면 전의 부분합과 해당요소를 더하여 부분합을 구하고 최종적으로 부분합의 최대값을 구하면 연속적인 배열 합의 최대값을 구할 수 있다.

여기서 중요한 것은 nums 리스트를 반복하면서 하위배열요소의 최대값을 구하여 똑같은 하위배열의 중복계산을 하지않아 시간복잡도 O(n)에 푼 것이다. -> Dynamic Programming

출처 : https://velog.io/@wind1992/Leetcode-53.-Maximum-Subarray
'''