def subcuboids(x: int, y: int, z: int):
    return x * (x+1) * y * (y+1) * z * (z+1) // 8

import codewars_test as test

@test.describe("Sample tests")
def sample_tests():
    @test.it("Tests")
    def it_1():
        test.assert_equals(subcuboids(1,1,1), 1)
        test.assert_equals(subcuboids(2,2,2), 27)
        test.assert_equals(subcuboids(2,3,3), 108)
        test.assert_equals(subcuboids(4,5,6), 3150)
        test.assert_equals(subcuboids(3,7,11), 11088)
        test.assert_equals(subcuboids(575902209,972149106,928202905), 33756632233154777740094375878952219961428995283639175)