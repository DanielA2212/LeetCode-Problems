#
# @lc app=leetcode id=44 lang=python
#
# [44] Wildcard Matching
#

# @lc code=start
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        # Track the last '*' position and its string position
        starPos = -1
        starInS = 0

        iS = 0 # For srting
        jP = 0 # For pattern

        while iS < len(s):
            # If characters match or '?', move both pointers
            if jP < len(p) and (p[jP] == s[iS] or p[jP] == '?'):
                iS += 1
                jP += 1

            # If pattern has '*', track the position and move the pattern pointer
            elif jP < len(p) and p[jP] == '*':
                starPos = jP
                starInS = iS
                jP += 1

            # If there was a '*' before, go back and try to match more
            elif starPos != -1:
                jP = starPos + 1
                starInS += 1
                iS = starInS
                
            # If no match and no '*', return False
            else:
                return False

        # If more then one '*'
        while jP < len(p) and p[jP] == '*':
            jP += 1

        # If we've got to the end of the pattern it's a match
        return jP == len(p)
        
# @lc code=end

