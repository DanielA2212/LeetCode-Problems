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

        #write fumctions manually (or take and give credit + URL)

        overall_gcd = reduce(gcd, nums)

        return overall_gcd == 1
        
# @lc code=end

