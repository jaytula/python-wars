from typing import List


def catch_sign_change(lst: List[int]):
    count = 0
    is_negative = False
    
    for idx, num in enumerate(lst):
      if(idx == 0):
        is_negative = num < 0
        continue
      if is_negative != (num < 0):
        count += 1
        is_negative = num < 0
      
    return count

import codewars_test as test

test.assert_equals(catch_sign_change([1, 3, 4, 5]), 0)
test.assert_equals(catch_sign_change([1, -3, -4, 0, 5]), 2)
test.assert_equals(catch_sign_change([]), 0)
test.assert_equals(catch_sign_change([-47,84,-30,-11,-5,74,77]), 3)