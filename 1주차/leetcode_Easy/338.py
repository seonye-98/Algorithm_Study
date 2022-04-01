'''
338. Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
'''

class Solution:
    def countBits(self, num):
        ans = [0]*(num+1)
        size = 1
        while True:
            for i in range(size):
                try:
                    ans[i+size] = ans[i]+1
                except:
                    return ans
            size *= 2