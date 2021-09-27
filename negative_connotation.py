import re

def connotation(strng: str):
    return sum([1 if re.match(r'[a-m]', w, re.IGNORECASE) else -1 
      for w in re.split(r'\s+', strng) if len(w) > 0]) >= 0

import codewars_test as test

test.it("True")
test.assert_equals(connotation("A big brown fox caught a bad bunny"), True)
test.it("False")
test.assert_equals(connotation("Xylophones can obtain Xenon."), False)
test.it("All caps")
test.assert_equals(connotation("CHOCOLATE MAKES A GREAT SNACK"), True)
test.it("Random case")
test.assert_equals(connotation("All FOoD tAsTEs NIcE for someONe"), True)
test.it("Random number of spaces")
test.assert_equals(connotation("Is  this the  best  Kata?"), True)
