#
# @lc app=leetcode id=753 lang=python
#
# [753] Cracking the Safe
#

# @lc code=start
class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
        # If n is 1, the sequence is simply all digits from 0 to k-1
        if n == 1:
            return ''.join(str(i) for i in range(k))
        
        # Set to keep track of visited combinations
        visited = set()
        result = []
        
        # Credit to: https://favtutor.com/blogs/depth-first-search-python for dfs code 
        def dfs(node):

            # Try all possible digits (0 to k-1)
            for x in map(str, range(k)): # Converts each digit to its string representation

                # Create a new combination by adding the digit
                neighbor = node + x

                if neighbor not in visited:
                    visited.add(neighbor)

                    # Move to the next node by removing the first character
                    dfs(neighbor[1:])
                    result.append(x)
        
        # A node consisting of (n-1) zeros
        start = '0' * (n-1)
        dfs(start)

        # Combine the result with the starting node
        return ''.join(result) + start
# @lc code=end