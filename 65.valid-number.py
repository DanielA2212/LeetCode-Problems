#
# @lc app=leetcode id=65 lang=python
#
# [65] Valid Number
#

# @lc code=start
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) == 0:
            return False
        if len(s) == 1 and ["+","-","."] in s:
            return False
        if all(c.isalpha() for c in s):
            return False
        
        eFlag = 0
        signFlag = 0
        pointFlag = 0
        digitFlag = 0

        for letter in s:
            if letter == "e":
                if digitFlag==0 or eFlag==1 or pointFlag==1 or signFlag==1:
                    return False
            



        
# @lc code=end
