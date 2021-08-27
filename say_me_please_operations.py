def say_me_operations(string_numbers: str):
    numbers = [int(num) for num in string_numbers.split(' ')]

    def get_operation(idx: int, num: int):
      if numbers[idx] + numbers[idx+1] == num: return 'addition'
      if numbers[idx] - numbers[idx+1] == num: return 'subtraction'
      if numbers[idx] * numbers[idx+1] == num: return 'multiplication'
      return 'division'

    return ', '.join([get_operation(idx, num) for idx, num in enumerate(numbers[2:])])

import codewars_test as test

@test.describe("say me operations")
def test_group():
    @test.it("basic")
    def basic():
        test.assert_equals(say_me_operations("1 2 3 5 8"), "addition, addition, addition")
        test.assert_equals(say_me_operations("9 4 5 20 25"), "subtraction, multiplication, addition")
        test.assert_equals(say_me_operations("10 2 5 -3 -15 12"), "division, subtraction, multiplication, subtraction")
        test.assert_equals(say_me_operations("2 2 4"), "addition")