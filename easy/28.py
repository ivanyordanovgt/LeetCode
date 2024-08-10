def strStr(haystack, needle):
    def built_in_solution():
        if needle in haystack:
            return haystack.index(needle)

        return -1

    def manual():
        needle_len = len(needle)
        for i in range(len(haystack)):
            if i + needle_len > len(haystack):
                return -1

            if haystack[i:i + needle_len] == needle:
                return i

        return -1

    return manual()

haystack = "omgiR7!loveit"
needle = "R7!"
result = strStr(haystack, needle)
print(result)