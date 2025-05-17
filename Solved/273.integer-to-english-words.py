#
# @lc app=leetcode id=273 lang=python
#
# [273] Integer to English Words
#

# @lc code=start
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num == 0:
            return "Zero"
        
        # Dictionary mapping numbers to their word equivalents
        d = {0: "",1: "One",2: "Two",3: "Three",4: "Four",5: "Five",6: "Six",7: "Seven",8: "Eight",9: "Nine",
        10: "Ten",11: "Eleven",12: "Twelve",13: "Thirteen",14: "Fourteen",15: "Fifteen",16: "Sixteen",17: "Seventeen",
        18: "Eighteen",19: "Nineteen",20: "Twenty",30: "Thirty",40: "Forty",50: "Fifty",60: "Sixty",70: "Seventy",
        80: "Eighty",90: "Ninety"
        }
        
        # Helper function to convert numbers less than 1000 to words
        def convToWords(n):
            res = ""

            # Handles hundreds
            if n >= 100:
                res += d[n // 100] + " Hundred "
                n %= 100

            # Handles (20-90)
            if n >= 20:
                res += d[n // 10 * 10] + " "
                n %= 10

            # Handles (1-19)
            if n > 0:
                res += d[n] + " "

            # Removing any trailing spaces
            return res.strip()
        
        res = ""

        # Handles billions 
        if num >= 1000000000:
            res += convToWords(num // 1000000000) + " Billion "
            num %= 1000000000

        # Handles millions 
        if num >= 1000000:
            res += convToWords(num // 1000000) + " Million "
            num %= 1000000

        # Handles thousands
        if num >= 1000:
            res += convToWords(num // 1000) + " Thousand "
            num %= 1000

        # Evrything else goes to the helpper function
        if num > 0:
            res += convToWords(num)
        
        # Clean up any extra spaces and return the result
        return ' '.join(res.split()) 
        
# @lc code=end

