def selection_sort(list): 
  n = len(list)

  for i in range(n):
    min_index = i

    # Search the minimum into the sub-list
    for j in range(i + 1, n):
      if list[min_index] > list[j]:
        min_index = j

    # Swap the i-th elemente with the new minimum
    a = list[i]
    b = list[min_index]

    list[i] = b
    list[min_index] = a
