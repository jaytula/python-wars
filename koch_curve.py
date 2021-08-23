def koch_curve(n: int):
    if n == 0: return []
    if n == 1: return [60, -120, 60]
    return [*koch_curve(n-1),  60, *koch_curve(n-1), -120, *koch_curve(n-1),60, *koch_curve(n-1)]

import codewars_test as test

@test.describe("Koch curve")
def _():

    @test.it("Should handle basic cases")
    def _():
        test.assert_equals(koch_curve(0), [])
        test.assert_equals(koch_curve(1), [60, -120, 60])
        test.assert_equals(koch_curve(2), [60, -120, 60, 60, 60, -120, 60, -120, 60, -120, 60, 60, 60, -120, 60])
