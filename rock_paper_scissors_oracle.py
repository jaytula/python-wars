from typing import List


def oracle(gestures: List[str]):
  def score_round(you, opponent):
    if you == opponent: return 0
    return {"rock": {"paper": -1, "scissors": 1}, "paper": {"scissors": -1, "rock": 1}, "scissors": {"rock": -1, "paper": 1}}[you][opponent]
  winning_hands = []

  for my_hand in ["rock", "paper", "scissors"]:
    score = sum([score_round(my_hand, opponent_hand) for opponent_hand in gestures])
    if score > 0: winning_hands.append(my_hand)

  return "/".join(winning_hands) if len(winning_hands) else "tie"
    

import codewars_test as test

@test.describe("Fixed Tests")
def fixed_test_cases():
    @test.it("Example Tests")
    def example_test_cases():
        test.assert_equals(oracle(["rock","paper","scissors","rock"]), "paper")
        test.assert_equals(oracle(["rock","paper","scissors"]), "tie")
        test.assert_equals(oracle(["rock","paper","paper","scissors","scissors"]), "scissors")
        test.assert_equals(oracle(["paper","scissors","scissors"]), "rock/scissors")