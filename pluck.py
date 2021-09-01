from typing import Dict, List

def pluck(objs: List[Dict], name: str): 
    return [obj.get(name, None) for obj in objs]

import codewars_test as test

@test.describe('Example Tests')
def example_tests():
    objs = [{'a':1, 'b':2, 'c': 3}, {'a':4, 'b':5, 'c': 6}, {'a':7, 'b':8, 'c': 9}, {'a':10, 'b':11}]
    
    test.assert_equals(pluck(objs, 'a'), [1,4,7,10])
    test.assert_equals(pluck(objs, 'b'), [2,5,8,11])
    test.assert_equals(pluck(objs, 'c'), [3,6,9,None])