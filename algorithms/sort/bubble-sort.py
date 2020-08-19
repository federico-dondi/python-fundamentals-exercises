def bubble_sort(list): 
  n = len(list)

  for i in range(n - 1):
    for j in range(0, n - i - 1):

      if list[j] > list[j+1]:
        # Swap the element's order
        a = list[j]
        b = list[j+1]

        list[j] = b
        list[j+1] = a