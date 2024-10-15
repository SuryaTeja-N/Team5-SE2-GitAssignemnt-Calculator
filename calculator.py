# calculator.py
def add(x, y):
   """Addition"""
   return x + y
def subtract(x, y):
   """Subtraction"""
   return x - y

def multiply(x, y):
  """Multiplication"""
  return x * y
def divide(x, y):
  """Division"""
  if y == 0:
    raise ValueError("Cannot divide by zero!")
    return x / y

def sqrt(x):
  """Square root"""
  if y == 0:
    raise ValueError("Cannot divide by zero!")
  return x ** (1/2)

def mod(x, y):
  """Modulus"""
  return x % y
