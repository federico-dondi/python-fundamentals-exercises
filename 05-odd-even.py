# 05 - Given one (integer) number via input, calculate if it's odd or even.

a = int(input("Enter a (integer) value: "))

if a % 2 == 0:
  print("Your number is 'even'.")
else:
  print("Your number is 'odd'.")