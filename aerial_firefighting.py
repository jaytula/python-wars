import re

def waterbombs(fire: str, w: int):
    return [len(s) // w if len(s) % w == 0 else len(s) // w + 1 for s in re.split(r'Y+', fire)]
    

import codewars_test as test

test.it("Basic Tests")
# test.assert_equals(waterbombs("xxxxYxYx", 4), 3)
# test.assert_equals(waterbombs("xxYxx", 3), 2)
test.assert_equals(waterbombs("xxxYYxxYYxxxxYx", 2), 6)