# 10 - Given 1 (integer) number via input, called N, take N (integer) numbers via input, calculate the minimum and print it on the terminal.

a = int(input("Enter a (integer) value: "))

if a > 100:
  a = 100

min = float("inf")

for i in range(0, a):
  b = int(input(f"Enter the {i}-th (integer) value: "))

  if min > b:
    min = b

print(min)