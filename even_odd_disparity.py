from typing import List, Union

def solve(arr: List[Union[str, int]]):
  return sum([
    1 if item % 2 == 0 else -1 
    for item in arr if isinstance(item, int)
  ])

import codewars_test as test

test.it("Basic tests")
test.assert_equals(solve([0,1,2,3]),0)
test.assert_equals(solve([0,1,2,3,'a','b']),0)
test.assert_equals(solve([0, 15,'z',16,'m', 13, 14,'c', 9, 10, 13,'u', 4, 3]),0)
test.assert_equals(solve([13, 6, 8, 15, 4, 8, 13]),1)
test.assert_equals(solve([1,'a', 17, 8,'e', 3,'i', 12, 1]),-2)