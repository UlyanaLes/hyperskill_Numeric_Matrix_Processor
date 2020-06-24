def fib(n):
    if n == 0:  # base case for month 0
        return 0  # the rabbits are not on a farm yet!
    if n in (1, 2):  # base case for month 1
        return 1  # a pair of baby rabbit has just arrived!
    return fib(n - 1) + fib(n - 2)  # recursive calls

# print(fib(6))
