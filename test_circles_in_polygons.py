import math

def circle_diameter(sides: int, side_length: int): 
  return side_length / math.tan(math.pi / sides)

import codewars_test as test

@test.describe('Example Tests')
def example_tests():
    @test.it('Example Test Cases')
    def example_test_case():
        test.assert_approx_equals(circle_diameter(4, 5), 5.000, margin=1e-3)
        test.assert_approx_equals(circle_diameter(8, 9), 21.728, margin=1e-3)
        test.assert_approx_equals(circle_diameter(3, 4), 2.309, margin=1e-3)