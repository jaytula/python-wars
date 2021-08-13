def even_and_odd(n: int):
  NE = ''
  NO = ''

  for ch in str(n):
    num = int(ch)
    if(num % 2 == 0):
      NE = NE + ch
    else:
      NO = NO + ch

  return (int(NE) if len(NE) else 0, int(NO) if len(NO) else 0)

import codewars_test as test

@test.describe("Example")
def test_group():
    @test.it("basic test cases")
    def test_case():
        test.assert_equals(even_and_odd(126453), (264, 153))
        test.assert_equals(even_and_odd(3012), (2, 31))
        test.assert_equals(even_and_odd(4628), (4628, 0))