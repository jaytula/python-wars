from typing import List

def words_to_sentence(words: List[str]):
    return ' '.join(words)

import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(words_to_sentence(['bacon', 'is', 'delicious']), 'bacon is delicious')
