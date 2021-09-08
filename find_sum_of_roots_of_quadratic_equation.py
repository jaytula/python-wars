import math

def roots(a,b,c):
  discriminant = b**2 - 4*a*c
  if discriminant < 0: return None

  root1 = (-b + math.sqrt(discriminant)) / (2*a)
  root2 = (-b - math.sqrt(discriminant)) / (2*a)
  return round(root1 + root2, 2)

import codewars_test as test

test.describe('Example tests')
test.assert_equals(roots(6,3,8),None)
test.assert_equals(roots(2,11,-6),-5.5)
test.assert_equals(roots(5,-8,3),1.6)
test.assert_equals(roots(6,4,9),None)
test.assert_equals(roots(1,-2,-5.25),2)
test.assert_equals(roots(3,-10,5),3.33)
test.assert_equals(roots(5,2,4),None)
test.assert_equals(roots(1,4,3),-4)
test.assert_equals(roots(2,3,1),-1.5)
test.assert_equals(roots(1,-4,4),4)
test.assert_equals(roots(1,3,9),None)
test.assert_equals(roots(1,-1,-20),1)
test.assert_equals(roots(2,-4,-2),2)
test.assert_equals(roots(6,11,-35),-1.83)
test.assert_equals(roots(3,4,9),None)
test.assert_equals(roots(-4,-7,12),-1.75)
test.assert_equals(roots(1,-1,-3),1)
test.assert_equals(roots(5,-2,-9),0.4)
test.assert_equals(roots(2,8,0),-4)
test.assert_equals(roots(3,5,10),None)
