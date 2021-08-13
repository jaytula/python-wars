from functools import reduce
from typing import List

def smallest_product(arr: List[List[int]]):
  return min([reduce(lambda a, b: a*b, item, 1) for item in arr])

import codewars_test as test

@test.describe("Fixed tests")
def fixed_tests():
  @test.it("Tests")
  def it_1():
    test.assert_equals(smallest_product([[3, 2], [1, 2, 1], [7, 8]]), 2)
    test.assert_equals(smallest_product([[10], [3, 0], [-1, -6, 2]]), 0)