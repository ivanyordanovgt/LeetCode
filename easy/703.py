class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k
        self.nums = nums if len(nums) < k else sorted(nums)[-k::]
        self.last = None if len(nums) < k else self.nums[-k]

    def add(self, val):

        if self.last is None:
            self.last = val

        if len(self.nums) < self.k:

            self.nums.append(val)
            self.last = min(self.nums)

            return self.last

        if val >= self.last:
            self.nums.append(val)
            self.nums = sorted(self.nums)[-self.k-1::]
            self.last = self.nums[-self.k]

        return self.last

input = [3,[5,-1]]
kthLargest = KthLargest(*input)

input_list = [[2],[1],[-1],[3],[4]]
results = []
for el in input_list:
    results.append(kthLargest.add(el[0]))
  # // return 4
   # // return 5
  # // return 5
   # // return 8

for res in results:
    print(res)