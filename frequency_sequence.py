def freq_seq(s: str, sep: str):
    d = {}
    for ch in s:
        if not ch in d: d[ch] = 0
        d[ch] += 1
    return sep.join([str(d[ch]) for ch in s])

import codewars_test as test

@test.describe("Tests using hard-coded strings")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(freq_seq('hello world', '-'), '1-1-3-3-2-1-1-2-1-3-1')
        test.assert_equals(freq_seq('19999999',    ':'), '1:7:7:7:7:7:7:7')
        test.assert_equals(freq_seq('^^^**$',      'x'), '3x3x3x2x2x1')
