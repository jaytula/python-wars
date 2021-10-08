import re

def remove_chars(s: str):
    return re.sub(r'[^a-zA-Z ]', '', s) 

import codewars_test as test

test.assert_equals(remove_chars("test for error!"),"test for error", 'remove_chars("test for error!") did not return correct value')
test.assert_equals(remove_chars(".tree1"),'tree', 'remove_chars".tree1") did not return correct value')
