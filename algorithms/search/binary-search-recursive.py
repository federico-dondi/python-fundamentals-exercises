# WARN: binary-Search only works against sorted lists.

def binary_search(list, value):
  left = 0
  right = len(list) - 1

  found = False

  while left <= right:
    m = (left + right) // 2

    if list[m] > value:
      right = m - 1
    elif list[m] < value:
      left = m + 1
    else:
      found = True

  return found