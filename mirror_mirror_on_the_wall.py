from typing import List

def mirror(data: List[int]) -> List[int]:
    sorted_data = sorted(data)
    reversed_data = sorted_data[:]
    reversed_data.reverse()
    return sorted_data + reversed_data[1:]

import codewars_test as test

fixed_cases = iter([
    ([], []),
    ([1], [1]),
    ([2, 1], [1, 2, 1]),
    ([1, 3, 2], [1, 2, 3, 2, 1]),
    ([-8, 42, 18, 0, -16], [-16, -8, 0, 18, 42, 18, 0, -8, -16]),
    ([-3, 15, 8, -1, 7, -1], [-3, -1, -1, 7, 8, 15, 8, 7, -1, -1, -3])
])

@test.describe("Fixed tests")
def fixed():
    for input, expected in fixed_cases:
        test.assert_equals(mirror(input), expected)
