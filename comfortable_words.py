def comfortable_word(word: str):
  letter_groups = ('qwertasdfgzxcvb', 'yuiophjklnm')
  start_group = 0 if word[0] in letter_groups[0] else 1

  return all([letter in letter_groups[(start_group + idx) % 2] for idx, letter in enumerate(word)])

import codewars_test as test

test.describe("comfortable_words:")

test.it("should return True for comfortable words")
word = 'yams'
test.assert_equals(comfortable_word(word), True, '"{}" is a comfortable word!'.format(word))

test.it("should return False for uncomfortable words")
word = 'test'
test.assert_equals(comfortable_word(word), False, '"{}" is NOT a comfortable word!'.format(word))