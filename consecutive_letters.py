def solve(st: str):
  char_list =  list(st)
  char_list.sort()

  for idx, ch in enumerate(char_list):
    if(idx == 0): continue
    if(ord(ch) != ord(char_list[idx-1]) + 1): return False

  return True

import codewars_test as test

test.it("Basic tests") 
test.assert_equals(solve("abc"),True)
test.assert_equals(solve("abd"), False)
test.assert_equals(solve("dabc"),True)
test.assert_equals(solve("abbc"), False)