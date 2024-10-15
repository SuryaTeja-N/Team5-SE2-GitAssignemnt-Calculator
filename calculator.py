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
  return x ** (1/2)

def mod(x, y):
  """Modulus"""
  return x % y

def power(x, y):
  """Power"""
  return x ** y

def factorial(x):
  """Factorial"""
  if x < 0:
    raise ValueError("Cannot calculate factorial of a negative number!")
  result = 1
  for i in range(1, x + 1):
    result *= i
  return result

def logarithm(x, base):
  """Logarithm"""
  if x <= 0:
    raise ValueError("Logarithm undefined for non-positive values!")
  if base <= 0 or base == 1:
    raise ValueError("Logarithm base must be positive and not equal to 1!")
  result = 0
  while x >= base:
    x /= base
    result += 1
  return result
