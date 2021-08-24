from typing import List

def least_larger(a: List[int], i: int): 
    num_at_index = a[i]

    filtered_arr = [item for item in a if item > num_at_index]
    return a.index(min(filtered_arr)) if filtered_arr else -1

import codewars_test as test

@test.it("example tests")
def test_case():
    test.assert_equals(least_larger( [4, 1, 3, 5, 6], 0), 3 )
    test.assert_equals(least_larger( [4, 1, 3, 5, 6], 4), -1 )
    test.assert_equals(least_larger( [1, 3, 5, 2, 4], 0), 3 )
    test.assert_equals(least_larger( [1, 2, 3, 4, 5, 0], 3), 4 )