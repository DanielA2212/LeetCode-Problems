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

        # Candies array with 1 candy for each child
        candies = [1] * n


        # Give more candies to children with higher ratings than their left neighbor
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1


        # Ensure children with higher ratings than their right neighbor have more candies
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1) # Max() used to maintain the previous constraint (left bigger than right)


        return sum(candies)  
# @lc code=end