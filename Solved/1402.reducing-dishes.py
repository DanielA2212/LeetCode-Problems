#
# @lc app=leetcode id=1402 lang=python
#
# [1402] Reducing Dishes
#

# @lc code=start
class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """

        # Sort the array in ascending order
        satisfaction.sort()
        n = len(satisfaction)

        maxSum = 0
        currSum = 0
        totalSum = 0
        
        # Go from the end of the array to the beginning
        for i in range(n - 1, -1, -1):
            currSum += satisfaction[i]
            totalSum += currSum

            if totalSum > maxSum:
                maxSum = totalSum
            else:
                break
        
        return maxSum
# @lc code=end