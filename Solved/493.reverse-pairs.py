#
# @lc app=leetcode id=493 lang=python
#
# [493] Reverse Pairs
#

# @lc code=start
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Base case: If the array is empty, there are no reverse pairs
        if not nums:
            return 0

        # Credit to: https://www.w3schools.com/dsa/dsa_algo_mergesort.php for modified merge sort
        def mergeSort(nums, left, right):

            # Base case: If the subarray has one or zero elements, no reverse pairs
            if left >= right:
                return 0

            mid = (left + right) // 2

            # Recursively count reverse pairs in the left and right halves
            count = mergeSort(nums, left, mid) + mergeSort(nums, mid + 1, right)

            j = mid + 1

            # Iterate through the left half to count reverse pairs
            for i in range(left, mid + 1):

                # Move the right pointer while nums[i] > 2 * nums[j]
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                # Add the number of valid pairs for nums[i] to the count
                count += j - (mid + 1)

            # Sort the subarray [left, right] for merging
            nums[left:right + 1] = sorted(nums[left:right + 1])

            # Return the total count in this subarray
            return count

        return mergeSort(nums, 0, len(nums) - 1)

# @lc code=end

