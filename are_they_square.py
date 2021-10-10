from typing import List
import math

def is_square(arr: List[int]):
    if len(arr) == 0: return None
    return all([math.sqrt(num) % 1 == 0 for num in arr])

import codewars_test as test

@test.describe("is_square")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(is_square([1, 4, 9, 16, 25, 36]), True)
        test.assert_equals(is_square([1, 2, 3, 4, 5, 6]), False)
        test.assert_equals(is_square([]), None)
        test.assert_equals(is_square([1, 4, 9, 16, 25]), True)
        test.assert_equals(is_square([1, 2, 4, 15]), False)