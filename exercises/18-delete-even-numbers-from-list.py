# 17 - Given 1 (integer) list, delete all its even values.

values = [
  64, 
  34, 
  25, 
  12, 
  22, 
  11, 
  90
]

for v in values:
  if v % 2 == 0:
    values.remove(v)
