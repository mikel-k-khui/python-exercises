import argparse
from scripts.rps import get_choices, check_win # import module
import scripts.fib_recursion as fib # import from files
from scripts.lambda_reduce import total_expenses
from scripts.dog import Dog

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

print(f"what is the total travel expenses? {total_expenses([('gas', 20), ('hotel', 90), ('drinks', 40)])}")

Spock = Dog("Spock", 9)
Kirk = Dog("Kirk", 8)
Spock.bark()
Kirk.walk()
print(f"Is Spock older than Kirk? {Spock > Kirk}")
# print(help(Dog))