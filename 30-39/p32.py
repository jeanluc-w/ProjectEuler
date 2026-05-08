#!/usr/bin/env python3

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit
# number, 15234, is 1 through 5 pandigital.
# 
# The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9
# pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# 
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

# Handles checking two numbers to see if it matches the pattern from the problem statement
def is_pandigital_identity(a, b):
    product = a * b
    # Combine the results into a string for easy comparison later
    identity_str = f"{a}{b}{product}"
    # Must be exactly 9 digits and contain 1-9 exactly once
    return len(identity_str) == 9 and "".join(sorted(identity_str)) == "123456789"

# Use a set to automatically handle duplicate products
pandigital_products = set()

# Optimization: Product must be 4 digits, factors must be 1x4 or 2x3 digits
for a in range(1, 100):
    for b in range(a, 10000 // a):
        if is_pandigital_identity(a, b):
            pandigital_products.add(a * b)

print(f"Products found: {sorted(list(pandigital_products))}")
print(f"Total Sum: {sum(pandigital_products)}")