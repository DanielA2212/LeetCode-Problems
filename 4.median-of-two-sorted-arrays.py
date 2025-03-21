#
# @lc app=leetcode id=4 lang=python
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
             return self.kth(nums1, nums2, l // 2)
        else:
             return (self.kth(nums1, nums2, l // 2) + self.kth(nums1, nums2, l // 2 - 1)) / 2.   
      #גשחגחןחשן
    
    def kth(self, a, b, k):
       if not a:
         return b[k]
       if not b:
          return a[k]
       ia, ib = len(a) // 2 , len(b) // 2
       ma, mb = a[ia], b[ib]
    
    # when k is bigger than the sum of a and b's median indices 
       if ia + ib < k:
        # if a's median is bigger than b's, b's first half doesn't include k
         if ma > mb:
              return self.kth(a, b[ib + 1:], k - ib - 1)
         else:
               return self.kth(a[ia + 1:], b, k - ia - 1)
    # when k is smaller than the sum of a and b's indices
       else:
        # if a's median is bigger than b's, a's second half doesn't include k
         if ma > mb:
              return self.kth(a[:ia], b, k)
         else:
              return self.kth(a, b[:ib], k)

        
# @lc code=end

