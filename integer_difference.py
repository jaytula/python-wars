from typing import List


def int_diff(lst: List[int], n: int):
    count = 0
    for i, num1 in enumerate(lst):
      for j, num2 in enumerate(lst):
        if i == j: continue
        if abs(num1 - num2) == n: count += 1

    return count // 2

import codewars_test as test

test.assert_equals(int_diff([1, 1, 5, 6, 9, 16, 27], 4), 3)
test.assert_equals(int_diff([1, 1, 3, 3], 2), 4)