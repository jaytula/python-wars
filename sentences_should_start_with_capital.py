def fix(paragraph: str):
    return ". ".join([sentence.capitalize() for sentence in paragraph.split('. ')])

import codewars_test as test
# TODO Write tests

# test.assert_equals(actual, expected, [optional] message)
@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        test.assert_equals(fix(""), "")
        test.assert_equals(fix("hi."), "Hi.")
        test.assert_equals(
          fix("hello. my name is inigo montoya. you killed my father. prepare to die."),
          "Hello. My name is inigo montoya. You killed my father. Prepare to die.")
