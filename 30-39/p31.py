#!/usr/bin/env python3

# PROBLEM:
# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
#
#    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
#
# It is possible to make £2 in the following way:
#
#    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#
# How many different ways can £2 be made using any number of coins?

# SOLUTION:
# Mathematical proof reference: https://andrew.neitsch.ca/publications/m496pres1.nb.pdf

def count_combinations(coins, target):
  # combos[i] stores the number of ways to make the sum i
  # Sums (i): [0, 1, 2... 200] 
  combos = [0] * (target + 1)
  # Base: Only 1 way to make change for 0
  combos[0] = 1

  # Iterate through teach coin
  for coin in coins:
    # Update the list for all amounts greater than or equal to the coin's value
    for i in range(coin, target + 1):
      combos[i] += combos[i - coin]
  return combos[target]

coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200
result = count_combinations(coins, target)
print(f"Total combinations: {result}") # Total combinations: 73682
