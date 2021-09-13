import math

def solve(st: str):
  count = 0

  for i in range(math.floor(len(st)/2)):
    if st[0:i+1] == st[-1-i:]:
      count = i+1

  return count

import codewars_test as Test

Test.it("Basic tests")
Test.assert_equals(solve("abcd"),0)
Test.assert_equals(solve("abcda"),1)
Test.assert_equals(solve("abcdabc"),3)
Test.assert_equals(solve("abcabc"),3)
Test.assert_equals(solve("abcabca"),1)
Test.assert_equals(solve("aaaaa"),2)
Test.assert_equals(solve("aaaa"),2)
Test.assert_equals(solve("aaa"),1)
Test.assert_equals(solve("aa"),1)
Test.assert_equals(solve("a"),0)