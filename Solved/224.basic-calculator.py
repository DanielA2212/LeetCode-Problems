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

        # Initialize a stack to handle parentheses
        stack = []

        result = 0
        num = 0
        sign = 1  # 1 for positive, -1 for negative
        
        for char in s:

            # If the character is a digit, build the number
            if char.isdigit():
                num = num * 10 + int(char)
            
            elif char == '+':
                result += sign * num

                # Reset num and set sign to positive
                num = 0
                sign = 1
            
            elif char == '-':
                result += sign * num

                # Reset num and set sign to negative
                num = 0
                sign = -1
            
            elif char == '(':
        
                # Push current result and sign to stack
                stack.append((result, sign))

                # Reset result and sign for the new expression inside parentheses
                result = 0
                sign = 1
            
            elif char == ')':

                # Add the last number to result with proper sign
                result += sign * num
                num = 0

                # Pop the previous result and sign from stack
                prev_result, prev_sign = stack.pop()

                # Combine the result inside parentheses with the previous result
                result = prev_result + prev_sign * result
        
        # Add the last number to result
        return result + sign * num
        
# @lc code=end

