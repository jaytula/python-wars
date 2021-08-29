from typing import List

def riders(stations: List[int]):
    riders = 1
    traveled = 0

    for station in stations:
      if traveled + station > 100:
        riders += 1
        traveled = 0

      traveled += station

    return riders

import codewars_test as test

@test.describe("Sample tests")
def testEx():
    test.assert_equals(riders([18, 15]), 1)
    test.assert_equals(riders([43, 23, 40, 13]), 2)
    test.assert_equals(riders([33, 8, 16, 47, 30, 30, 46]), 3)
    test.assert_equals(riders([6, 24, 6, 8, 28, 8, 23, 47, 17, 29, 37, 18, 40, 49]), 4)