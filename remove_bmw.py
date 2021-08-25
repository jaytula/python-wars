import re
def remove_bmw(string):
    if not isinstance(string, str):
      raise TypeError("This program only works for text.")
    return re.sub(r"[bmw]", "", string, flags=re.IGNORECASE)

import codewars_test as test

@test.describe("Example")
def test_group():
    test.assert_equals(remove_bmw("bmwvolvoBMW"), "volvo")
    test.assert_equals(remove_bmw("blablahblah"), "lalahlah")
    try:
      remove_bmw(0)
    except TypeError as e:
      test.assert_equals(str(e), "This program only works for text.")


