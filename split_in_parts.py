def split_in_parts(s: str, part_length: int): 
    return ' '.join([s[i:i+part_length] for i in range(0, len(s), part_length)])


import codewars_test as test

@test.describe('Example Tests')
def example_tests():
    test.assert_equals(split_in_parts("supercalifragilisticexpialidocious", 3), "sup erc ali fra gil ist ice xpi ali doc iou s")
    test.assert_equals(split_in_parts("HelloKata", 1), "H e l l o K a t a")
    test.assert_equals(split_in_parts("HelloKata", 9), "HelloKata")