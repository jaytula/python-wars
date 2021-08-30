import datetime

def solve(a,b):
    total = 0
    start_month = ''
    end_month = ''
    for year in range(a, b+1):
      for month in [1, 3, 5, 7, 8, 10, 12]:
        dt = datetime.date(year, month, 1)
        if dt.weekday() == 4:
          if start_month == '':
            start_month = dt.strftime('%b')
          end_month = dt.strftime('%b')

          total += 1
    return (start_month, end_month, total)

import codewars_test as test

test.it("Basic tests")
test.assert_equals(solve(2016,2020),("Jan","May",5))
test.assert_equals(solve(1900,1950),("Mar","Dec",51))
test.assert_equals(solve(1800,2500),("Aug","Oct",702))
