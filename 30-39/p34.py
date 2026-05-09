#!/usr/bin/env python3
import math

# PROBLEM
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: 1! and 2! are not included due to their simplicity

# SOLUTION
# Since 8! leads to a 7 digit value, we can establish that the upper bound of this should be 7! = 2,540,160

# Precompute factorials for efficiency
fact_map = {str(i): math.factorial(i) for i in range(10)}
    
factorions = []
# Exclude 1 and 2, so start from 10
for num in range(10, 2540161):
    # Brute force all combinations to find what matches the pattern
    if num == sum(fact_map[digit] for digit in str(num)):
        factorions.append(num)
            
# Print the resulting sum of the found number(s)
print(sum(factorions)) # Result: 