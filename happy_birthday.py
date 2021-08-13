def wrap(height: int, width: int, length: int):
  arr = sorted([height, width, length])
  return arr[0] * 4 + arr[1] * 2 + arr[2] * 2 + 20

import codewars_test as test

@test.describe("wrap present")
def tests():
  @test.it("basic tests")
  def basic():
    test.assert_equals(wrap(17, 32, 11), 162)
    test.assert_equals(wrap(13, 13, 13), 124)
    test.assert_equals(wrap(1, 3, 1), 32)