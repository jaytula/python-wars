def infected(s: str):
    groups = [('1' in group, len(group)) for group in s.split('X')]

    infected_count = 0
    total = 0
    for is_infected, count in groups:
      if is_infected:
        infected_count += count
      total += count

    return 0 if total == 0 else infected_count / total * 100

import codewars_test as test

@test.describe("Sample Tests")
def _():
    fixeds = [
        ("01000000X000X011X0X",73.33333333333333),
        ("01X000X010X011XX", 72.72727272727273),
        ("XXXXX", 0),
        ("00000000X00X0000", 0),
        ("0000000010", 100),
        ("000001XXXX0010X1X00010", 100),
        ("X00X000000X10X0100",42.857142857142854),
    ]
    for inp,exp in fixeds:
        test.assert_approx_equals(infected(inp),exp)