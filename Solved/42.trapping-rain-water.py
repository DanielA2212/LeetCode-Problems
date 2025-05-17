#
# @lc app=leetcode id=42 lang=python
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if not height:
            return 0

        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n

        # Fill the leftMax array
        # leftMax[i] represents the maximum height to the left of index i
        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        # Fill the rightMax array
        # rightMax[i] represents the maximum height to the right of index i
        rightMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        trapped_water = 0
        for i in range(n):

            # Water trapped at current index is the minimum of left and right max heights minus the current height (which is the base)
            trapped_water += min(leftMax[i], rightMax[i]) - height[i]

        return trapped_water
# @lc code=end

