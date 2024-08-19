class Solution(object):
    def minSteps(self, n):

        if n <= 0:
            return 0

        last_copy = "A"
        current = "AA"
        operations_amount = 2
        while True:

            if len(current) == n:
                return operations_amount
            elif len(current) > n:
                print(last_copy, current, operations_amount)
                return False

            if n % len(current) == 0:
                last_copy = current
                current += last_copy
                operations_amount += 1
            else:
                current += last_copy

            operations_amount += 1
sol = Solution()
input = 3
res = sol.minSteps(input)
print(res)