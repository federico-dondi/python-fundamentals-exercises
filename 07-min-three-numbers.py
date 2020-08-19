# 07 - Given 3 (integer) numbers via input, calculate the minimum and print it on the terminal.

a = int(input("Enter a (integer) value: "))
b = int(input("Enter a (integer) value: "))
c = int(input("Enter a (integer) value: "))

if a < b and a < c:
  print("A is the minimum.")
elif b < a and b < c:
  print("B is the minimum.")
elif c < a and c < b:
  print("C is the minimum.")
else:
  print("Equals.")