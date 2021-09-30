def add(a: int):
    return lambda b: a + b

import codewars_test as test

@test.describe("Fixed Tests")
def _():
    @test.it("Single call should return a function")
    def _():
        test.expect(callable(add(32)), "The first call did not return a function")
        test.expect(callable(add(15)), "The first call did not return a function")
    @test.it("Double calls should return the addition result")
    def _():
        test.assert_equals(add(2)(5), 7,    'Should return the addition of these invocations!')
        test.assert_equals(add(14)(25), 39, 'Should return the addition of these invocations!')