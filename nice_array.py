from typing import List


def is_nice(arr: List[int]):
    return all([num+1 in arr or num-1 in arr for num in arr]) and len(arr) > 0

import codewars_test as test

test.it("Basic tests")
test.assert_equals(is_nice([2,10,9,3]),True)
test.assert_equals(is_nice([3,4,5,7]),False)