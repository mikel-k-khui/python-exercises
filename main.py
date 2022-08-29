import scripts.rps as rps
import scripts.fib_recursion as fib

choices = rps.get_choices()
print(choices)
print(rps.check_win(choices))

print(f"The 10th fib seq is {fib.fib_recursion(10)}")
