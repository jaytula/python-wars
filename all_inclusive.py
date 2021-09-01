from typing import List

def contain_all_rots(strng: str, arr: List[str]):
    rotations = [
      strng[len(strng)-i:] + strng[0:len(strng)-i] 
      for i in range(len(strng))
    ]

    missing = [rotation for rotation in rotations if not rotation in arr]
    
    return len(missing) == 0
    

import codewars_test as test

def testing(actual, expected):
    test.assert_equals(actual, expected)

test.describe("contain_all_rots")
test.it("Basic tests")
testing(contain_all_rots("", []), True)
testing(contain_all_rots("", ["bsjq", "qbsj"]), True)
testing(contain_all_rots("bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]), True)
testing(contain_all_rots("XjYABhR", ["TzYxlgfnhf", "yqVAuoLjMLy", "BhRXjYA", "YABhRXj", "hRXjYAB", "jYABhRX", "XjYABhR", "ABhRXjY"]), False)
