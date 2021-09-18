import re
def valid_number(n: str):
  return True if re.match(r'^(\+|-)?\d*\.\d{2}$', n) else False

import codewars_test as test

@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        test.assert_equals(valid_number("0.00"),True)
        test.assert_equals(valid_number(".00"),True)
        test.assert_equals(valid_number("-.00"),True)
        test.assert_equals(valid_number(".30"),True)
        test.assert_equals(valid_number("0.40"),True)
        test.assert_equals(valid_number("34443.33"),True)
        test.assert_equals(valid_number(".0a"),False)
        test.assert_equals(valid_number("1.00."),False)
        test.assert_equals(valid_number(".+00"),False)
        test.assert_equals(valid_number("w.00"),False)
        test.assert_equals(valid_number("..00"),False)
        test.assert_equals(valid_number("1,00"),False)
