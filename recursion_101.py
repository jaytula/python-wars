def solve(a: int, b: int):
  if a == 0 or b == 0: return [a, b]
  if a >= 2 * b:
    a = a - 2 * b
    return solve(a, b)
  if b >= 2 * a:
    b = b - 2 * a
    return solve(a, b)

  return [a, b]
    
import codewars_test as test

test.it("Basic tests")
test.assert_equals(solve(6,19),[6,7])
test.assert_equals(solve(2,1),[0,1])
test.assert_equals(solve(22,5),[0,1])
test.assert_equals(solve(2,10),[2,2])