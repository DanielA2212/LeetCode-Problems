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
            palindromes = set()  # Using set to avoid duplicates
            half_length = (n + 1) // 2  # Calculate half length for palindrome generation

            # Range for the first half of the palindrome
            start = 10**(half_length - 1)
            end = 10**half_length

            # Generate palindromes by mirroring the first half
            for first_half in range(start, end):
                s = str(first_half)
                
                # For even length palindromes
                if n % 2 == 0:
                    candidate = int(s + s[::-1]) # Mirroring the first half
                # For odd length palindromes
                else:
                    candidate = int(s + s[-2::-1]) # Mirroring the first half excluding the last digit
                
                if candidate % k == 0:
                    palindromes.add(candidate)

            return palindromes
        
        # Build a tuple of digit counts for a given number
        def get_digit_count_tuple(num):
            count = [0] * 10  # Initialize count for digits 0-9
            # Count occurrences of each digit
            for d in str(num):
                count[int(d)] += 1
            return tuple(count)  # Return as tuple for hashability

        # Simple factorial function
        def factorial(n):
            fact = 1
            # Multiply numbers from 2 to n
            for i in range(2, n + 1):
                fact *= i
            return fact
        
        # Calculate number of distinct permutations for given digit counts
        def count_permutations(count_tuple, total_digits):
            total = factorial(total_digits)  # Total permutations without considering duplicates
            
            # Adjust for duplicate digits using factorial of counts
            for c in count_tuple:
                total //= factorial(c)  # Permutation formula that we learned in probability class
            return total

        # Calculate invalid permutations where the number would start with 0
        def count_invalid_with_leading_zero(count_tuple, total_digits):
            if count_tuple[0] == 0:
                return 0  # No zeros to worry about

            # Adjust counts for leading zero case
            count_list = list(count_tuple)
            count_list[0] -= 1  # Use one 0 as the first digit

            # Calculate permutations with leading zero
            total = factorial(total_digits - 1)
            for c in count_list:
                total //= factorial(c)  # Permutation formula that we learned in probability class
            return total

        # Main logic starts here
        palindromic_numbers = generate_palindromes(k, n)  # Generate palindromes divisible by k
        seen = set()  # Track seen digit count patterns
        result = 0  # Final result accumulator

        # Process each palindrome
        for pal in palindromic_numbers:
            count_tuple = get_digit_count_tuple(pal) 
            
            # Skip if we've already processed this digit pattern
            if count_tuple in seen:
                continue

            seen.add(count_tuple)  # Mark this pattern as seen

            # Calculate valid permutations
            total_perms = count_permutations(count_tuple, n)  # All permutations - including leading zeros
            invalid_perms = count_invalid_with_leading_zero(count_tuple, n)  # Only leading zeros permutations

            # Add valid permutations to result
            result += total_perms - invalid_perms

        return result

# @lc code=end