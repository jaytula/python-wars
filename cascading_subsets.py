from typing import List

def each_cons(lst: List[int], n: int):
  return [lst[i:i+n] for i in list(range(len(lst) - n + 1))]
    

import codewars_test as test

@test.describe("Test Cases")
def test_group():
    lst = [3, 5, 8, 13]
    @test.it('Should return cascading lists of 2 elements')
    def test_case1():
        test.assert_equals(each_cons(lst, 2), [[3,5], [5,8], [8,13]])