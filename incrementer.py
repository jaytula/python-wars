from typing import List


def incrementer(nums: List[int]):
    return [(num + 1 + idx) % 10 for idx, num in enumerate(nums)]

import codewars_test as test

def testing(arr, exp):
    @test.it("Testing for [" + ", ".join([str(x) for x in arr]) + "]")
    def tester():
        test.assert_equals(incrementer(arr), exp)

@test.describe("Fixed tests")
def fixed_tests():
    testing([], [])
    testing([1, 2, 3], [2, 4, 6])
    testing([4, 6, 7, 1, 3], [5, 8, 0, 5, 8])
    testing([3, 6, 9, 8, 9], [4, 8, 2, 2, 4])
    testing([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 8], [2, 4, 6, 8, 0, 2, 4, 6, 8, 9, 0, 1, 2, 2])