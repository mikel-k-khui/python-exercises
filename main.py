from scripts.rps import get_choices, check_win # import module
import scripts.fib_recursion as fib # import from files

choices = get_choices()
print(f"Choices were {choices} and {check_win(choices)}")

print(f"The 10th fib seq is {fib.fib_recursion(10)}")

# apply slicing shorthand to list
print(['test', 'that', 'those'][0:2]) 