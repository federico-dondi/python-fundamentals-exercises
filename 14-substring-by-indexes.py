# 14 - Given 2 (integer) number via input (I and J), calculate the substring of "Hello, World" starting from I, ending to J and print it on the terminal.

s = "Hello, World!"

i = int(input("Enter the start index: "))
j = int(input("Enter the finish index: "))

if i >= 0:
  if j < len(s):
    if i <= j:
      print(s[i:j])
    else:
      print("Finish index should be greater/equal to start index.")
  else:
    print("Finish index not valid.")
else:
  print("Start index not valid.")