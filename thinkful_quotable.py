def quotable(name: str, quote: str):
    return f'{name} said: "{quote}"'

import codewars_test as test

test.describe('Basic Tests')
test.assert_equals(quotable('Grae', 'Practice makes perfect'), 'Grae said: "Practice makes perfect"')
test.assert_equals(quotable('Dan', 'Get back to work, Grae'), 'Dan said: "Get back to work, Grae"')
test.assert_equals(quotable('Alex', 'Python is great fun'), 'Alex said: "Python is great fun"')
test.assert_equals(quotable('Bethany', 'Yes, way more fun than R'), 'Bethany said: "Yes, way more fun than R"')
test.assert_equals(quotable('Darrell', 'What the heck is this thing?'), 'Darrell said: "What the heck is this thing?"')