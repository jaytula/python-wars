from typing import List

def consecutive(arr: List[int], a: int, b: int):
    stored = None
    for i in arr:
      if stored == None and i in [a, b]:
        stored = i
      if stored != None and i in [a, b] and i != stored:
        return True
      if not i in [a, b]:
        stored = None
    return False

import codewars_test as test

@test.describe("Simple tests")
def test_group_1():
    @test.it("Test 1")
    def test_1():
        test.assert_equals(consecutive([1, 3, 5, 7], 3, 7), False)
    @test.it("Test 2")
    def test_2():
        test.assert_equals(consecutive([1, 3, 5, 7], 3, 1), True)
    @test.it("Test 3")
    def test_3():
        test.assert_equals(consecutive([1, 6, 9, -3, 4, -78, 0], -3, 4), True)