# test function int-to-roman in the Inttoroman python file
from InttoRoman import int_to_roman

def test_int_to_roman():
  num=[1, 2, 3, 4, 10, 50, 90, 500, 755]
  roman= ["I", "II", "III", "IV", "X", "L", "XC", "D", "DCCLV"]
  for i in range(len(num)):
    assert int_to_roman(num[i])== roman[i]

def main():
  test_int_to_roman()

if __name__ == '__main__':
  main()