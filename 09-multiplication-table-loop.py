# 09 - Given 1 (integer) number via input, calculate its multiplication-table and print it on the terminal.

a = int(input("Enter a (integer) value: "))
 
for i in range(0, 11):
  print(f"{a} * {i} = {a * i}")