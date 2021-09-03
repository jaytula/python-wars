from typing import List


def sum_diagonals(matrix: List[List[int]]):
    if len(matrix) == 0: return 0
    if len(matrix[0]) == 0: return 0
    total = 0
    for row, submatrix in enumerate(matrix):
      total += submatrix[row] + submatrix[-(row+1)]
    return total

import codewars_test as test

test.assert_equals(sum_diagonals([[1,2,3], [4,5,6], [7,8,9]]), 1 + 5 + 9 + 3 + 5 + 7)