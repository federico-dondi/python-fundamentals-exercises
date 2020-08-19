# 13 - Reverse the string "Hello, World" and print it on the terminal.

base = "Hello, World"
reverse = ""

for i in range(len(base) - 1, -1, -1):
  reverse += base[i]

print(f"The reverse of '{base}' is '{reverse}'.")