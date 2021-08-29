class Person:
    def __init__(self, name: str) -> None:
        self.name = name
    def greet(self, friend: str):
      return "Hello %s, my name is %s" % (friend, self.name)

import codewars_test as test

jack = Person("Jack")
jill = Person("Jill")

test.assert_equals(jack.greet("Jill"), "Hello Jill, my name is Jack")
test.assert_equals(jack.greet("Mary"), "Hello Mary, my name is Jack")

test.assert_equals(jill.greet("Jack"), "Hello Jack, my name is Jill")
test.assert_equals(jill.name, 'Jill', "Person's name could not be retrieved")