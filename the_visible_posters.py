from typing import List, Set, Tuple


def count_visible(posters: List[Tuple[int, int]]):
    visible = 0
    used = set()

    for start, end in posters[::-1]:
      should_add = False
      for i in range(start, end+1):
        if not i in used:
          should_add = True
          used.add(i)

      if should_add:
        visible += 1
    return visible


import codewars_test as test

@test.describe("Sample tests")
def sample_tests():
    @test.it("Tests")
    def it_1():
        test.assert_equals(count_visible([(1, 4), (2, 6), (8, 10), (3, 4), (7, 10)]), 4)
        test.assert_equals(count_visible([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (1, 10)]), 1)
        test.assert_equals(count_visible([(1, 10), (1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]), 5)
        test.assert_equals(count_visible([(1, 2), (1, 3), (1, 4), (1, 6), (1, 8), (1, 10)]), 1)
        test.assert_equals(count_visible([(1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)]), 6)
        test.assert_equals(count_visible([(1, 1000), (1, 2), (3, 999)]), 3)