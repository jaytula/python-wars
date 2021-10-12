from typing import List


def odd_ones_out(numbers: List[int]):
    return [num for num in numbers if len([num2 for num2 in numbers if num2 == num]) % 2 == 0]

import codewars_test as test

test.assert_equals(odd_ones_out([1,2,3,1,3,3]), [1,1])
test.assert_equals(odd_ones_out([75, 68, 75, 47, 68]), [75, 68, 75, 68])
test.assert_equals(odd_ones_out([42, 72, 32, 4, 94, 82, 67, 67]), [67, 67])
test.assert_equals(odd_ones_out([100, 100, 5, 5, 100, 50, 68, 50, 68, 50, 68, 5, 100]), [100, 100, 100, 100])
test.assert_equals(odd_ones_out([82, 86, 71, 58, 44, 79, 50, 44, 79, 67, 82, 82, 55, 50]), [44, 79, 50, 44, 79, 50])