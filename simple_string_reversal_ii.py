def solve(st: str,a: int,b: int):
    b = min(b, len(st))
    return st[0:a] + st[b:None if a == 0 else a-1:-1] + st[b+1:]
    
import codewars_test as test

test.it("Basic tests")
test.assert_equals(solve("codewars",1,5),"cawedors")
test.assert_equals(solve("codingIsFun",2,100),"conuFsIgnid")
test.assert_equals(solve("FunctionalProgramming", 2,15),"FuargorPlanoitcnmming")
test.assert_equals(solve("abcefghijklmnopqrstuvwxyz",0,20),"vutsrqponmlkjihgfecbawxyz")
test.assert_equals(solve("abcefghijklmnopqrstuvwxyz",5,20),"abcefvutsrqponmlkjihgwxyz")