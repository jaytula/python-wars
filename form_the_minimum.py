from typing import List

def min_value(digits: List[int]):
  digits = sorted(list(set(digits)))
  return int(''.join([str(digit) for digit in digits]))

import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(min_value([1, 3, 1]), 13)
        test.assert_equals(min_value([4, 7, 5, 7]), 457)
        test.assert_equals(min_value([4, 8, 1, 4]), 148)