from typing import List


def is_solved(board: List[List[int]]):
  flattened = [col for row in board for col in row]
  return all(idx == 0 or el > flattened[idx-1] for idx, el in enumerate(flattened))
  
import codewars_test as test

@test.describe('Sample Tests')
def sample_tests():
    test.assert_equals(is_solved([[0,1],[2,3]]), True)
    test.assert_equals(is_solved([[1,0],[3,2]]), False)