import scripts.rps as rps
import scripts.fib_recursion as fib

choices = rps.get_choices()
print(f"Choices were {choices} and {rps.check_win(choices)}")

print(f"The 10th fib seq is {fib.fib_recursion(10)}")

# apply slicing shorthand to list
print(['test', 'that', 'those'][0:2]) 