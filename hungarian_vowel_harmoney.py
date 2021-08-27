# -*- coding: utf-8 -*-
import re

def dative(word: str):
  nek_vowels = 'eéiíöőüű'
  nak_vowels = 'aáoóuú'
  vowels = re.sub(fr'[^{nek_vowels}{nak_vowels}]', '', word)

  return word + 'nek' if vowels[-1] in nek_vowels else word + 'nak'

import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():

        tests = [
            # [input, expected],
            [u"ablak", u"ablaknak"],
            [u"tükör", u"tükörnek"],
            [u"keret", u"keretnek"],
            [u"otthon", u"otthonnak"],
            [u"virág", u"virágnak"],
            [u"tett", u"tettnek"],
            [u"rokkant", u"rokkantnak"],
            [u"rossz", u"rossznak"],
            [u"gonosz", u"gonosznak"],
            [u"rög", u"rögnek"],
            [u"király", u"királynak"],
        ]
        
        for inp, exp in tests:
            print("%s -> %s" % (inp, exp))
            test.assert_equals(dative(inp), exp)
    