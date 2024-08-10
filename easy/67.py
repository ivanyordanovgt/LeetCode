def addBinary(a, b):
    c_carry = ""
    result = []
    max_len = max(len(a), len(b))

    def simplify(a):
        if "1" in a:
            return "1"
        return "0"

    a = a[::-1]
    b = b[::-1]
    for i in range(max_len):
        c_a = ""
        c_b = ""

        if i < len(a):
            c_a = a[i]
        if i < len(b):
            c_b = b[i]

        combined = c_a + c_b + c_carry
        ones_count = combined.count("1")

        if ones_count > 1:
            combined = str(ones_count-2)
            c_carry = "1"
        else:
            c_carry = ""

        combined = simplify(combined)
        result.insert(0, combined)

    if c_carry:
        result.insert(0, "1")

    return "".join(result)


a, b = "1010", "1011"
result = addBinary(a, b)
print(result)