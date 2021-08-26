from typing import List
import re

def build_inverted_index(collection: List[str], term: str, case_sensitive: bool, exact_match: bool):
  rgx = re.compile(fr"\b{term}\b" if exact_match else term, 0 if case_sensitive else re.IGNORECASE)

  return [idx+1 for idx, item in enumerate(collection) if rgx.search(item)]

import codewars_test as test

# test.assert_equals(actual, expected, [optional] message)
@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        test.assert_equals(build_inverted_index(['hello there', 'gEnErAl kenobi'],'general', True, False),[])
        test.assert_equals(build_inverted_index(['hello there', 'general kenobi'],'Hello', False, False),[1])
        test.assert_equals(build_inverted_index(['hello. there', 'general kenobi'],'hello', True, True),[1])
        test.assert_equals(build_inverted_index(['hellos there', 'general kenobi'],'Hello', False, False),[1])
        test.assert_equals(build_inverted_index(['hello there', 'general kenobi'],'Hello', True, False),[])
        test.assert_equals(build_inverted_index(['hello there', 'general kenobi'],'Hell', False, False),[1])

        test.assert_equals(build_inverted_index(['Lorem Ipsum Dolor', 'Hodor Dolor Hodor', 'Dolormiten are not a thing'],'Dolor', True, False),[1,2,3])
        test.assert_equals(build_inverted_index(['Rumpel Dumpel','Holger', 'Quadrumpel'],'UmPeL', False, False),[1,3])
        test.assert_equals(build_inverted_index(['Im Wald gibts nicht viel zu tun', 'Oooh du schoener Westerwald'],'wald', False, True),[1])