def skiponacci(n: int):
  sequence = []
  for i in range(1, n+1):
    if i == 1 or i == 2: sequence.append(1)
    else: sequence.append(sequence[-1] + sequence[-2])

  return ' '. join([str(item) if idx % 2 == 0 else 'skip' for idx, item in enumerate(sequence)])

import codewars_test as test

test.assert_equals(skiponacci(1), "1")
test.assert_equals(skiponacci(5), "1 skip 2 skip 5")
test.assert_equals(skiponacci(7), "1 skip 2 skip 5 skip 13")