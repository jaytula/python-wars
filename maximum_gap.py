from typing import List

def max_gap(numbers: List[int]):
  sorted_numbers = sorted(numbers)
  theMax = 0

  for i in range(1, len(sorted_numbers)):
    diff = sorted_numbers[i] - sorted_numbers[i-1]
    if diff > theMax:
      theMax = diff
  
  return theMax

import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(max_gap([13,10,2,9,5]),4)
        test.assert_equals(max_gap([13,3,5]),8)
        test.assert_equals(max_gap([24,299,131,14,26,25]),168)
        test.assert_equals(max_gap([-3,-27,-4,-2]),23)
        test.assert_equals(max_gap([-7,-42,-809,-14,-12]),767)
        test.assert_equals(max_gap([12,-5,-7,0,290]),278)
        test.assert_equals(max_gap([-54,37,0,64,-15,640,0]),576)
        test.assert_equals(max_gap([130,30,50]),80)
        test.assert_equals(max_gap([1,1,1]),0)
        test.assert_equals(max_gap([-1,-1,-1]),0)