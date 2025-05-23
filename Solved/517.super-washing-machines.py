#
# @lc app=leetcode id=517 lang=python
#
# [517] Super Washing Machines
#

# @lc code=start
class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        
        total = sum(machines)
        n = len(machines)

        # If total is not divisible by n, it's impossible to balance
        if total % n != 0:
            return -1
        
        # Calculate the target number of dresses each machine should have
        avg = total // n
        maxMoves = 0
        currSum = 0

        for i in range(n):
            
            # CurrSum is the excess of machines[i] over avg
            currSum += machines[i] - avg
            maxMoves = max(maxMoves, abs(currSum), machines[i] - avg)
            # Update the maximum number of moves:
            # 1. The absolute value of the current imbalance (total imbalance so far)
            # 2. The excess of dresses in the current machine (since it can give dresses to both left and right)

        return maxMoves
        
# @lc code=end

