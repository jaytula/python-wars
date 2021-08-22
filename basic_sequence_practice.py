def sum_of_n(n: int):
    result = [0]
    if(n == 0): return result

    multipler = -1 if n < 0 else 1
    counter = 1
    n = abs(n)

    while(n > 0):
      result.append(result[-1] + counter*multipler)
      counter+=1
      n -= 1

    return result

import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(sum_of_n(3), [0, 1, 3, 6])
        # test.assert_equals(sum_of_n(-4), [0, -1, -3, -6, -10])
        # test.assert_equals(sum_of_n(1), [0, 1])
        # test.assert_equals(sum_of_n(0), [0])
        # test.assert_equals(sum_of_n(10), [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55])
