#
# @lc app=leetcode id=135 lang=python
#
# [135] Candy
#

# @lc code=start
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """

        n = len(ratings)
        if n == 0:
            return 0
        if n == 1:
            return 1



        # candies = [1] * n

        # for i in range(1, n):
        #     if ratings[i] > ratings[i-1]:
        #         candies[i] = candies[i-1] + 1

        # for i in range(n-2, -1, -1):
        #     if ratings[i] > ratings[i+1]:
        #         candies[i] = max(candies[i], candies[i+1] + 1)

        # return sum(candies)
        
# @lc code=end

