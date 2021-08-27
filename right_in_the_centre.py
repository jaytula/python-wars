import math

def is_in_middle(sequence: str):
    offset = math.floor((len(sequence)-3) / 2)
    return sequence[offset:offset+3] == 'abc' if len(sequence) % 2 == 1 else sequence[offset:offset+3] == 'abc' or sequence[offset+1:offset+4] == 'abc'
    
import codewars_test as test

@test.describe("is_in_middle")
def tests():
    @test.it("example test cases")
    def test_the_examples():
        test.assert_equals(is_in_middle("AAabcBB"), True)
        test.assert_equals(is_in_middle("AabcBB"), True)
        test.assert_equals(is_in_middle("AabcBBB"), False)
