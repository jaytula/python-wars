def ordered_count(inp: str):
  d = {}
  for idx, ch in enumerate(inp):
    if not ch in d:
      d[ch] = { "count": 0, "order": idx}
    d[ch]['count'] = d[ch]['count']+1
  
  return [(x[0], x[1]['count']) for x in sorted(d.items(), key=lambda item: item[1]['order'])]

import codewars_test as test

test.describe("Basic Tests")

tests = (
    ('abracadabra', [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]),
    ('Code Wars', [('C', 1), ('o', 1), ('d', 1), ('e', 1), (' ', 1), ('W', 1), ('a', 1), ('r', 1), ('s', 1)])
)

for t in tests:
    inp, exp = t
    test.assert_equals(ordered_count(inp), exp)