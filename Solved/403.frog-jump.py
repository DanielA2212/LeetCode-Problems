#
# @lc app=leetcode id=403 lang=python
#
# [403] Frog Jump
#

# @lc code=start
class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        # @lc code=start
class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """

        # A dict to store possible jump sizes for each stone
        jumpsDict = {stone: set() for stone in stones}
        jumpsDict[0].add(0)  # Start at the first stone with a jump size of 0

        for stone in stones:
            for jump in jumpsDict[stone]:

                # Try jumos of k-1, k, k+1
                for nextJump in [jump - 1, jump, jump + 1]:
                    if (nextJump > 0) and (stone + nextJump in jumpsDict):
                        jumpsDict[stone + nextJump].add(nextJump)

        # Return true if the last stone has any possible jump sizes
        return len(jumpsDict[stones[-1]]) > 0
        
# @lc code=end

