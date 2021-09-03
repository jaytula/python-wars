import math

def cost(mins: int):
  if mins == 0: return 0
  
  billable = max(mins - 65, 0) / 30
  return 30 + math.ceil(billable) * 10

import codewars_test as test

@test.describe('Basic Tests')
def fixed_tests():
    @test.it('It should works for basic tests.')
    def basic_tests():
        test.assert_equals(cost(45),30)
        test.assert_equals(cost(63),30)
        test.assert_equals(cost(84),40)
        test.assert_equals(cost(102),50)
        test.assert_equals(cost(273),100)