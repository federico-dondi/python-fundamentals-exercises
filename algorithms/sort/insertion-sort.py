def insertion_sort(list): 
  for i in range(1, len(list)):
    # Pivot
    key = list[i]

    j = i - 1

    # Move all the elements greater than "key"
    while j >= 0 and key < list[j]:
      list[j + 1] = list[j]
      j -= 1

    # Move "key" into first position
    list[j + 1] = key