import math

def coordinates(degrees: int, radius: int):
  x = math.cos(degrees * math.pi / 180) * radius
  y = math.sin(degrees * math.pi / 180) * radius
  return (round(x, 10), round(y, 10))

import codewars_test as test

test.assert_equals(coordinates(45, 1), (0.7071067812, 0.7071067812))
test.assert_equals(coordinates(90, 1), (0.0, 1.0))