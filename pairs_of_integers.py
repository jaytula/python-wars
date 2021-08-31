def generate_pairs(m, n):
    result = []
    for i in range(m, n+1):
      for j in range(i, n+1):
        result.append((i, j))
    return result

import codewars_test as test

@test.describe("Fixed Tests")
def fixed_test_cases():
    @test.it("Example Tests")
    def example_test_case():
        test.assert_equals(generate_pairs(2, 4),  [ (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4) ])
        test.assert_equals(generate_pairs(0, 1),  [ (0, 0), (0, 1), (1, 1) ])
        test.assert_equals(generate_pairs(0, 0),  [ (0, 0) ])