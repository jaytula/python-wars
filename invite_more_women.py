from typing import List


def invite_more_women(arr: List[int]):
    return sum(arr) > 0

import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(invite_more_women([1, -1, 1]), True)
        test.assert_equals(invite_more_women([-1, -1, -1]), False)
        test.assert_equals(invite_more_women([1, -1]), False)
        test.assert_equals(invite_more_women([1, 1, 1]), True)