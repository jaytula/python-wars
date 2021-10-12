from typing import List

def cube_times(times: List[float]):
    times.sort()

    return (round((times[1]+times[2]+times[3])/3, 2), times[0])

import codewars_test as test

@test.describe("cube_times")
def tests():
    @test.it("Basic tests")
    def basic_tests():
        test.assert_equals(cube_times([9.5, 7.6, 11.4, 10.5, 8.1]), (9.37, 7.6))
        test.assert_equals(cube_times([13.4, 12.3, 9.5, 11.9, 20.8]), (12.53, 9.5))
        test.assert_equals(cube_times([28.3, 14.5, 17.3, 8.9, 10.1]), (13.97, 8.9))