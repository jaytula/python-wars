from typing import List

def all_non_consecutive(arr: List[int]):
    result = []

    for i, n in enumerate(arr):
      if i == 0: continue
      if n != arr[i-1] + 1:
        result.append({"i": i, "n": n})
    
    return result

import codewars_test as test

test.describe('A simple example')
test.assert_equals(all_non_consecutive([1,2,3,4,6,7,8,10]), [{'i': 4, 'n': 6}, {'i': 7, 'n': 10}])