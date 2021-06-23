def factorial(n):
    # n! could also be defined as n * (n-1)!
    """ calculates n! recursively """
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

for i in range(130):
    print(i, factorial(i))