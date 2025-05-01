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
        
        avg = total // n
        maxMoves = 0
        currSum = 0

        for i in range(n):
            
            # currSum is the excess of machines[i] over avg
            currSum += machines[i] - avg
            maxMoves = max(maxMoves, abs(currSum), machines[i] - avg) # max of current imbalance and the current machine's excess

        return maxMoves
        
# @lc code=end

