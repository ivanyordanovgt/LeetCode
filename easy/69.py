def mySqrt(x):
    left = 0
    right = x
    mid = None
    while left <= right:
        mid = (left+right) // 2
        mid_sqr = mid * mid
        if mid * mid > x:
            right = mid-1
        elif mid_sqr < x:
            left = mid + 1
        else:
            return mid

    return right


input = 37
result = mySqrt(input)
print(result)