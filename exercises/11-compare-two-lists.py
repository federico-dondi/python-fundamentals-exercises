# 11 - Given 2 (integer) lists, calculate if they're equal element by element and print it on the terminal.

equal = True

L1 = [67, 82, 100, 28, 22, 68]
L2 = [18, 27, 33, 13, 83, 61]

n = len(L1)

for i in range(0, n):
  if L1[i] != L2[i]:
    equal = False

if equal:
  print("Lists are equal.")
else:
  print("Lists aren't equal.")