def prev_mult_of_three(n: int):
    while True:
      s = str(n)
      if n % 3 == 0:
        return n
      if len(s) == 1:
        return None
      n = int(s[0:-1])
      
import codewars_test as test

@test.describe("Tests")
def tests():
    @test.it("Basic tests")
    def basic_tests():
        test.assert_equals(prev_mult_of_three(1), None)
        test.assert_equals(prev_mult_of_three(25), None)
        test.assert_equals(prev_mult_of_three(36), 36)
        test.assert_equals(prev_mult_of_three(1244), 12)
        test.assert_equals(prev_mult_of_three(952406), 9)