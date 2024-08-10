def climbStairs(n):
    if n <= 2:
        return n

    a, b = 1, 2

    for i in range(3, n+1):
        new = a+b
        a = b
        b = new

    return b

input = 5
result = climbStairs(input)
print(result)


