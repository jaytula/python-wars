from typing import List, Union

def duplicate_sandwich(arr: List[Union[int, str, bool]]):
    duplicate = [item for item in arr if arr.count(item) == 2][0]
    first_index = arr.index(duplicate)
    last_index = arr.index(duplicate, first_index+1)

    return arr[first_index+1:last_index]

import codewars_test as test

@test.describe("Duplicate sandwich")
def tests():
    @test.describe("Basic tests")
    def basic():
        test.assert_equals(duplicate_sandwich([0, 1, 2, 3, 4, 5, 6, 1, 7, 8]), [2, 3, 4, 5, 6])
        test.assert_equals(duplicate_sandwich(['None', 'Hello', 'Example', 'hello', 'None', 'Extra']), ['Hello', 'Example', 'hello'])
        test.assert_equals(duplicate_sandwich([0, 0]), [])
        test.assert_equals(duplicate_sandwich([True, False, True]), [False])
        test.assert_equals(duplicate_sandwich(['e', 'x', 'a', 'm', 'p', 'l', 'e']), ['x', 'a', 'm', 'p', 'l'])