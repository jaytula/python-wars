def count_ways(n: int, k: int):
    if k > n: count_ways(n, n)
    if k == 1: return 1
    memory = [1, 1]

    for i in range(2, n+1):
      memory.append(sum(memory[max(0, i-k):i]))

    return memory[-1]

import codewars_test as test

@test.describe('Example Tests')
def example_tests():
    test.assert_equals(count_ways(1, 3), 1)
    test.assert_equals(count_ways(3, 3), 4)
    test.assert_equals(count_ways(2, 3), 2)
    test.assert_equals(count_ways(5, 3), 13)
    test.assert_equals(count_ways(4, 3), 7)
    test.assert_equals(count_ways(10, 6), 492)
    test.assert_equals(count_ways(14, 7), 7936)