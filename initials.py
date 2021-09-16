def initials(name: str):
    segments = name.split(' ')
    return '.'.join([
      s.capitalize() if idx == len(segments) - 1 else s[0].upper() 
      for idx, s in enumerate(segments)
    ])

import codewars_test as test

test.assert_equals(initials('code wars'),'C.Wars')
test.assert_equals(initials('Barack hussein obama'),'B.H.Obama')
test.assert_equals(initials('barack hussein Obama'),'B.H.Obama')