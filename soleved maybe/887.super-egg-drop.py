#
# @lc app=leetcode id=887 lang=python
#
# [887] Super Egg Drop
#

# @lc code=start
class Solution(object):
    def superEggDrop(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """

        # Credit to: https://stackoverflow.com/questions/26560726/python-binomial-coefficient
        # Calculates the binomial coefficient C(m, k)
        # which represents the number of ways to choose k items from m items

        def binocoe(m, k):
            
            if k > m:
                return 0
            res = 1
            for i in range(k):
                res = res * (m - i) // (i + 1)
            return res


        # credit to: https://stackoverflow.com/a/212413 for binary search
        
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            total = 0
            for i in range(1, k + 1):
                total += binocoe(mid, i)
                if total >= n:
                    break
            if total >= n:
                right = mid
            else:
                left = mid + 1

        return left
# @lc code=end

