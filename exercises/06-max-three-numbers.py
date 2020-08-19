# 06 - Given 3 (integer) numbers via input, calculate the maximum and print it on the terminal.

a = int(input("Enter a (integer) value: "))
b = int(input("Enter a (integer) value: "))
c = int(input("Enter a (integer) value: "))

if a > b and a > c:
  print("A is the maximum.")
elif b > a and b > c:
  print("B is the maximum.")
elif c > a and c > b:
  print("C is the maximum.")
else:
  print("Equals.")