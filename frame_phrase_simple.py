def frame(phrase, ch='*'): 
    # your code here
    pass

import codewars_test as test

@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        test.assert_equals(frame("Yolo", "@"), "@@@@@@@@\n@      @\n@ Yolo @\n@      @\n@@@@@@@@")
        test.assert_equals(frame("Yolo"), "********\n*      *\n* Yolo *\n*      *\n********")