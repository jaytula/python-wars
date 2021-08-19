def vaporcode(s: str):
  return "  ".join(s.replace(' ', '').upper())

import codewars_test as test


@test.describe("Basic Tests")
def __():
    @test.it("Some Examples")
    def __():
        test.assert_equals(vaporcode("Lets go to the movies"),"L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S")
        test.assert_equals(vaporcode("Why isn't my code working?"),"W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?")