def bus_timer(current_time: str):
  hours, minutes = [int(val) for val in current_time.split(':')]
  total = (hours*60 + minutes + 5) % (60*24)

  return 360 - total if total < 360 and total > 0 else (15 - total % 15) % 15

import codewars_test as test

test.assert_equals(bus_timer("10:00"), 10)
test.assert_equals(bus_timer("15:05"), 5)
test.assert_equals(bus_timer("06:10"), 0)