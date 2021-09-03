def solve(n: int):
    if n == 0: return '0'
    if n == 1: return '01'
    return solve(n-1) + solve(n-2)

import codewars_test as test

test.it("Basic tests")
test.assert_equals(solve(0),'0')
test.assert_equals(solve(1),'01')
test.assert_equals(solve(2),'010')
test.assert_equals(solve(3),'01001')
test.assert_equals(solve(5),'0100101001001')