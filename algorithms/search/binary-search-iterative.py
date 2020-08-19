# WARN: binary-Search only works against sorted lists.

def binary_search(list, left, right, value):
  if left > right: return False

  m = (left + right) // 2

  if list[m] > value:
    return binary_search(list, left, m - 1, value)
  elif list[m] < value:
    return binary_search(list, m + 1, right, value)
  else:
    return True

your_value = ...
your_list = ...

start = 0
end = len(your_list) - 1

found = binary_search(your_list, start, end, your_value)