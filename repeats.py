from typing import Dict, List

def repeats(arr: List[int]):
    dict: Dict[int, int] = {}
    for num in arr:
      if not num in dict: dict[num] = 0
      dict[num] += 1

    return sum([key for key, value in dict.items() if value==1])

import codewars_test as test

test.it("Basic tests")
test.assert_equals(repeats([4,5,7,5,4,8]),15)
test.assert_equals(repeats([9, 10, 19, 13, 19, 13]),19)
test.assert_equals(repeats([16, 0, 11, 4, 8, 16, 0, 11]),12)
test.assert_equals(repeats([5, 17, 18, 11, 13, 18, 11, 13]),22)
test.assert_equals(repeats([5, 10, 19, 13, 10, 13]),24)