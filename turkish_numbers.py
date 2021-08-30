import math

def get_turkish_number(num):
  digits = [
    "sıfır",
    "bir",
    "iki",
    "üç",
    "dört",
    "beş",
    "altı",
    "yedi",
    "sekiz",
    "dokuz",
  ]
  tens = [
    "",
    "on",
    "yirmi",
    "otuz",
    "kırk",
    "elli",
    "altmış",
    "yetmiş",
    "seksen",
    "doksan",
  ]
  if num < 10: return digits[num]
  tensDigit = math.floor(num / 10)
  return (tens[tensDigit] + " " + ("" if num % 10 == 0 else digits[num % 10])).strip()


import codewars_test as test

test.assert_equals(get_turkish_number(1), "bir")
test.assert_equals(get_turkish_number(13), "on üç")
test.assert_equals(get_turkish_number(27), "yirmi yedi")
test.assert_equals(get_turkish_number(38), "otuz sekiz")
test.assert_equals(get_turkish_number(77), "yetmiş yedi")
test.assert_equals(get_turkish_number(94), "doksan dört")