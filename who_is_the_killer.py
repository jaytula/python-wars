from typing import Dict, List

def killer(suspect_info: Dict[str, List[str]], dead: List[str]):
    for name, seen in suspect_info.items():
      if all([person in seen for person in dead]):
        return name
      

import codewars_test as test

@test.describe("Killer")
def tests():
    @test.describe("Basic tests")
    def basic():
        test.assert_equals(killer({'James': ['Jacob', 'Bill', 'Lucas'], 'Johnny': ['David', 'Kyle', 'Lucas'], 'Peter': ['Lucy', 'Kyle']}, ['Lucas', 'Bill']), 'James')
        test.assert_equals(killer({'Brad': [], 'Megan': ['Ben', 'Kevin'], 'Finn': []}, ['Ben']), 'Megan')