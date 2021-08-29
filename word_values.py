from typing import List
import re

def name_value(my_list: List[str]):
  def get_value(letters: str):
    return sum([ord(letter) - ord('a') + 1 for letter in letters])
  return [(idx + 1) * get_value(re.sub(r'[^a-z]', '', item)) for idx, item in enumerate(my_list)]

import codewars_test as test
    
@test.describe("Fixed tests")
def fixed_tests():
    @test.it("")
    def f():
        test.assert_equals(name_value(["codewars","abc","xyz"]),[88,12,225])
        test.assert_equals(name_value(["abc abc","abc abc","abc","abc"]),[12,24,18,24])