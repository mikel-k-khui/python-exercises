import random

game_choices = ["rock", "paper", "scissors"]

def get_choices(player_choice = "paper"):
  if player_choice is None:
    player_choice = input("Input a choice of (rock, paper, scissors):")
  choices = { "player": player_choice, "computer": random.choice(game_choices) }
  return choices

choices = get_choices(random.choice(game_choices))
print(choices)
