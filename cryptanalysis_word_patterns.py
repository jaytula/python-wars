from typing import Dict

def word_pattern(word: str):
    word = word.lower()
    count = 0
    d: Dict[str, int] = {}

    result = []

    for ch in word:
      if not ch in d:
        d[ch] = count
        count += 1
      result.append(str(d[ch]))
    return '.'.join(result)

import codewars_test as test

@test.describe("Example Tests")
def tests():
    test_cases = [
        (word_pattern("hello"), "0.1.2.2.3"),
        (word_pattern("heLlo"), "0.1.2.2.3"),
        (word_pattern("helLo"), "0.1.2.2.3"),
        (word_pattern("Hippopotomonstrosesquippedaliophobia"), "0.1.2.2.3.2.3.4.3.5.3.6.7.4.8.3.7.9.7.10.11.1.2.2.9.12.13.14.1.3.2.0.3.15.1.13")
    ]
    for n, (actual, expected) in enumerate(test_cases, 1):
        @test.it(f"Example Test {n}")
        def test_function():
            test.assert_equals(actual, expected)