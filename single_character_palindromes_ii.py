import math
def solve(s: str):
  if len(s) % 2 == 0 and s == s[::-1]: return False
  if len(s) % 2 == 1 and s == s[::-1]: return True

  diff_count = 0
  max_index = math.floor(len(s) / 2)
  for idx, ch in enumerate(s[:max_index]):
    if ch != s[-(idx+1)]: diff_count += 1

  return diff_count == 1

import codewars_test as test

test.it("Basic tests")
test.assert_equals(solve("abba"),False)
test.assert_equals(solve("abbaa"),True)
test.assert_equals(solve("abbx"),True)
test.assert_equals(solve("aa"),False)
test.assert_equals(solve("ab"),True)
test.assert_equals(solve("abcba"),True)