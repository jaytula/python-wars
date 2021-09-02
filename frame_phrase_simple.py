def frame(phrase: str = '', ch: str = '*'): 
    result = []
    result.append(ch * (len(phrase) + 4))
    result.append(ch + ' ' * (len(phrase) + 2) + ch)
    if phrase != '': result.append(ch + ' ' + phrase  +  ' ' + ch)
    result.append(ch + ' ' * (len(phrase) + 2) + ch)
    result.append(ch * (len(phrase) + 4))
    return '\n'.join(result)

import codewars_test as test

@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        test.assert_equals(frame("Yolo", "@"), "@@@@@@@@\n@      @\n@ Yolo @\n@      @\n@@@@@@@@")
        test.assert_equals(frame("Yolo"), "********\n*      *\n* Yolo *\n*      *\n********")
        test.assert_equals(frame("", ";"), ";;;;\n;  ;\n;  ;\n;;;;")
