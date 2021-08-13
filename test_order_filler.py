from typing import Dict

def fillable(stock: Dict[str, int], merch: str, n: int):
  return stock[merch] >= n if merch in stock else False

import codewars_test as test

@test.describe("Sample tests")
def tests():
    @test.it("Some examples")
    def tests():
        stock = {
            'football': 4,
            'boardgame': 10,
            'leggos': 1,
            'doll': 5 }
        test.assert_equals(fillable(stock, 'football', 3), True)
        test.assert_equals(fillable(stock, 'leggos', 2), False)
        test.assert_equals(fillable(stock, 'action figure', 1), False)