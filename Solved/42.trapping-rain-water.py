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
        left_max = [0] * n
        right_max = [0] * n
        left_max[0] = height[0]

        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        trapped_water = 0
        for i in range(n):
            trapped_water += min(left_max[i], right_max[i]) - height[i]

        return trapped_water
        
# @lc code=end

