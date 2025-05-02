#
# @lc app=leetcode id=224 lang=python
#
# [224] Basic Calculator
#

# @lc code=start
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        stack = []
        result = 0
        num = 0
        sign = 1
        
        for char in s:

            if char.isdigit():
                num = num * 10 + int(char)

            elif char == '+':
                result += sign * num
                num = 0
                sign = 1

            elif char == '-':
                result += sign * num
                num = 0
                sign = -1

            elif char == '(':
                stack.append((result, sign))
                result = 0
                sign = 1

            elif char == ')':
                result += sign * num
                num = 0
                prev_result, prev_sign = stack.pop()
                result = prev_result + prev_sign * result
        
        return result + sign * num
        
# @lc code=end

