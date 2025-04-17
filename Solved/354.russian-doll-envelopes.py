#
# @lc app=leetcode id=354 lang=python
#
# [354] Russian Doll latterelopes
#

# @lc code=start
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """

        # Credit to: https://stackoverflow.com/a/63366327
        # For Sorting the Width in ascending order and Height in descending order
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        longestStack = [] * len(envelopes)

        # Binary search, credit same as in problem 887 (https://stackoverflow.com/a/212413)
        for latter in envelopes:
            left, right = 0, len(longestStack) - 1

            # Find the first element with hight >= of the current latter height
            while left <= right:
                mid = (left + right) // 2
                if longestStack[mid][1] >= latter[1]:
                    right = mid - 1
                else:
                    left = mid + 1

            # If current latter hight larger than all elements, add it to the end
            if left == len(longestStack):
                longestStack.append(latter)
            else:
            # otherwise, replace the first element with hight >= current latter hight
                longestStack[left] = latter
                
        return len(longestStack)
    
# @lc code=end

