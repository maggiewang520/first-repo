print("this is a pythagorean triangle calculator!")
side_a = input("what is the length of the first side?")
side_b = input("What is the length of the second side?")

side1 = int(side_a)
side2 = int(side_b)

side3 = sqrt(side1 * side1 + side2 * side2)

print(f"the length of the hypotenuse is {side3}")
