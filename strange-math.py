def add(num1: int, num2: int):
  s1, s2 = sorted([str(num1), str(num2)], key=len)

  s1 = "0"*(len(s2)-len(s1)) + s1

  result = ''
  for a, b in zip(s1, s2):
    result += str(int(a) + int(b))
  return int(result)
      

import codewars_test as test

@test.it("Actual Addition")
def real_addition_test():
    test.assert_equals(add(2,11), 13)
    test.assert_equals(add(0,1), 1)
    test.assert_equals(add(0,0), 0)

@test.it("Silly Addition")
def silly_addition_test():
    test.assert_equals(add(16,18), 214)
    test.assert_equals(add(26,39), 515)
    test.assert_equals(add(122,81), 1103)
