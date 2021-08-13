from typing import List

def determine_sequence(series_array: List[int]):
  if len(series_array) == 1:
    return 0
  common_difference = series_array[1] - series_array[0]
  common_ratio = series_array[1] / series_array[0] if series_array[0] != 0 else 0

  isAP = True
  isGP = True

  for i in range(1, len(series_array)):
    if series_array[i] - series_array[i-1] != common_difference:
      isAP = False
    if series_array[i-1] == 0 or series_array[i] / series_array[i-1] != common_ratio:
      isGP = False

  if isAP and isGP:
    return 2
  elif isAP:
    return 0
  elif isGP:
    return 1
  else:
    return -1
  

import codewars_test as test

@test.describe("Determine Sequence")
def tests():
    @test.it("Example Test Cases")
    def test_determine_sequence():
        test.assert_equals(determine_sequence([2, 5, 8, 11, 14]), 0) #It is an AP
        test.assert_equals(determine_sequence([1, 2, 4, 8, 16]), 1) #It is a GP
        test.assert_equals(determine_sequence([1, 2, 1, 3, 4, 5]), -1) #It is not a series
        test.assert_equals(determine_sequence([1, 1, 1, 1, 1]), 2) #It is both an AP and GP
        test.assert_equals(determine_sequence([1, 0, 0, 0, 0]), -1)
        test.assert_equals(determine_sequence([100, 0, 0, 0, 0]), -1)