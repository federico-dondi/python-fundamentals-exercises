# 21 - Given 1 charater via input, print on the terminal if it's contained into "Hello, World"

a = input("Enter a character: ")
b = "Hello, World"

found = False

for char in b:
  if char == a:
    found = True

if found:
  print("Character in string.")
else:
  print("Character not in string.")