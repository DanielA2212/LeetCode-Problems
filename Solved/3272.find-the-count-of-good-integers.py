#
# @lc app=leetcode id=3272 lang=python
#
# [3272] Find The Count Of Good Integers
#

# @lc code=start
class Solution(object):
    def countGoodIntegers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        # Generate all palindromes divisible by k
        def generate_palindromes(k, n):
            palindromes = set()
            half_length = (n + 1) // 2

            start = 10**(half_length - 1)
            end = 10**half_length

            for first_half in range(start, end):
                s = str(first_half)

                if n % 2 == 0:
                    candidate = int(s + s[::-1])

                else:
                    candidate = int(s + s[-2::-1])
                
                if candidate % k == 0:
                    palindromes.add(candidate)

            return palindromes
        

        # Build a tuple of digit counts
        def get_digit_count_tuple(num):
            count = [0] * 10

            for d in str(num):
                count[int(d)] += 1

            return tuple(count)


        # Simple factorial
        def factorial(n):
            fact = 1

            for i in range(2, n + 1):
                fact *= i

            return fact
        

        # Calculate number of distinct permutations
        def count_permutations(count_tuple, total_digits):
            total = factorial(total_digits)

            for c in count_tuple:
                total //= factorial(c) # Permutation formula that we learned in probability class

            return total

        # Calculate invalid permutations where the number would start with 0
        def count_invalid_with_leading_zero(count_tuple, total_digits):
            if count_tuple[0] == 0:
                return 0  # No zeros to worry about

            # Else we have a leading zero so we need to remove it - therefore we have one less digit
            count_list = list(count_tuple)
            count_list[0] -= 1  # Use one 0 as the first digit

            total = factorial(total_digits - 1)
            for c in count_list:
                total //= factorial(c) # Permutation formula that we learned in probability class

            return total


        palindromic_numbers = generate_palindromes(k, n) # Generate palindroms divisible by k

        seen = set()
        result = 0

        for pal in palindromic_numbers:
            count_tuple = get_digit_count_tuple(pal) 

            if count_tuple in seen:
                continue

            seen.add(count_tuple)

            total_perms = count_permutations(count_tuple, n) # All permutations - including leading zeros
            invalid_perms = count_invalid_with_leading_zero(count_tuple, n) # Only leading zeros permutatio

            result += total_perms - invalid_perms


        return result

# @lc code=end