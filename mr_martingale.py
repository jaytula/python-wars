from typing import List

def martingale(bank: int, outcomes: List[int]):
    balance = bank
    unit = 1
    for outcome in outcomes:
      balance -= unit*100
      if outcome == 1:
        balance += 2 * unit * 100
        unit = 1
      else:
        unit *= 2
    return balance

import codewars_test as test
   
basic_tests = [
  [500, [], 500],
  [1000, [1, 1, 0, 0, 1], 1300],
  [0, [0, 0, 0, 0, 1, 0, 0,], -200],
  [5100, [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0], 5600],
  [-500, [1, 1, 0, 1, 0, 1, 0], -200]
]

@test.describe("Example tests")
def test_group():
    @test.it("example tests")
    def test_case():
        for bankroll, rounds, output in basic_tests:
            test.assert_equals(martingale(bankroll, rounds), output)
