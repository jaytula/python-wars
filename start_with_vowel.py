import re

def vowel_start(st: str): 
  st = st.lower()
  return re.sub(r'([aeiou])', r' \1', re.sub(r'[^a-z0-9]', '', st)).strip()

import codewars_test as test

@test.describe('Fixed Tests')
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_tests():
        test.assert_equals(vowel_start('It is beautiful weather today!'), 'it isb e a ut if ulw e ath ert od ay',)
        test.assert_equals(vowel_start('Coding is great'),'c od ing isgr e at',)
        test.assert_equals(vowel_start('my number is 0208-533-2325'),'myn umb er is02085332325' ,)
        test.assert_equals(vowel_start('oranges, apples, melon, pineapple'), 'or ang es appl esm el onp in e appl e', )
        test.assert_equals(vowel_start('under_score'), 'und ersc or e')