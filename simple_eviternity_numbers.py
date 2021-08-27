import re

def solve(a: int, b: int):
  count = 0
  rgx = re.compile(r'^[853]+$')
  for i in range(a, b):
    number_string = str(i)
    if rgx.match(number_string): 
      eights = number_string.count('8')
      fives = number_string.count('5')
      threes = number_string.count('3')
      if eights >= fives and fives >= threes:
        count += 1
  return count

import codewars_test as test

test.it("Basic tests")
test.assert_equals(solve(0,100),4)
test.assert_equals(solve(0,1000),14)
test.assert_equals(solve(0,10000),37)
test.assert_equals(solve(0,100000),103)
test.assert_equals(solve(0,500000),148)
