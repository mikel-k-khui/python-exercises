from scripts.rps import get_choices, check_win # import module
import scripts.fib_recursion as fib # import from files
import argparse

# get user input
parser = argparse.ArgumentParser(description = "print something")
parser.add_argument('-c', '--cli_choice', metavar='cli_choice', required=False, choices={'rock', 'paper', 'scissors'}, help="Pick Rock, Paper, or Scissors")
args = parser.parse_args()
print(args.cli_choice)
                          
choices = get_choices(args.cli_choice)
print(f"Choices were {choices} and {check_win(choices)}")

print(f"The 10th fib seq is {fib.fib_recursion(10)}")

# apply slicing shorthand to list
print(['test', 'that', 'those'][0:2]) 
