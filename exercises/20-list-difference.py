# 20 - Given 2 (integer) lists (A and B), calculate the list difference element by element.

a = [51, 75, 87, 42, 85, 67, 86]
b = [51, 33, 64, 9, 97, 67, 69]

diff = []

for i in range(0, 7):
  x = a[i]
  y = b[i]

  diff.append(x == y)
