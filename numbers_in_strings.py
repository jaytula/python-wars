import re

def solve(s: str):
  return max([int(num) for num in re.findall(r'\d+', s)])

import codewars_test as test

test.it("Basic tests")
test.assert_equals(solve('gh12cdy695m1'),695)
test.assert_equals(solve('2ti9iei7qhr5'),9)
test.assert_equals(solve('vih61w8oohj5'),61)
test.assert_equals(solve('f7g42g16hcu5'),42)
test.assert_equals(solve('lu1j8qbbb85'),85)