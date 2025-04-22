#
# @lc app=leetcode id=123 lang=python
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1 = -float('inf')
        sell1 = 0  
        
        buy2 = -float('inf')
        sell2 = 0

        for price in prices:
            # Update states in reverse to avoid overwriting

            sell2 = max(sell2, buy2 + price) 
            # The maximum of the current sell2 or selling at the current price after the second buy

            buy2 = max(buy2, sell1 - price)   
            # The maximum of the current buy2 or buying at the current price after the first sell

            sell1 = max(sell1, buy1 + price)  
            # The maximum of the current sell1 or selling at the current price after the first buy

            buy1 = max(buy1, -price)          
            # The maximum of the current buy1 or buying at the current price

        return sell2
# @lc code=end

