def to_jaden_case(string: str):
    return " ".join(word[0].upper() + word[1:] for word in string.split(' '))

import codewars_test as test

quote = "How can mirrors be real if our eyes aren't real"
test.assert_equals(to_jaden_case(quote), "How Can Mirrors Be Real If Our Eyes Aren't Real")