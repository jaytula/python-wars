def point_in_circle(x: float, y: float):
    return x**2 + y**2 <= 1

import codewars_test as test

@test.describe("Point in a unit circle")
def _():
    @test.it("Origin is inside")
    def _():
        test.assert_equals(point_in_circle(0, 0), True)


    @test.it("(2, 0) is outside")
    def _():
        test.assert_equals(point_in_circle(2, 0), False)


    @test.it("(-1.1, 0) is outside")
    def _():
        test.assert_equals(point_in_circle(-1.1, 0), False)


    @test.it("(0, 0.9) is inside")
    def _():
        test.assert_equals(point_in_circle(0, 0.9), True)


    @test.it("(0.5, 0.5) is inside")
    def _():
        test.assert_equals(point_in_circle(0.5, 0.5), True)


    @test.it("(0.7, 0.7) is inside")
    def _():
        test.assert_equals(point_in_circle(0.7, 0.7), True)


    @test.it("(0.71, 0.71) is inside")
    def _():
        test.assert_equals(point_in_circle(0.71, 0.71), False)