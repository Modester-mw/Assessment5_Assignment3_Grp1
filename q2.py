# computing factorial of a number

# first method
# Implement factorial computation using memoization. Test the program on n such that 4<= n < 1,000,00

# second method
# Implement factorial computation using tabulation technique (bottom up).  Test the program on n such that 4 <= n < 1,000,000

# implementations

# memoization

import time


# memoization function
def factorial_memo(n, memo):
    # check if the value is already in the memo
    if n in memo:
        return memo[n]
    # base case
    if n == 1:
        return 1
    memo[n] = n * factorial_memo(n - 1, memo)
    return memo[n]


# tabulation
def factorial_tab(n):
    # create a table to store the values
    table = [0] * (n + 1)
    table[1] = 1
    # fill the table
    for i in range(2, n + 1):
        table[i] = i * table[i - 1]
    return table[n]


# sample run
test_nums = [5, 100, 1000]

memo = {}
print("Memoization")
for num in test_nums:
    # start time
    start_time = time.time()
    print("Factorial of {} is {}".format(num, factorial_memo(num, memo)))
    end_time = time.time()
    print("Time taken for memoization is {} ms".format(
        (time.time() - start_time) * 1000))
    print()

print()
print()

print("Tabulation")
for num in test_nums:
    start_time = time.time()
    print("Factorial of {} is {}".format(num, factorial_tab(num)))
    end_time = time.time()
    print("Time taken for tabulation is {} ms".format(
        (time.time() - start_time) * 1000))
    print()

# Identify the algorithm that works the best as the number gets big.
# for input 1000 and large inputs, tabulation is faster than memoization
