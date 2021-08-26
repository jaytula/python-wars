import math

def validate(username: str, password: str):
    if len(password) == 0 or len(username) == 0: return False

    (shorter, longer) = sorted([username, password], key=lambda x: len(x))

    common_length = math.ceil(len(shorter) / 2)

    for i in range(len(shorter) - common_length + 1):
      if shorter[i:i+common_length] in longer:
        return False

    return True

import codewars_test as test

# test.assert_equals(actual, expected, [optional] message)
@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        test.assert_equals(validate("", ""), False)
        test.assert_equals(validate("username", "myname"), False)
        test.assert_equals(validate("sword", "password" ), False)
        test.assert_equals(validate("qwertyuiop", "asdfghjkl"), True)
        test.assert_equals(validate("MASH", "M*A*S*H"), True)
        test.assert_equals(validate("asdfghjkl", "lkjhgfdsa"), True)
