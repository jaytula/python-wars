import re

def solve(s: str):
    lowerCount = len(re.sub(r'[^a-z]', '', s))
    return s.lower() if lowerCount >= len(s)/2 else s.upper()

import codewars_test as test

test.it("Basic tests")
test.assert_equals(solve("code"),"code")
test.assert_equals(solve("CODe"),"CODE")
test.assert_equals(solve("COde"),"code")
test.assert_equals(solve("Code"),"code")