from collections import deque


def solution(s):
    parentheses = {
        "(": ")",
        "[": "]",
        "{": "}"
    }

    opened_stack = deque()
    to_close = 0
    if len(s) % 2 != 0:
        return False

    for char in s:
        if char in list(parentheses.keys()):
            opened_stack.append(char)
            to_close += 1

        else:
            if len(opened_stack) == 0:
                return False

            if char != parentheses[opened_stack.pop()]:
                return False

            to_close -= 1

    if to_close != 0:
        return False

    return True


input = "()"
result = solution(input)
print(result)
