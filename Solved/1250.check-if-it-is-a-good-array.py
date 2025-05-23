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

        # Credit to https://stackoverflow.com/a/11175154 for the gcd function
        def gcd(a, b):
          
            while b:
                a, b = b, a%b
            return a
        
        # Credit to https://stackoverflow.com/a/9109065 for the reduce function
        # The reduce function is used to apply the gcd function cumulatively to the items of nums
        def reduce(func, iterable, start=None): 

            it = iter(iterable)
            if start is None:
                try:
                   start = next(it)
                except StopIteration:
                   raise TypeError('reduce() of empty sequence with no initial value')
            accum_value = start
            for x in it:
                  accum_value = func(accum_value, x)
            return accum_value
        
        # Compute the GCD of all numbers in the list using the reduce function
        overall_gcd = reduce(gcd, nums)
        return overall_gcd == 1
        
# @lc code=end

