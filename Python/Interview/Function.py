# Recursion, recursive function
def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    return n * factorial(n - 1)
print(factorial(5))
# 1
# 2
# 3
# 4
# 5
