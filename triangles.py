def input_sides():
  global side_a
  global side_b
  print("this is a pythagorean triangle calculator!")
  side_a = input("what is the length of the first side?")
  side_b = input("What is the length of the second side?")

def finding_side():
  global side_a
  global side_b
  global side1
  global side2
  global side3
  side1 = int(side_a)
  side2 = int(side_b)
  side3 = sqrt(side1 * side1 + side2 * side2)
  print(f"the length of the hypotenuse is {side3}")
