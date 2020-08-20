# 30- Given 3 (float) numbers via input, calculate the solution of the associated 2-nd degree equation.

import math

a = float(input("Insert A: "))
b = float(input("Insert B: "))
c = float(input("Insert C: "))

delta = b * b - 4 * a * c

if delta > 0.0:
  x1 = (-b + math.sqrt(delta)) / 2 * a
  x2 = (-b - math.sqrt(delta)) / 2 * a

  print(f"x_1 = {x1}")
  print(f"x_2 = {x2}")
elif delta < 0.0:
  print("The equation does not admit real solutions.")
else:
  x = (-b + math.sqrt(delta)) / 2 * a

  print(f"x_1 = x_2 = {x}")

