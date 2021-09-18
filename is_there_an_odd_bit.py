def any_odd(x: int):
    return 1 if (x & 0xAAAAAAAA) else 0

import codewars_test as test

test.assert_equals(any_odd(5), 0)
test.assert_equals(any_odd(170), 1)
test.assert_equals(any_odd(2), 1)