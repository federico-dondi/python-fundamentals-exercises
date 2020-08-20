# 29 - Collect the votes of a hypothetical poll, calculate the result and print it on the terminal.

gandalf = 0
ragadast = 0
saruman = 0

ask = True

while ask:
  value = input("(G)Gandalf, (R)Ragadast, (S)Saruman, (O)Fine")

  if value == "G":
    gandalf += 1
  elif value == "R":
    ragadast += 1
  elif value == "S":
    saruman += 1
  elif value == "=":
    ask = False
  else:
    print("Valore non valido.")

if gandalf > ragadast and gandalf > saruman:
  print("(G)Gandalf vince.")
if ragadast > gandalf and ragadast > saruman:
  print("(R)Ragadast vince.")
if saruman > gandalf and saruman > ragadast:
  print("(S)Saruman vince.")
else:
  print("Nessun vincitore.")