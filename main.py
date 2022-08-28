import random

game_choices = ["rock", "paper", "scissors"]

def get_choices(player_choice = "paper"):
  if player_choice is None:
    player_choice = input("Input a choice of (rock, paper, scissors):")
  choices = { "player": player_choice, "computer": random.choice(game_choices) }
  return choices

def check_win(choices):
  player = choices["player"]
  computer = choices["computer"]
  if player == computer:
    return "It's a tie" 
  elif player == "rock":
    return "You Win! Rock smashs scissors" if computer == "scissors" else "You Lost! Paper covers rock"
  elif player == "paper":
    return "You Win! Papers cover rock" if computer == "rock" else "You Lost! Scissors cuts paper"
  elif player == "scissors":
    return "You Win! Scissors cuts paper" if computer == "paper" else "You Lost! Rock smashs scissors"


choices = get_choices(random.choice(game_choices))
print(choices)
print(check_win(choices))
