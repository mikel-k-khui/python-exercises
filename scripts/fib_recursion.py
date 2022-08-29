def fib_recursion(k: int) -> int:
  if(k > 2):
    result = fib_recursion(k - 2) + fib_recursion(k - 1)
  elif(k == 2):
  	result = 1 + fib_recursion(k - 1)
  elif(k == 1):
    result = 0
  return result