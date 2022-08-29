from functools import reduce
from itertools import accumulate

def total_expenses(expenses):
  return reduce(lambda prev, curr: prev + curr[1], expenses, 0)
