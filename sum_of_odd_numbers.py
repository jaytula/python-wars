def row_sum_odd_numbers(n: int):
    return n**3

import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(row_sum_odd_numbers(1), 1)
        test.assert_equals(row_sum_odd_numbers(2), 8)
        test.assert_equals(row_sum_odd_numbers(13), 2197)
        test.assert_equals(row_sum_odd_numbers(19), 6859)
        test.assert_equals(row_sum_odd_numbers(41), 68921)