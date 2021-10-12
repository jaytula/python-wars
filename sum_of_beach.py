import re

def sum_of_a_beach(beach: str):
    return len(re.split(r'sand|water|fish|sun', beach.lower())) - 1
    
import codewars_test as test

test.assert_equals(sum_of_a_beach("SanD"), 1)
test.assert_equals(sum_of_a_beach("sunshine"), 1)
test.assert_equals(sum_of_a_beach("sunsunsunsun"), 4)
test.assert_equals(sum_of_a_beach("123FISH321"), 1)