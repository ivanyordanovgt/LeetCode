def lengthOfLastWord(s):
    return len(s.split()[-1])

input = "   fly me   to   the moon  "
result = lengthOfLastWord(input)
print(result)