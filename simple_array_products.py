from typing import List

def solve(arr: List[List[int]]):
  result: List[int] = []
  for item in arr:
    new_result: List[int] = []

    if len(result) == 0:
      for subitem in item:
        new_result.append(subitem)
    else:
      for result_item in result:
        for subitem in item:
          new_result.append(result_item * subitem)

    result = new_result
  
  return max(result)

import codewars_test as Test

Test.it("Basic tests")
Test.assert_equals(solve([[1, 2],[3, 4]]),8)
Test.assert_equals(solve([[10,-15],[-1,-3]]),45)
Test.assert_equals(solve([[-1,2,-3,4],[1,-2,3,-4]]),12)
Test.assert_equals(solve([[-11,-6],[-20,-20],[18,-4],[-20, 1]]),17600)
Test.assert_equals(solve([[14,2],[0,-16],[-12,-16]]),3584)
Test.assert_equals(solve([[-3,-4],[1,2,-3]]),12)