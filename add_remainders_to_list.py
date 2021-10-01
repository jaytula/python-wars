from typing import List


def solve(nums: List[int], div: int):
    return [num + (num % div) for num in nums]

import codewars_test as test

@test.describe("Sample tests")
def tests():
    @test.it("Some examples")
    def tests():
        test.assert_equals(solve([2, 7, 5, 9, 100, 34, 32, 0], 3), [4, 8, 7, 9, 101, 35, 34, 0])
        test.assert_equals(solve([1000, 999, 998, 997], 5), [1000, 1003, 1001, 999])
        test.assert_equals(solve([], 2), [])