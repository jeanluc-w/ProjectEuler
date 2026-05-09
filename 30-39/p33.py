#!/usr/bin/env python3
from fractions import Fraction
from functools import reduce
import operator

# PROBLEM
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe 
# that 49/98 = 4/8, which is correct, is obtained by cancelling the 9's.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

# SOLUTION
results = []
# Determine the 4 fractions first by looping through 11-99 (denominator)
for d in range(11, 100):
    # Loop only the values that are less than the denominator
    for n in range(10, d):
        # Convert to strings for quick and easy digit manipulation
        n_str, d_str = str(n), str(d)
        # Check digit cancellation for non-trivial solutions (i.e. no 0 in ones place)
        if n_str[1] == d_str[0] and int(d_str[1]) != 0:
            if n * int(d_str[1]) == d * int(n_str[0]):
                # Add the simplified form of the fraction so it's less memory and still leads to the solution
                results.append(Fraction(int(n_str[0]), int(d_str[1])))

# Print the final fraction in its reduced form
print(reduce(operator.mul, results)) # Result: 1/100