def solve(st: str, k: int):
  k = min(len(st) - 1, k)
  size = len(st) - k
  return max([int(st[i:i+size]) for i in range(k+1)])
    

import codewars_test as test

test.assert_equals(solve('123',1) ,23)
test.assert_equals(solve('1234',1),234)
test.assert_equals(solve('1234',2),34)
test.assert_equals(solve('234',3),4)

