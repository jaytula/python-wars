import re

def solve(eq: str):
    return re.sub(r'(\d+)', lambda x: x[0][::-1], eq[::-1])

import codewars_test as test

test.it("Basic tests")
test.assert_equals(solve("100*b/y"),"y/b*100")
test.assert_equals(solve("a+b-c/d*30"),"30*d/c-b+a")
test.assert_equals(solve("a*b/c+50"),"50+c/b*a")