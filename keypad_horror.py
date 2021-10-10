def computer_to_phone(numbers: str):
    return "".join([str([0,7,8,9,4,5,6,1,2,3][int(num)]) for num in numbers])

import codewars_test as test

test.assert_equals(computer_to_phone("0789456123"), "0123456789")
test.assert_equals(computer_to_phone("000"), "000")
test.assert_equals(computer_to_phone("94561"), "34567")