import re
def word_splitter(string1: str):
    return re.split(r'[:;&|>?%!=#*+]', string1)

import codewars_test as test

example1 = word_splitter("12:56C:144:1000:1200")
test.it("Search the string for special Characters!")
test.assert_equals(example1, ["12","56C","144","1000","1200"])

example2 = word_splitter("23;RPM;300;PSI;MODE;FORWARD")
test.it("Search the string for special Characters!")
test.assert_equals(example2, ["23","RPM","300","PSI","MODE","FORWARD"])


example3 = word_splitter("340000.00*-140.49902*ELEVATION*24000000*END")
test.it("Search the string for special Characters!")
test.assert_equals(example3, ["340000.00","-140.49902","ELEVATION","24000000","END"])
