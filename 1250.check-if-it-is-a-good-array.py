#
# @lc app=leetcode id=1250 lang=python
#
# [1250] Check If It Is a Good Array
#

# @lc code=start
class Solution(object):
    def isGoodArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from math import gcd
        from functools import reduce

        # Calculate the GCD of all numbers in the array
        overall_gcd = reduce(gcd, nums)

        # If the GCD is 1, return True; otherwise, return False
        return overall_gcd == 1
        
# @lc code=end

