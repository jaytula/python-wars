def multiple(x: int):
    if x % 5 == 0 and x % 3 == 0: return 'BangBoom'
    if x % 3 == 0: return 'Bang'
    if x % 5 == 0: return 'Boom'
    return 'Miss'

import codewars_test as test

test.assert_equals(multiple(30), "BangBoom")
test.assert_equals(multiple(3), "Bang")
test.assert_equals(multiple(98),"Miss")
test.assert_equals(multiple(65),"Boom")
test.assert_equals(multiple(23),"Miss")
test.assert_equals(multiple(15),"BangBoom")