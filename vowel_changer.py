import re

def vowel_change(txt: str, vow: str):
    return re.sub(r'[aeiou]', vow, txt)

import codewars_test as test

@test.describe("Fixed Tests")
def f():
    @test.it('Basic Test Cases')
    def b():
        test.assert_equals(vowel_change("hannah hannah bo-bannah banana fanna fo-fannah fee, fy, mo-mannah. hannah!",'i'), 'hinnih hinnih bi-binnih binini finni fi-finnih fii, fy, mi-minnih. hinnih!');
        test.assert_equals(vowel_change('adira wants to go to the park', 'o'), 'odoro wonts to go to tho pork');
