import math


def longestPalindrome(s):
    max_string = ""

    if len(s) <= 1:
        return s


    for i in range(len(s)):
        l, r = 0 + i, len(s)

        while l <= r:
            c_string = s[l:r]

            if len(max_string) > len(c_string):
                break

            print(c_string, max_string)
            if c_string == c_string[::-1]:
                if len(c_string) > len(max_string):
                    max_string = c_string
                else:
                    break

            r -= 1

    return max_string


input = 'abcdbbfcba'
result = longestPalindrome(input)
print("result: ", result)