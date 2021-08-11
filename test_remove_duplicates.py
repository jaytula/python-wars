import unittest

def remove_duplicate_words(s: str):
    result = []
    words = s.split(" ")

    for word in words:
      if not word in result:
        result.append(word)
    
    return " ".join(result)

class TestRemoveDuplicates(unittest.TestCase):

  def test_duplicate_words(self):
    self.assertEqual(remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"), "alpha beta gamma delta")
    self.assertEqual(remove_duplicate_words("my cat is my cat fat"), "my cat is fat")

if __name__ == '__main__':
  unittest.main()
