import pytest
def fibonacci (x):
  if x == 0:
    return 0
  elif x == 1:
    return 1
  else:
    return fibonacci(x-1) + fibonacci(x-2)
def factorial(x):
  if x == 0:
    return 1
  else:
    return x * factorial(x-1)
def test_fib():
  assert fibonacci(0) == 0
  assert fibonacci(1) == 1
  assert fibonacci(2) == 1
  assert fibonacci(3) == 2
  assert fibonacci(4) == 3
  assert fibonacci(5) == 5