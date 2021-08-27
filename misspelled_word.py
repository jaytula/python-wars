def mispelled(word1: str,word2: str):
    if word1 == word2: return True

    (shorter, longer) = sorted([word1, word2], key=lambda x: len(x))

    if len(longer) - len(shorter) > 1: return False
    if shorter in longer: return True
    if len(shorter) != len(longer): return False

    diff_count = 0

    for i, j in zip(shorter, longer):
      if i != j: diff_count += 1
      if diff_count == 2: return False

    return True

import codewars_test as test

@test.describe('Sample Tests')
def sample():
    test.assert_equals(mispelled('versed','xersed'),True)
    test.assert_equals(mispelled('versed','applb'),False)
    test.assert_equals(mispelled('versed','v5rsed'),True)
    test.assert_equals(mispelled('1versed','versed'),True)
    test.assert_equals(mispelled('versed','versed'),True)
    