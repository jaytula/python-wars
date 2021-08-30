from typing import List

def split_by_value(k: int, elements: List[int]):
    before = []
    after = []

    for el in elements:
      if el < k:
        before.append(el)
      else:
        after.append(el)

    return before + after

import codewars_test as test

@test.describe('Sample Tests')
def sample_tests():

    # Basic Tests: Test the basic behavior (basic understanding of the task).
    @test.it('Basic Test Cases')
    def basic_tests():
        test.assert_equals(split_by_value(5, [1, 3, 5, 7, 6, 4, 2]), [1, 3, 4, 2, 5, 7, 6])
        test.assert_equals(split_by_value(0, [5, 2, 7, 3, 2]),[5, 2, 7, 3, 2])
        test.assert_equals(split_by_value(6, [6, 4, 10, 10, 6]),[4, 6, 10, 10, 6])