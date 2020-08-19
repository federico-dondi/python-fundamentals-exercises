# 12 - Create some wrappers functions around the input() function, forcing the return type to "float" and "integer".

def input_wrapper_int(prompt):
  return int(input(prompt))

def input_wrapper_float(prompt):
  return float(input(prompt))