import math

def is_prime(n: int):
  if n <= 1:
    return False

  root = math.sqrt(n)
  upper_limit = math.floor(root+1 if root % 1 == 0 else root)
  for i in range(2, upper_limit):
    if(n % i == 0):
      return False

  return True

import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    test.assert_equals(is_prime(0),False)
    test.assert_equals(is_prime(1),False)
    test.assert_equals(is_prime(2),True)
    test.assert_equals(is_prime(3),True)
    test.assert_equals(is_prime(11),True)
    test.assert_equals(is_prime(12),False)
    test.assert_equals(is_prime(571),True)
    test.assert_equals(is_prime(25),False)