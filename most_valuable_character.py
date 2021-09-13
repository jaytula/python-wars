def solve(st: str):
    most_valuable = ''
    value = 0

    for ch in st:
      current_value = st.rfind(ch) - st.find(ch)
      if most_valuable == '' or current_value > value or (current_value == value and ord(ch) < ord(most_valuable)):
        most_valuable = ch
        value = current_value

    return most_valuable

import codewars_test as test

@test.describe('Fixed Tests')
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_tests():        
        test.assert_equals(solve('a'), 'a')
        test.assert_equals(solve('aa'), 'a')
        test.assert_equals(solve('bcd'), 'b')
        test.assert_equals(solve('axyzxyz'), 'x') 
        test.assert_equals(solve('aabccc'), 'c') 