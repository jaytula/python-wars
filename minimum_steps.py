from typing import List

def minimum_steps(numbers: List[int], value: int):
  sortedNumbers = sorted(numbers)
  for idx in range(0, len(sortedNumbers)):
    if sum(sortedNumbers[0:idx+1]) >= value:
      return idx


import codewars_test as test

test.describe("Basic tests")
test.assert_equals(minimum_steps([4,6,3], 7), 1)
test.assert_equals(minimum_steps([10,9,9,8], 17), 1)
test.assert_equals(minimum_steps([8,9,10,4,2], 23), 3)
test.assert_equals(minimum_steps([19,98,69,28,75,45,17,98,67], 464), 8)
test.assert_equals(minimum_steps([4,6,3], 2), 0)
print("<COMPLETEDIN::>")