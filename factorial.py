def factorial (n):
    if n < 0:
        return "Invalid input"

    result = 1
    for i in range(1, n + 1):
        result = result * i

    return result


def factorial_recursive (n):
    if n < 0:
        return 'Invalid input'

    if n == 0:
        return 1 #Base case

    else:
        return n * factorial_recursive(n - 1)


print(factorial_recursive(5))
print(factorial(5))
print(factorial(-1))
