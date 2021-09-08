from typing import List

def positive_to_negative(binary: List[int]):
    inverted = [1 if val == 0 else 0 for val in binary]

    inverted[-1] += 1
    for i in range(len(inverted)):
      if inverted[-i-1] == 2:
        inverted[-i-1] = 0
        if i != len(inverted) -1:
          inverted[-i-2] += 1
      
    return inverted

import codewars_test as test

test.assert_equals(positive_to_negative([0, 0, 0, 0]), [0, 0, 0, 0])
test.assert_equals(positive_to_negative([0, 0, 1, 0]), [1, 1, 1, 0])
test.assert_equals(positive_to_negative([0, 0, 1, 1]), [1, 1, 0, 1])
test.assert_equals(positive_to_negative([0, 1, 0, 0]), [1, 1, 0, 0])