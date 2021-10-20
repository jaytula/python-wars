def nth_char(words):
	return "".join([word[idx] for idx, word in enumerate(words)])


import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(nth_char(['yoda', 'best', 'has']), 'yes')
        test.assert_equals(nth_char([]),'')
        test.assert_equals(nth_char(['X-ray']),'X')
        test.assert_equals(nth_char(['No','No']),'No')
        test.assert_equals(nth_char(['Chad','Morocco','India','Algeria','Botswana','Bahamas','Ecuador','Micronesia']),'Codewars')