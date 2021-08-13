def ensure_question(s: str):
  return s if s.endswith('?') else s + '?'

import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(ensure_question(""),"?","Expected: '?'")
        test.assert_equals(ensure_question("Yes"),"Yes?","Expected: '?'")
        test.assert_equals(ensure_question("No?"),"No?","Expected: '?'")