# 24 - Given 1 (integer) matrix, calculate its sum and print it on terminal.

matrix = [
  [8, 1, 9, 6, 7],
  [7, 1, 9, 3, 10],
  [9, 5, 8, 3, 6],
  [7, 9, 5, 10, 3],
  [5, 3, 2, 1, 7],
]

sum = 0

for row in matrix:
  for elem in row:
    sum += elem

print(sum)