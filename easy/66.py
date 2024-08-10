def plusOne(digits):
    result = []
    carry = 1

    for num in digits[::-1]:
        num = num + carry
        carry = 0
        if num >= 10:
            carry = 1
            num = 0

        result.insert(0, num)

    if carry > 0:
        result.insert(0, 1)

    return result





input = [9]
result = plusOne(input)
print(result)