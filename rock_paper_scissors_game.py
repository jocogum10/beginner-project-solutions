"""
### Rock Paper Scissors Game
- Create a rock-paper-scissors game.
- Ask the player to pick rock, paper or scissors.
- Have the computer chose its move.
- Compare the choices and decide who wins.
- Print the results.
- Subgoals:
  - Give the player the option to play again.
  - Keep a record of the score (e.g. Player: 3 / Computer: 6).
"""
import random

player_score = 0
computer_score = 0
weapon = ['rock', 'paper', 'scissors']
    
def battle(player, computer):
    global player_score, computer_score, weapon
    if player == 'rock' and computer == 'paper':
        print("computer won: player({0}) computer({1})".format(player, computer))
        computer_score += 1
        print("Player: {0} / Computer: {1}".format(player_score, computer_score))
    elif player == 'rock' and computer == 'scissors':
        print("player won: player({0}) computer({1})".format(player, computer))
        player_score += 1
        print("Player: {0} / Computer: {1}".format(player_score, computer_score))
        
    elif player == 'paper' and computer == 'rock':
        print("player won: player({0}) computer({1})".format(player, computer))
        player_score += 1
        print("Player: {0} / Computer: {1}".format(player_score, computer_score))
    elif player == 'paper' and computer == 'scissors':
        print("computer won: player({0}) computer({1})".format(player, computer))
        computer_score += 1
        print("Player: {0} / Computer: {1}".format(player_score, computer_score))
        
    elif player == 'scissors' and computer == 'paper':
        print("player won: player({0}) computer({1})".format(player, computer))
        player_score += 1
        print("Player: {0} / Computer: {1}".format(player_score, computer_score))
    elif player == 'scissors' and computer == 'rock':
        print("computer won: player({0}) computer({1})".format(player, computer))
        computer_score += 1
        print("Player: {0} / Computer: {1}".format(player_score, computer_score))
    elif player == computer:
        print("draw: player({0}) computer({1})".format(player, computer))
        print("Player: {0} / Computer: {1}".format(player_score, computer_score))
    else:
        print("Input Invalid")
        
if __name__ == '__main__':
    
    player_score = 0
    computer_score = 0
    weapon = ['rock', 'paper', 'scissors']
    
    while(True):
        player = input("rock, paper, scissors?:")
        computer = weapon[random.randrange(3)]
        print(player, computer)
        battle(player, computer)